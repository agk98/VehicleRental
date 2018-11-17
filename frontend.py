import tkinter as tk
import datetime
from tkinter.ttk import *
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from backend import *


LARGE_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 9)

class common_variable():
	cur_customer=None
	cur_customerID=None
	cur_vehicle=None
	cur_date=None
	cur_duration=None
	cur_price=None

class TSE(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container=ttk.Frame(self)				

		container.grid()

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}							

		for F in (Home, Admin_Login, Second_page, Adding_emp, removing_emp, Employee_login, Customer_details, VehicleType, CAR, BIKE): 

			frame=F(container, self)		

			self.frames[F]=frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(Home)			

	def show_frame(self, cont):
		frame=self.frames[cont]
		frame.tkraise()	

class Home(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label1=Label(self, text="VEHICLE RENTAL", font=LARGE_FONT)
		admin_log=Button(self, text="ADMIN LOGIN", command=lambda: controller.show_frame(Admin_Login))
		emp_log=Button(self, text="EMPLOYEE LOGIN", command=lambda: controller.show_frame(Employee_login))

		label1.grid(row=0, column=1, sticky='w')
		admin_log.grid(row=1, column=0, sticky='w')
		emp_log.grid(row=1, column=1, sticky='w')




class Admin_Login(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.password="irule"

		self.label1=Label(self, text="ADMIN LOGIN", font=LARGE_FONT)
		self.label2=Label(self, text="Admin Password", font=SMALL_FONT)
		self.entered_pass=Text(self, height=2, width=30)
		self.login=Button(self, text="LOGIN", command=self.checking)
		self.back=Button(self, text="BACK", command=lambda: controller.show_frame(Home))

		self.label1.grid(row=0, column=1, sticky='w')
		self.label2.grid(row=1, column=0, sticky='w')
		self.entered_pass.grid(row=1, column=1, sticky='w')
		self.back.grid(row=2, column=0, sticky='w')
		self.login.grid(row=2, column=1, sticky='w')
	def checking(self):
		
		if self.entered_pass.get("1.0","end-1c")==self.password:
			self.entered_pass.delete("1.0","end")
			self.controller.show_frame(Second_page)
		else:
			app.destroy()

class Second_page(Frame):															# Add to frames list
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller

		label=Label(self, text="ADMIN OPERATIONS", font=LARGE_FONT)
		add_employee=Button(self, text="ADD EMPLOYEE", command=lambda: self.controller.show_frame(Adding_emp))
		del_employee=Button(self, text="REMOVE EMPLOYEE", command=lambda: self.controller.show_frame(removing_emp))

		label.grid(row=0, column=1, sticky='w')
		add_employee.grid(row=1, column=0, sticky='w')
		del_employee.grid(row=2, column=0, sticky='w')

class Adding_emp(Frame):
	

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.Top=Label(self, text="ENTER EMPLOYEE DETAILS", font=LARGE_FONT)
		self.Id=Label(self, text="Employee ID:", font=SMALL_FONT)
		self.name=Label(self, text="Name:", font=SMALL_FONT)
		self.date_of_birth=Label(self, text="Date Of Birth:", font=SMALL_FONT)
		self.email_id=Label(self, text="Email ID:", font=SMALL_FONT)
		self.password=Label(self, text="Password:", font=SMALL_FONT)

		self.EID=Text(self, height=2, width=30)
		self.ename=Text(self, height=2, width=30)
		self.edob=Text(self, height=2, width=30)
		self.eemail_id=Text(self, height=2, width=30)
		self.Password=Text(self, height=2, width=30)

		self.Top.grid(row=0, column=1, sticky='w')
		self.Id.grid(row=1, column=0, sticky='w')
		self.EID.grid(row=1, column=1, sticky='w')
		self.name.grid(row=2, column=0, sticky='w')
		self.ename.grid(row=2, column=1, sticky='w')	
		self.date_of_birth.grid(row=3, column=0, sticky='w')
		self.edob.grid(row=3, column=1, sticky='w')
		self.email_id.grid(row=4, column=0, sticky='w')
		self.eemail_id.grid(row=4, column=1, sticky='w')
		self.password.grid(row=5, column=0, sticky='w')
		self.Password.grid(row=5, column=1, sticky='w')


		back=Button(self, text="LOGOUT", command=lambda: controller.show_frame(Home))
		Add=Button(self, text="ADD", command=self.add)
		back.grid(row=6, column=0, sticky='w')
		Add.grid(row=6, column=1, sticky='w')

	def add(self):
		self.emp_id=self.EID.get("1.0","end-1c")
		self.emp_name=self.ename.get("1.0","end-1c")
		self.emp_dob=self.edob.get("1.0","end-1c")
		self.emp_emailID=self.eemail_id.get("1.0","end-1c")
		self.emp_password=self.Password.get("1.0","end-1c")

		self.EID.delete("1.0","end")
		self.ename.delete("1.0","end")
		self.edob.delete("1.0","end")
		self.eemail_id.delete("1.0","end")
		self.Password.delete("1.0","end")
			# insert code to insert values into employee table
		
		employee_insertion(self.emp_id, self.emp_name, self.emp_dob, self.emp_emailID, self.emp_password)

		self.controller.show_frame(Home)


class removing_emp(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller

		self.header=Label(self, text="REMOVE EMPLOYEE", font=LARGE_FONT)
		self.label=Label(self, text="Enter Employee ID:", font=SMALL_FONT)
		self.textbox=Text(self, height=2, width=30)
		self.remove=Button(self, text="REMOVE", command=self.rem)

		self.header.grid(row=0, column=1, sticky='w')
		self.label.grid(row=1, column=0, sticky='w')
		self.textbox.grid(row=1, column=1, sticky='w')
		self.remove.grid(row=2, column=2, sticky='w')

	def rem(self):

		self.rem_emp=self.textbox.get("1.0","end-1c")
		self.textbox.delete("1.0","end")
		removing_employee(self.rem_emp)
		
		self.controller.show_frame(Home)



class Employee_login(Frame):
	def hello(self):
		self.e_id=self.emp_id.get("1.0","end-1c")
		self.pas=self.password.get("1.0","end-1c")

		self.emp_id.delete("1.0","end")
		self.password.delete("1.0","end")
			
		auth=retrieve_login(self.e_id, self.pas)
		
		if auth == 1:
			self.controller.show_frame(Customer_details)
		elif auth == 0:
			self.controller.show_frame(Employee_login)


	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		self.label1=tk.Label(self, text="EMPLOYEE LOGIN", font=LARGE_FONT)	
		self.label1.grid(row=0, column=1,sticky='W')

		self.label2=tk.Label(self,text="Employee ID", font=LARGE_FONT)
		self.label2.grid(row=1,column=0,sticky='w')
		self.label3=tk.Label(self,text="Password", font=LARGE_FONT)
		self.label3.grid(row=2,column=0,sticky='w')


		self.emp_id=tk.Text(self, height=2,width=30)
		self.password=tk.Text(self, height=2, width=30)

		self.emp_id.grid(row=1,column=2,padx=10,pady=10)
		self.password.grid(row=2,column=2,padx=10,pady=10)

		self.button1=tk.Button(self, text="LOGIN", command=self.hello)
		self.button1.grid(row=4, column=0, sticky='W')

	

class Customer_details(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller  = controller

		label1=tk.Label(self, text="CUSTOMER DETAILS", font=LARGE_FONT)
		label=Label(self, text="Customer ID:", font=LARGE_FONT)
		label2=tk.Label(self, text="Name", font=SMALL_FONT)
		label3=tk.Label(self, text="Phone Number", font=SMALL_FONT)
		label4=tk.Label(self, text="Email ID", font=SMALL_FONT)
		label5=tk.Label(self, text="Address", font=SMALL_FONT)
		
		label1.grid(row=0, column=1, sticky='w')
		label.grid(row=1, column=0, sticky='w')
		label2.grid(row=2, column=0, sticky='w')
		label3.grid(row=3, column=0, sticky='w')
		label4.grid(row=4, column=0, sticky='w')
		label5.grid(row=5, column=0, sticky='w')

		self.c_name=tk.Text(self, height=2,width=30)
		self.c_ID=Text(self, height=2, width=30)
		self.c_phno=tk.Text(self, height=2, width=30)
		self.c_eid=tk.Text(self, height=2,width=30)
		self.c_addr=tk.Text(self, height=2, width=30)

		self.c_ID.grid(row=1, column=2, padx=10, pady=10)
		self.c_name.grid(row=2,column=2,padx=10,pady=10)
		self.c_phno.grid(row=3,column=2,padx=10,pady=10)
		self.c_eid.grid(row=4,column=2,padx=10,pady=10)
		self.c_addr.grid(row=5,column=2,padx=10,pady=10)

		button1=tk.Button(self, text="CANCEL", command=lambda: controller.show_frame(Employee_login))
		button1.grid(row=7, column=1, sticky='w')
		button2=tk.Button(self, text="NEXT", command=self.enter)
		button2.grid(row=7, column=2, sticky='w')

	def enter(self):
		
		self.cID=self.c_ID.get("1.0","end-1c")	
		self.cname=self.c_name.get("1.0","end-1c")
		self.cphno=self.c_phno.get("1.0","end-1c")
		self.ceid=self.c_eid.get("1.0","end-1c")
		self.caddr=self.c_addr.get("1.0","end-1c")

		self.c_ID.delete("1.0","end")
		self.c_name.delete("1.0","end")
		self.c_phno.delete("1.0","end")
		self.c_eid.delete("1.0","end")
		self.c_addr.delete("1.0","end")
		
		adding_customer(self.cID, self.cname, self.cphno, self.ceid, self.caddr)
		self.controller.show_frame(VehicleType)
	


	

class VehicleType(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller
		


		label=tk.Label(self, text="VEHICLE TYPE", font=LARGE_FONT)

		button1=tk.Button(self, text="CAR", command=lambda: controller.show_frame(CAR), height=5, width=15)
		button2=tk.Button(self, text="BIKE", command=lambda: controller.show_frame(BIKE), height=5, width=15)
		button3=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(Customer_details))

		label.grid(row=0, column=2, sticky='w')
		button1.grid(row=1, column=0, sticky='e')
		button2.grid(row=1, column=3, sticky='e')
		button3.grid(row=2, column=0, sticky='w')

		# Insert two tables showing prices for each vehicle type and each vehicle

class CAR(tk.Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.choice="CAR"
		self.CID=Label(self, text="ENTER CURRENT CUSTOMER ID:", font=SMALL_FONT)
		self.current_id=Text(self, height=2, width=30)
		self.label=tk.Label(self, text="CAR DETAILS", font=LARGE_FONT)
		self.label.grid(row=0,column=1,sticky='w')
		self.CID.grid(row=1, column=0, sticky='w')
		self.current_id.grid(row=1, column=1, sticky='w')

		self.DatePicked=datetime.date(1984, 6, 24)
		#adding radio buttons for choosing car
		self.cars=[ ("SWIFT", 1), ("POLO", 2), ("XUV",3), ("FORTUNER", 4)]
		self.label1=tk.Label(self, text="Choose Car: ", font=SMALL_FONT)
		self.label1.grid(row=2,column=0, sticky=W)

		
		self.var=StringVar()
		self.CarChoice=None
		c_val=1
		
		for self.u, car in enumerate(self.cars):
			tk.Radiobutton(self, text=car, padx=20,variable=self.var, value=self.u, command=self.asign).grid(row=2, column=c_val, sticky='w')
			c_val=c_val+1
	



		#Adding calender to select date
		ttk.Label(self, text="Date: ", font=SMALL_FONT).grid(row=3, column=0,sticky='w')
		ttk.Button(self, text='Calendar', command=lambda: self.opencal("Calendar")).grid(row=3,column=2, sticky='w')

		#adding dropdown box for plan selection
		self.label2=ttk.Label(self, text="Choose plan", font=SMALL_FONT)
		self.label2.grid(row=4,column=0,sticky='w')

		options=["1 Day","5 Days", "10 Days","15 Days", "30 Days"] 	

		self.variable=StringVar(self)
		self.variable.set(options[0])

		self.w=OptionMenu(self,self.variable, *options)
		self.w.grid(row=4,column=2,sticky='w')

		#Adding the back and next button
		self.button1=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(VehicleType))
		self.button2=ttk.Button(self, text="NEXT", command=self.adding) 

		self.button1.grid(row=5, column=0, sticky='w')
		self.button2.grid(row=5, column=1, sticky='w')

	def adding(self):
		self.C_ID=self.CID     #remove the LHS. not needed
		print(self.DatePicked)
		self.days=self.variable.get()  # This stores the duration for which the vehicle is rented
		if self.days=="1 Day":
			self.days="one_day"
		elif self.days=="5 Days":
			self.days="five_days"
		elif self.days=="10 Days":
			self.days="ten_days"
		elif self.days=="15 Days":
			self.days="fifteen_days"
		elif self.days=="30 Days":
			self.days="thirty_days"

		
		print(self.CarChoice)

	def print_sel(self):
		self.DatePicked=(self.cal.selection_get()).strftime('%m/%d/%Y')
		self.popup.destroy()

	def opencal(self,msg):
		self.popup=tk.Toplevel()
		
		self.msg=self.popup.wm_title("calender")
		self.la=ttk.Label(self.popup, text=msg, font=LARGE_FONT)
		self.la.grid(row=0,column=0, sticky='w')
		self.cal=Calendar(self.popup, font="Arial 14", selectmode='day',
						cursor='hand1', year=2018, month=2, day=5)
		self.bu=ttk.Button(self.popup, text="OK", command=self.print_sel)

		self.cal.grid(row=1,column=0, sticky='w')
		self.bu.grid(row=2, column=0, sticky='w')

		self.popup.mainloop()


		
	def asign(self):
		self.CarChoice=self.var.get()


	
	
	

class Car1(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		list_of_prices=Label(self, text="PRICE OF CARS", font=LARGE_FONT)
		list_of_prices.grid(row=0, column=1, sticky='w')

		# Use this frame to display the prices of each car in a treeview



class BIKE(tk.Frame):

	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		choice="BIKE"

		label=tk.Label(self, text="BIKE DETAILS", font=LARGE_FONT)
		label.grid(row=0,column=1,sticky='w')

		bikes=[ ("SWIFT", 1), ("POLO", 2), ("XUV",3), ("FORTUNER", 4)]
		label1=tk.Label(self, text="Choose Bike: ", font=SMALL_FONT)
		label1.grid(row=1,column=0, sticky=W)

		var=IntVar()
		c_val=1
		for val, bike in enumerate(bikes):
			tk.Radiobutton(self, text=bike, padx=20,variable=var, value=val).grid(row=1, column=c_val, sticky='w')
			c_val=c_val+1

		def opencal(msg):
			popup=tk.Toplevel()

			def print_sel():
				print(cal.selection_get())
				popup.destroy()
			popup.wm_title("calender")
			la=ttk.Label(popup, text=msg, font=LARGE_FONT)
			la.grid(row=0,column=0, sticky='w')

			cal=Calendar(popup, font="Arial 14", selectmode='day',
						cursor='hand1', year=2018, month=2, day=5)
			bu=ttk.Button(popup, text="OK", command=print_sel)

			cal.grid(row=1,column=0, sticky='w')
			bu.grid(row=2, column=0, sticky='w')
			popup.mainloop()

		#Adding calender to select date
		ttk.Label(self, text="Date: ", font=SMALL_FONT).grid(row=2, column=0,sticky='w')
		ttk.Button(self, text='Calendar', command=lambda: opencal("Calendar")).grid(row=2,column=2, sticky='w')

		#addting dropdown box for plan selection
		label2=ttk.Label(self, text="Choose plan", font=SMALL_FONT)
		label2.grid(row=3,column=0,sticky='w')

		options=["5 Days", "10 Days", "20 Days"] #write code to get from database?

		variable=StringVar(self)
		variable.set(options[0])

		w=OptionMenu(self,variable, *options)
		w.grid(row=3,column=2,sticky='w')

		#Adding the back and next button

		button1=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(VehicleType))
		button2=ttk.Button(self, text="NEXT", command=lambda: controller.show_frame(confirm)) #add function to insert values into the table before going to next page

		button1.grid(row=4, column=0, sticky='w')
		button2.grid(row=4, column=1, sticky='w')

		


app=TSE()
app.mainloop()