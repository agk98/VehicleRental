import tkinter as tk
import datetime
from tkinter.ttk import *
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from backend import *
from fullscreen import *


LARGE_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 9)

class TSE(Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container=Frame(self)				

		container.grid()

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}							

		for F in (Home, Admin_Login, Second_page, Adding_emp, removing_emp, Employee_login, Customer_details, VehicleType, CAR, BIKE, BILL): 

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

		label1.grid(row=0, column=1, sticky='w', padx=10, pady=10)
		admin_log.grid(row=1, column=0, sticky='w', padx=20, pady=20)
		emp_log.grid(row=2, column=0, sticky='w', padx=20, pady=20)




class Admin_Login(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.password="irule"

		self.label1=Label(self, text="ADMIN LOGIN", font=LARGE_FONT)
		self.label2=Label(self, text="Admin Password", font=SMALL_FONT)
		self.entered_pass=Entry(self, width=30, show="*")
		self.login=Button(self, text="LOGIN", command=self.checking)
		self.back=Button(self, text="BACK", command=lambda: controller.show_frame(Home))

		self.label1.grid(row=0, column=1, sticky='w',padx=10, pady=10)
		self.label2.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		self.entered_pass.grid(row=1, column=1, sticky='w', ipady=3, padx=20, pady=20)
		self.back.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		self.login.grid(row=2, column=1, sticky='w',padx=20, pady=20)
	def checking(self):
		
		if self.entered_pass.get()==self.password:
			self.entered_pass.delete(0,"end")
			self.controller.show_frame(Second_page)
		else:
			app.destroy()

class Second_page(Frame):															
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller

		employee=get_employee()

		
		label=Label(self, text="ADMIN OPERATIONS", font=LARGE_FONT)
		add_employee=Button(self, text="ADD EMPLOYEE", command=lambda: self.controller.show_frame(Adding_emp))
		del_employee=Button(self, text="REMOVE EMPLOYEE", command=lambda: self.controller.show_frame(removing_emp))
		self.bill=Button(self, text="TRANSACTION RECORDS", command=lambda: controller.show_frame(BILL))
		self.logout=Button(self, text="LOGOUT", command= lambda:controller.show_frame(Home))

		label.grid(row=0, column=1, sticky='w',padx=20, pady=20)
		add_employee.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		del_employee.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		self.bill.grid(row=3, column=0, sticky='w',padx=20, pady=20)
		self.logout.grid(row=4, column=0, sticky='w',padx=20, pady=20)


class Adding_emp(Frame):
	

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.Top=Label(self, text="ENTER EMPLOYEE DETAILS", font=LARGE_FONT)
		self.Id=Label(self, text="Employee ID:", font=SMALL_FONT)
		self.name=Label(self, text="Name:", font=SMALL_FONT)
		self.date_of_birth=Label(self, text="AGE:", font=SMALL_FONT)
		self.email_id=Label(self, text="Email ID:", font=SMALL_FONT)
		self.password=Label(self, text="Password:", font=SMALL_FONT)

		self.EID=Text(self, height=2, width=30)
		self.ename=Text(self, height=2, width=30)
		self.edob=Text(self, height=2, width=30)
		self.eemail_id=Text(self, height=2, width=30)
		self.Password=Text(self, height=2, width=30)

		self.Top.grid(row=0, column=1, sticky='w',padx=20, pady=20)
		self.Id.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		self.EID.grid(row=1, column=1, sticky='w',padx=20, pady=20)
		self.name.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		self.ename.grid(row=2, column=1, sticky='w',padx=20, pady=20)
		self.date_of_birth.grid(row=3, column=0, sticky='w',padx=20, pady=20)
		self.edob.grid(row=3, column=1, sticky='w',padx=20, pady=20)
		self.email_id.grid(row=4, column=0, sticky='w',padx=20, pady=20)
		self.eemail_id.grid(row=4, column=1, sticky='w',padx=20, pady=20)
		self.password.grid(row=5, column=0, sticky='w',padx=20, pady=20)
		self.Password.grid(row=5, column=1, sticky='w',padx=20, pady=20)


		logout=Button(self, text="LOGOUT", command=lambda: controller.show_frame(Home))
		Add=Button(self, text="ADD", command=self.add)
		back=Button(self, text="BACK", command=lambda: controller.show_frame(Second_page))


		logout.grid(row=7, column=1, sticky='w',padx=20, pady=20)
		Add.grid(row=6, column=1, sticky='w',padx=20, pady=20)
		back.grid(row=6, column=0, sticky='w',padx=20, pady=20)

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

		self.controller.show_frame(Second_page)


class removing_emp(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller

		self.header=Label(self, text="REMOVE EMPLOYEE", font=LARGE_FONT)
		self.label=Label(self, text="Enter Employee ID:", font=SMALL_FONT)
		self.textbox=Text(self, height=2, width=30)
		self.remove=Button(self, text="REMOVE", command=self.rem)

		self.header.grid(row=0, column=1, sticky='w',padx=20, pady=20)
		self.label.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		self.textbox.grid(row=1, column=1, sticky='w',padx=20, pady=20)
		self.remove.grid(row=2, column=2, sticky='w',padx=20, pady=20)

		# self.tree=Treeview(self)

		# self.tree["columns"]=("#1", "#2","#3","#4","#5")
		# self.tree.heading("#1",text="emp_id")
		# self.tree.heading("#2",text="emp_name")
		# self.tree.heading("#3",text="emp_eid")
		# self.tree.heading("#4",text="emp_pass")
		# self.tree.heading("#5",text="emp_age")

		# self.tree.column("#1", stretch=YES)
		# self.tree.column("#2", stretch=YES)
		# self.tree.column("#3", stretch=YES)
		# self.tree.column("#4", stretch=YES)
		# self.tree.column("#5", stretch=YES)

		# self.tree.grid(row=3, column=0, padx=10, pady=10, columnspan=4, sticky='nsew')
		# self.tree['show']='headings'

		# self.employee=get_employee()

		# for i in self.employee:
		# 	self.tree.insert("",'end', values=i)


	def rem(self):

		self.rem_emp=self.textbox.get("1.0","end-1c")
		self.textbox.delete("1.0","end")
		removing_employee(self.rem_emp)
		
		self.controller.show_frame(Second_page)



class Employee_login(Frame):
	def hello(self):
		self.e_id=self.emp_id.get("1.0","end-1c")
		self.pas=self.password.get()

		self.emp_id.delete("1.0","end")
		self.password.delete(0,"end")
			
		auth=retrieve_login(self.e_id, self.pas)
		
		if auth == 1:
			self.controller.show_frame(Customer_details)
		elif auth == 0:
			self.controller.show_frame(Employee_login)


	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		self.label1=tk.Label(self, text="EMPLOYEE LOGIN", font=LARGE_FONT)	
		self.label1.grid(row=0, column=1,sticky='W',padx=20, pady=20)

		self.label2=tk.Label(self,text="Employee ID", font=LARGE_FONT)
		self.label2.grid(row=1,column=0,sticky='w',padx=20, pady=20)
		self.label3=tk.Label(self,text="Password", font=LARGE_FONT)
		self.label3.grid(row=2,column=0,sticky='w',padx=20, pady=20)


		self.emp_id=tk.Text(self, height=2,width=30)
		self.password=tk.Entry(self, width=30, show="*")

		self.emp_id.grid(row=1,column=2,padx=20, pady=20)
		self.password.grid(row=2,column=2, ipady=3,padx=20, pady=20)

		self.button1=tk.Button(self, text="LOGIN", command=self.hello)
		self.button1.grid(row=4, column=1, sticky='W',padx=20, pady=20)
		self.button2=Button(self, text="BACK", command=lambda:controller.show_frame(Home))
		self.button2.grid(row=4, column=0, sticky='w',padx=20, pady=20)

	

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
		
		label1.grid(row=0, column=1, sticky='w',padx=20, pady=20)
		label.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		label2.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		label3.grid(row=3, column=0, sticky='w',padx=20, pady=20)
		label4.grid(row=4, column=0, sticky='w',padx=20, pady=20)
		label5.grid(row=5, column=0, sticky='w',padx=20, pady=20)

		self.c_name=tk.Text(self, height=2,width=30)
		self.c_ID=Text(self, height=2, width=30)
		self.c_phno=tk.Text(self, height=2, width=30)
		self.c_eid=tk.Text(self, height=2,width=30)
		self.c_addr=tk.Text(self, height=2, width=30)

		self.c_ID.grid(row=1, column=2,padx=20, pady=20)
		self.c_name.grid(row=2,column=2,padx=20, pady=20)
		self.c_phno.grid(row=3,column=2,padx=20, pady=20)
		self.c_eid.grid(row=4,column=2,padx=20, pady=20)
		self.c_addr.grid(row=5,column=2,padx=20, pady=20)

		button1=tk.Button(self, text="CANCEL", command=lambda: controller.show_frame(Home))
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
		


		label=tk.Label(self, text="CHOOSE VEHICLE TYPE", font=LARGE_FONT)

		button1=tk.Button(self, text="CAR", command=lambda: controller.show_frame(CAR), height=3, width=8)
		button2=tk.Button(self, text="BIKE", command=lambda: controller.show_frame(BIKE), height=3, width=8)
		button3=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(Customer_details))

		label.grid(row=0, column=1, sticky='w',padx=20, pady=20)
		button1.grid(row=3, column=0, sticky='e',padx=20, pady=20)
		button2.grid(row=3, column=1, sticky='e',padx=20, pady=20)
		button3.grid(row=4, column=1, sticky='w',padx=20, pady=20)

		# tree view for car

		car_tree=Treeview(self)

		car_tree["columns"]=("#1", "#2","#3","#4","#5", "#6", "#7")
		car_tree.heading("#1",text="CAR MAKE")
		car_tree.heading("#2",text="CAR MODEL")
		car_tree.heading("#3",text="1 Day")
		car_tree.heading("#4",text="5 Days")
		car_tree.heading("#5",text="10 Days")
		car_tree.heading("#6",text="15 Days")
		car_tree.heading("#7",text="30 Days")

		car_tree.column("#1")
		car_tree.column("#2")
		car_tree.column("#3")
		car_tree.column("#4")
		car_tree.column("#5")
		car_tree.column("#6")
		car_tree.column("#7")

		car_tree.grid(row=1, column=0, padx=10, pady=10, columnspan=4, sticky='nsew')
		car_tree['show']='headings'

		headings=get_car_prices()

		for i in headings:
			car_tree.insert("",'end', values=i)


		# tree view for bikes
		bike_tree=Treeview(self)

		bike_tree["columns"]=("#1", "#2","#3","#4","#5")
		bike_tree.heading("#1",text="BIKE MAKE")
		bike_tree.heading("#2",text="BIKE MODEL")
		bike_tree.heading("#3",text="1 Day")
		bike_tree.heading("#4",text="5 Days")
		bike_tree.heading("#5",text="10 Days")

		bike_tree.column("#1", stretch=YES)
		bike_tree.column("#2", stretch=YES)
		bike_tree.column("#3", stretch=YES)
		bike_tree.column("#4", stretch=YES)
		bike_tree.column("#5", stretch=YES)

		bike_tree.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky='nsew')
		bike_tree['show']='headings'

		headingss=get_bike_prices()

		for i in headingss:
			bike_tree.insert("",'end', values=i)

