import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Book(Base):
    """
    ORM对象：书
    """
    __tablename__ = 'books'

    uuid = Column(UUID, default=lambda: str(uuid.uuid1()), primary_key=True)  # default=lambda: str(uuid.uuid1())
    # 书名
    name = Column(String(length=50))
    # 作者
    author = Column(String(length=50))
    # 类别
    category = Column(String(length=15))
    # 网址
    website = Column(Text)

