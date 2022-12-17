from datetime import datetime
from sqlalchemy.ext.asyncio import create_async_engine,  AsyncSession
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey


engine = create_async_engine('postgresql+asyncpg://app_aio:5555@127.0.0.1:7778/app_aio')
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class UserAio(Base):

    __tablename__ = 'users_aio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String)
    create_time = Column(DateTime, default=datetime.utcnow())

class AdvAio(Base):

    __tablename__ = 'advertisements'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    text = Column(Text)
    published_at = Column(DateTime, default=datetime.utcnow())
    owner_id = Column(Integer, ForeignKey("users_aio.id", ondelete="CASCADE"))
    owner = relationship("UserAio", lazy="joined")