class CAR(tk.Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.label=tk.Label(self, text="CAR DETAILS", font=LARGE_FONT)
		self.CID=Label(self, text="ENTER CURRENT CUSTOMER ID:", font=SMALL_FONT)
		self.transID=Label(self, text="ENTER TRANSACTION ID:", font=SMALL_FONT)
		self.current_id=Text(self, height=2, width=30)
		self.current_trans=Text(self, height=2, width=30)
		

		self.label.grid(row=0,column=1,sticky='w',padx=20, pady=20)
		self.CID.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		self.current_id.grid(row=1, column=1, sticky='w',padx=20, pady=20)
		self.transID.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		self.current_trans.grid(row=2, column=1, sticky='w',padx=20, pady=20)

		self.DatePicked=datetime.date(1984, 6, 24)
		#adding radio buttons for choosing car
		self.cars=[("Swift",0), ("Polo",1), ("XUV",2), ("Fortuner",3)]
		self.label1=tk.Label(self, text="Choose Car: ", font=SMALL_FONT)
		self.label1.grid(row=3,column=0, sticky=W,padx=20, pady=20)

		
		self.var=StringVar()
		self.r1=Radiobutton(self, text="SWIFT", variable=self.var, value="Swift", command=self.asign).grid(row=3, column=1, sticky='w',padx=20, pady=20)
		self.r2=Radiobutton(self, text="POLO", variable=self.var, value="Polo", command=self.asign).grid(row=4, column=1, sticky='w',padx=20, pady=20)
		self.r3=Radiobutton(self, text="XUV", variable=self.var, value="XUV", command=self.asign).grid(row=5, column=1, sticky='w',padx=20, pady=20)
		self.r4=Radiobutton(self, text="FORTUNER", variable=self.var, value="Fortuner", command=self.asign).grid(row=6, column=1, sticky='w',padx=20, pady=20)

		
		#Adding calender to select date
		ttk.Label(self, text="Date: ", font=SMALL_FONT).grid(row=7, column=0,sticky='w',padx=20, pady=20)
		ttk.Button(self, text='Calendar', command=lambda: self.opencal("Calendar")).grid(row=7,column=1, sticky='w',padx=20, pady=20)

		#adding dropdown box for plan selection
		self.label2=ttk.Label(self, text="Choose plan", font=SMALL_FONT)
		self.label2.grid(row=8,column=0,sticky='w',padx=20, pady=20)

		options=["1 Day","5 Days", "10 Days","15 Days", "30 Days"] 	

		self.variable=StringVar(self)
		self.variable.set(options[0])

		self.w=OptionMenu(self,self.variable, *options)
		self.w.grid(row=8,column=1,sticky='w',padx=20, pady=20)

		#Adding the back and next button
		self.button1=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(VehicleType))
		self.button2=ttk.Button(self, text="NEXT", command=self.adding) 


		self.button1.grid(row=9, column=0, sticky='w',padx=20, pady=20)
		self.button2.grid(row=9, column=1, sticky='w',padx=20, pady=20)


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

	def adding(self):
		self.CID=self.current_id.get("1.0","end-1c")
		self.tid=self.current_trans.get("1.0","end-1c")

		self.days=self.variable.get()  # This stores the duration for which the vehicle is rented
		if self.days=="1 Day":
			self.day="one_day"
		elif self.days=="5 Days":
			self.day="five_days"
		elif self.days=="10 Days":
			self.day="ten_days"
		elif self.days=="15 Days":
			self.day="fifteen_days"
		elif self.days=="30 Days":
			self.day="thirty_days"
		self.car_price=calculating_car_price(self.day, self.CarChoice, 0)
		self.bike_model="-"
		self.customer_name=get_customer_name(self.CID,"")	
		inserting_trsaction(self.CID, self.customer_name, self.tid, self.CarChoice, self.bike_model, self.DatePicked, self.days, self.car_price)


