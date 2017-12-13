from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crawl.config import DB_SETTINGS
from crawl.models import Book, Base

engine = create_engine('{0}://{1}:{2}@{3}/{4}'.
                       format(DB_SETTINGS['POSTGRESQL_DIRVER'],
                              DB_SETTINGS['POSTGRESQL_USERNAME'],
                              DB_SETTINGS['POSTGRESQL_PASSWORD'],
                              DB_SETTINGS['POSTGRESQL_HOST'],
                              DB_SETTINGS['POSTGRESQL_DB']))


def get_session():
    """
    获取postgresql连接
    :return:
    """
    Session = sessionmaker(bind=engine)
    return Session()


def rebuild_db():
    """
    c初始化数据库
    :return:
    """
    Base.metadata.create_all(engine)
