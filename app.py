from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Customer,Base

engine=create_engine("sqlite:///Vehicle.db")
Base.metadata.bind=engine

Session=sessionmaker(bind=engine)

session=Session()

def add_customer(cname,cphno,cemail,caddress):
	customer=Customer(customer_name=cname,customer_phno=cphno,customer_email=cemail,customer_address=caddress)
	session.add(customer)
	session.commit()
def add_employee(eid, ename, edob, eeid, epass):
	employee=Employee_details(emp_id=eid, emp_name=ename, emp_dob=edob, emp_password=epass)
	session.add(customer)
	session.commit()