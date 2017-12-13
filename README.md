# crawl_book

## 爬取豆瓣指定页数书单

> 1.初始化数据库
> > python manage.py rebuild_db
> 
> 2.爬取
> > python manage.py crawl [num]
> > 
> > num:(可选)表示要爬取的页数，默认为100
>
> 3.环境
> > xpath、lxml、SQLAlchemy、postgresql
> 

注：爬取代码所使用的自动获取代理脚本地址：[ProxyPool](https://github.com/TitorX/ProxyPool "ProxyPool")

		