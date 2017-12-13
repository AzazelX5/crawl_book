import random
import json

from crawl import get_session
from crawl.config import User_Agent
from crawl.models import Book

from lxml import etree
from urllib import request
from urllib.error import HTTPError


def get_proxy(num=1):
    """
    获取免费代理
    :param num: 获取数量
    :return:
    """
    url_base = 'http://0.0.0.0:5454?num={0}'
    result = request.urlopen(url_base.format(num)).read()
    proxy_dict = json.loads(result)

    return proxy_dict['proxies']


def crawl_book(index=100):
    """
    爬取豆瓣书单
    :param index: 需要爬取的页数
    :return:
    """
    # 获取数据库连接
    session = get_session()
    # 代理ip列表
    ip_list = get_proxy()

    loop = 0
    while loop < index:
        print('正在爬取第{0}页'.format(loop+1))

        url = 'https://read.douban.com/kind/1?start={0}&sort=hot&' \
              'promotion_only=False&min_price=None&max_price=None&' \
              'works_type=None'.format(loop*20)
        while True:
            try:
                proxy_support = request.ProxyHandler({'http': ip_list[0]})
                opener = request.build_opener(proxy_support)
                # 随机获取一个User-Agent
                opener.addheaders = [('User-Agent', random.choice(User_Agent))]

                html = opener.open(url).read()
                # 代理IP可用，则跳出循环
                break
            except HTTPError:
                # 代理IP不可用，则更新代理IP列表后跳过本次循环
                ip_list[0] = get_proxy()[0]
                continue

        selector = etree.HTML(html)

        book_list = selector.xpath('//div[@class="info"]')
        num = 0
        for book in book_list:
            num += 1
            print('--第{0}本书'.format(loop*20+num))

            # 获取书名
            name = book.xpath('div[@class="title"]/a')[0].text
            # 获取网址
            website = book.xpath('div[@class="title"]/a/@href')[0].strip()
            # 获取作者
            author_list = book.xpath('p/span/span[@class="labeled-text"]/a')
            if len(author_list) == 0:
                author = None
            else:
                author = author_list[0].text
            # 获取类别
            category = book.xpath(
                'p/span[@class="category"]/span[@class="labeled-text"]/'
                'span[@itemprop="genre"]')[0].text

            book = Book(name=name, author=author, website=website,
                        category=category)

            print('爬取成功，正在添加到数据库中。。。')
            session.add(book)
            session.commit()
            print('添加成功！\n')

        loop += 1

    session.close()
