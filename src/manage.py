import sys

from crawl import  rebuild_db
from crawl.views import crawl_book

input_data = sys.argv

if __name__ == '__main__':
    if len(input_data) == 2 and 'rebuild_db' in input_data[1]:
        # 重建数据库
        rebuild_db()
    elif len(input_data) == 2 and 'crawl' in input_data[1]:
	# 爬取
	crawl_book()
    elif len(input_data) == 3 and 'crawl' in input_data[1]:
        # 爬取指定页数
        crawl_book(input_data[2])
    else:
 	print('参数输入有误！')
