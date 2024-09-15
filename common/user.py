from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'ip_data'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True, unique = True )
    JSON = Column(String, index=True)