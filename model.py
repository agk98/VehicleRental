from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base=declarative_base()

class Employees(Base):
	__tablename__="Employees"

	name= Column('name', String)
	id= Column('Emp_id', String, primary_key=True, unique=True)

engine=create_engine('sqlite:///users.db')
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)

session=Session()

users=session.query(Employees).all()
for user in users:
	print("User with username=%s and id=%s"%(user.username, user.id))

session.close()