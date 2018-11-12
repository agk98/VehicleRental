import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

Base=declarative_base()

class Customer(Base):

	__tablename__='Customers'

	customer_id=Column(Integer,primary_key=True)
	customer_name=Column(String(40),nullable=False)
	customer_phno=Column(String(10),nullable=False)
	customer_email=Column(String(30),nullable=False)
	customer_address=Column(String(50),nullable=False)








engine = create_engine("sqlite:///Vehicle.db")
Base.metadata.create_all(engine)