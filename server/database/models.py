from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, BINARY, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime as dt

CBase = declarative_base()


class Client(CBase):
    """

    """
    __tablename__ = "client"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(BINARY(), nullable=False)
    info = Column(String(255), default="")
    online_status = Column(Boolean(), default=False)


class History(CBase):
    """

    """
    __tablename__ = "history"

    id = Column(Integer(), primary_key=True)
    time = Column(DateTime(), default=dt.now(), nullable=False)
    ip_addr = Column(String(255))
    client_id = Column(Integer(), ForeignKey("client.id"))
    client = relationship("Client",
                          backref=backref("history", order_by=client_id))