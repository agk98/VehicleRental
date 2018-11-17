5
#!/usr/bin/python3

import mysql.connector as my

# Open database connection
db = my.connect(host="localhost",user="root",passwd="root",database="vehicle" )

cur=db.cursor()

def get_car_prices():
	sql="SELECT * FROM car_price"
	cur.execute(sql)

	prices=cur.fetchall()
	return prices

def get_bike_prices():
	sql="SELECT * FROM bike_price"
	cur.execute(sql)

	prices=cur.fetchall()
	return prices


def get_employee():
	sql="SELECT * FROM employee_details"
	cur.execute(sql)

	employeee=cur.fetchall()
	return employeee


def calculating_car_price(days, model, new_car):
	query="SELECT {} FROM car_price WHERE car_model='{}'"
	q=query.format(days, model)
	cur.execute(q)
	price=cur.fetchall()
	for x in price:
		new_car=x[0]
	return new_car

def calculating_bike_price(days, model, new_bike):
	query="SELECT {} FROM bike_price WHERE bike_model='{}'"
	q=query.format(days, model)
	cur.execute(q)
	price=cur.fetchall()
	for x in price:
		new_bike=x[0]
	return new_bike



def adding_customer(c_id, c_name, c_phno, c_email, c_addr):

	query="INSERT INTO customer_details VALUES( %s, %s, %s, %s, %s)"
	values=(c_id, c_name, c_phno, c_email, c_addr)

	cur.execute(query, values)
	db.commit()

def employee_insertion(emp_id, emp_name, emp_dob, emp_eid, emp_pass):
	query="INSERT INTO employee_details VALUES(%s, %s, %s, %s, %s);"
	val=(emp_id, emp_name, emp_dob, emp_eid, emp_pass)

	cur.execute(query, val)
	db.commit()

def removing_employee(emp_id):
	query="DELETE FROM employee_details WHERE emp_id=%s"
	val=(emp_id,)

	cur.execute(query, val)
	db.commit()

def retrieve_login(emp_id, emp_pass):
	query="SELECT * FROM employee_details WHERE emp_id=%s AND emp_pass=%s"
	values=(emp_id, emp_pass,)

	cur.execute(query, values)
	details=cur.fetchall()
	if not details:
		return 0
	else:
		return 1
	db.commit()