class BIKE(tk.Frame):

	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller
		self.label=tk.Label(self, text="BIKE DETAILS", font=LARGE_FONT)
		self.CID=Label(self, text="ENTER CURRENT CUSTOMER ID:", font=SMALL_FONT)
		self.transID=Label(self, text="ENTER TRANSACTION ID:", font=SMALL_FONT)
		self.current_id=Text(self, height=2, width=30)
		self.current_trans=Text(self, height=2, width=30)


		self.label.grid(row=0,column=1,sticky='w',padx=20, pady=20)
		self.CID.grid(row=1, column=0, sticky='w',padx=20, pady=20)
		self.current_id.grid(row=1, column=1, sticky='w',padx=20, pady=20)
		self.transID.grid(row=2, column=0, sticky='w',padx=20, pady=20)
		self.current_trans.grid(row=2, column=1, sticky='w',padx=20, pady=20)


		self.DatePicked=datetime.date(1984, 6, 24)
		#adding radio buttons for choosing car
		self.bikes=[("Pulsar",0), ("Splendor",1), ("X-Blade",2), ("FZ-S",3)]
		self.label1=tk.Label(self, text="Choose Bike: ", font=SMALL_FONT)
		self.label1.grid(row=3,column=0, sticky=W,padx=20, pady=20)

		
		self.var=StringVar()
		self.r1=Radiobutton(self, text="PULSAR", variable=self.var, value="Pulsar", command=self.asign).grid(row=3, column=1, sticky='w',padx=20, pady=20)
		self.r2=Radiobutton(self, text="SPLENDOR", variable=self.var, value="Splendor", command=self.asign).grid(row=4, column=1, sticky='w',padx=20, pady=20)
		self.r3=Radiobutton(self, text="X-BLADE", variable=self.var, value="X-Blade", command=self.asign).grid(row=5, column=1, sticky='w',padx=20, pady=20)
		self.r4=Radiobutton(self, text="FZ-S", variable=self.var, value="FZ-S", command=self.asign).grid(row=6, column=1, sticky='w',padx=20, pady=20)

		
		#Adding calender to select date
		ttk.Label(self, text="Date: ", font=SMALL_FONT).grid(row=7, column=0,sticky='w',padx=20, pady=20)
		ttk.Button(self, text='Calendar', command=lambda: self.opencal("Calendar")).grid(row=7,column=1, sticky='w',padx=20, pady=20)

		#adding dropdown box for plan selection
		self.label2=ttk.Label(self, text="Choose plan", font=SMALL_FONT)
		self.label2.grid(row=8,column=0,sticky='w',padx=20, pady=20)

		options=["1 Day","5 Days", "10 Days"] 	

		self.variable=StringVar(self)
		self.variable.set(options[0])

		self.w=OptionMenu(self,self.variable, *options)
		self.w.grid(row=8,column=1,sticky='w',padx=20, pady=20)

		#Adding the back and next button
		self.button1=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(VehicleType))
		self.button2=ttk.Button(self, text="NEXT", command=self.adding) 

		self.button1.grid(row=9, column=0, sticky='w',padx=20, pady=20)
		self.button2.grid(row=9, column=1, sticky='w',padx=20, pady=20)

	def adding(self):

		self.CID=self.current_id.get("1.0","end-1c")
		self.tid=self.current_trans.get("1.0","end-1c")

		self.days=self.variable.get()  # This stores the duration for which the vehicle is rented
		if self.days=="1 Day":
			self.day="one_day"
		elif self.days=="5 Days":
			self.day="five_days"
		elif self.days=="10 Days":
			self.day="ten_days"
		self.bike_price=calculating_bike_price(self.day, self.BikeChoice, 0)
		self.CarChoice="-"
		self.customer_name=get_customer_name(self.CID,"")	
		inserting_trsaction(self.CID, self.customer_name, self.tid, self.CarChoice, self.BikeChoice, self.DatePicked, self.days, self.bike_price)

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
		self.BikeChoice=self.var.get()
		
class BILL(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller= controller

		bike_tree=Treeview(self)

		bike_tree["columns"]=("#1", "#2","#3","#4","#5")
		bike_tree.heading("#1",text="Customer ID")
		bike_tree.heading("#2",text="Customer name")
		bike_tree.heading("#3",text="car_model")
		bike_tree.heading("#4",text="bike_model")
		bike_tree.heading("#5",text="amount")


		bike_tree.column("#1", stretch=YES)
		bike_tree.column("#2", stretch=YES)
		bike_tree.column("#3", stretch=YES)
		bike_tree.column("#4", stretch=YES)
		bike_tree.column("#5", stretch=YES)

		bike_tree.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky='nsew')
		bike_tree['show']='headings'

		headingss=get_bill()

		for i in headingss:
			bike_tree.insert("",'end', values=i)

		self.back=Button(self, text="BACK", command=lambda:controller.show_frame(Second_page))
		self.back.grid(row=3, column=0, sticky='w',padx=20, pady=20)

	


app=TSE()
root=FullScreenApp(app)
app.mainloop()