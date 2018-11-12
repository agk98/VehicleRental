import tkinter as tk
import datetime
from tkinter.ttk import *
from tkinter import *
from tkcalendar import Calendar
from datetime import date 
from app import *


LARGE_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 9)

class TSE(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container=ttk.Frame(self)				

		container.grid()

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}							

		for F in (Admin_Login, Admin,Employee_login,Customer_details, VehicleType, CAR, BIKE): 

			frame=F(container, self)		

			self.frames[F]=frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(Admin_Login)			

	def show_frame(self, cont):
		frame=self.frames[cont]
		frame.tkraise()	


class Admin_Login(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller=controller
		self.password="irule"

		label1=Label(self, text="ADMIN LOGIN", font=LARGE_FONT)
		label2=Label(self, text="Admin Password", font=SMALL_FONT)
		self.entered_pass=Text(self, height=2, width=30)
		login=Button(self, text="LOGIN", command=self.checking)

		label1.grid(row=0, column=1, sticky='w')
		label2.grid(row=1, column=0, sticky='w')
		self.entered_pass.grid(row=1, column=1, sticky='w')
		login.grid(row=2, column=0, sticky='w')
	def checking(self):
		if self.entered_pass.get("1.0","end-1c")==self.password:
			self.controller.show_frame(Admin)
		else:
			app.destroy()

class Admin(Frame):
	

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

		Add=Button(self, text="ADD", command=self.add)
		Add.grid(row=6, column=0, sticky='w')

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
			# insert code to insert values into customer table

		add_employee(self.emp_id, self.emp_name, self.emp_dob, self.emp_emailID, self.emp_password)

		controller.show_frame(Admin_Login)







class Employee_login(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		def hello():
			self.e_id=self.emp_id.get("1.0","end-1c")
			self.pas=self.password.get("1.0","end-1c")

			self.emp_id.delete("1.0","end")
			self.password.delete("1.0","end")
			#enter code to check whether entered details are correct

			controller.show_frame(Customer_details)


		label1=tk.Label(self, text="EMPLOYEE LOGIN", font=LARGE_FONT)	
		label1.grid(row=0, column=1,sticky='W')

		label2=tk.Label(self,text="Employee ID", font=LARGE_FONT)
		label2.grid(row=1,column=0,sticky='w')
		label3=tk.Label(self,text="Password", font=LARGE_FONT)
		label3.grid(row=2,column=0,sticky='w')


		self.emp_id=tk.Text(self, height=2,width=30)
		self.password=tk.Text(self, height=2, width=30)

		self.emp_id.grid(row=1,column=2,padx=10,pady=10)
		self.password.grid(row=2,column=2,padx=10,pady=10)

		button1=tk.Button(self, text="LOGIN", command=hello)
		button1.grid(row=4, column=0, sticky='W')

class Customer_details(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller  = controller

		label1=tk.Label(self, text="CUSTOMER DETAILS", font=LARGE_FONT)
		label2=tk.Label(self, text="Name", font=SMALL_FONT)
		label3=tk.Label(self, text="Phone Number", font=SMALL_FONT)
		label4=tk.Label(self, text="Email ID", font=SMALL_FONT)
		label5=tk.Label(self, text="Address", font=SMALL_FONT)
		
		label1.grid(row=0, column=1, sticky='w')
		label2.grid(row=1, column=0, sticky='w')
		label3.grid(row=2, column=0, sticky='w')
		label4.grid(row=3, column=0, sticky='w')
		label5.grid(row=4, column=0, sticky='w')

		self.c_name=tk.Text(self, height=2,width=30)
		self.c_phno=tk.Text(self, height=2, width=30)
		self.c_eid=tk.Text(self, height=2,width=30)
		self.c_addr=tk.Text(self, height=2, width=30)

		self.c_name.grid(row=1,column=2,padx=10,pady=10)
		self.c_phno.grid(row=2,column=2,padx=10,pady=10)
		self.c_eid.grid(row=3,column=2,padx=10,pady=10)
		self.c_addr.grid(row=4,column=2,padx=10,pady=10)

		button1=tk.Button(self, text="CANCEL", command=lambda: controller.show_frame(Employee_login))
		button1.grid(row=5, column=1, sticky='w')
		button2=tk.Button(self, text="NEXT", command=self.enter)
		button2.grid(row=5, column=2, sticky='w')

	def enter(self):
		
			
		self.cname=self.c_name.get("1.0","end-1c")
		self.cphno=self.c_phno.get("1.0","end-1c")
		self.ceid=self.c_eid.get("1.0","end-1c")
		self.caddr=self.c_addr.get("1.0","end-1c")

		self.c_name.delete("1.0","end")
		self.c_phno.delete("1.0","end")
		self.c_eid.delete("1.0","end")
		self.c_addr.delete("1.0","end")
			# insert code to insert values into customer table

		add_customer(self.cname,self.cphno,self.ceid,self.caddr)

		controller.show_frame(VehicleType)
	


	

class VehicleType(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		label=tk.Label(self, text="VEHICLE TYPE", font=LARGE_FONT)

		button1=tk.Button(self, text="CAR", command=lambda: controller.show_frame(CAR), height=5, width=15)
		button2=tk.Button(self, text="Bike", command=lambda: controller.show_frame(BIKE), height=5, width=15)
		button3=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(Customer_details))

		label.grid(row=0, column=2, sticky='w')
		button1.grid(row=1, column=0, sticky='e')
		button2.grid(row=1, column=3, sticky='e')
		button3.grid(row=2, column=0, sticky='w') 

class CAR(tk.Frame):

	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		choice="CAR"

		label=tk.Label(self, text="CAR DETAILS", font=LARGE_FONT)
		label.grid(row=0,column=1,sticky='w')

		DatePicked=datetime.date(1984, 6, 24)
		#adding radio buttons for choosing car
		cars=[ ("SWIFT", 1), ("POLO", 2), ("XUV",3), ("FORTUNER", 4)]
		label1=tk.Label(self, text="Choose Car: ", font=SMALL_FONT)
		label1.grid(row=1,column=0, sticky=W)

		
		var=IntVar()
		def asign():
			CarChoice=var.get()
		c_val=1
		self.CarChoice=None
		for val, car in enumerate(cars):
			tk.Radiobutton(self, text=car, padx=20,variable=var, command=asign, value=val).grid(row=1, column=c_val, sticky='w')
			c_val=c_val+1
		
		def asign():
			self.CarChoice=var.get()
		def opencal(msg):
			popup=tk.Toplevel()
			def print_sel():
				DatePicked=(cal.selection_get()).strftime('%m/%d/%Y')
				popup.destroy()
			popup.wm_title("calender")
			la=ttk.Label(popup, text=msg, font=LARGE_FONT)
			la.grid(row=0,column=0, sticky='w')

			self.cal=Calendar(popup, font="Arial 14", selectmode='day',
						cursor='hand1', year=2018, month=2, day=5)
			bu=ttk.Button(popup, text="OK", command=print_sel)

			print(self.cal)

			self.cal.grid(row=1,column=0, sticky='w')
			bu.grid(row=2, column=0, sticky='w')

			popup.mainloop()

		#Adding calender to select date
		ttk.Label(self, text="Date: ", font=SMALL_FONT).grid(row=2, column=0,sticky='w')
		ttk.Button(self, text='Calendar', command=lambda: opencal("Calendar")).grid(row=2,column=2, sticky='w')

		#adding dropdown box for plan selection
		label2=ttk.Label(self, text="Choose plan", font=SMALL_FONT)
		label2.grid(row=3,column=0,sticky='w')

		options=["5 Days", "10 Days", "20 Days"] 	#write code to get from database?

		variable=StringVar(self)
		variable.set(options[0])

		w=OptionMenu(self,variable, *options)
		w.grid(row=3,column=2,sticky='w')

		#Adding the back and next button
		def adding():
			print(DatePicked)
			days=variable.get()
			print(days)
			print(self.CarChoice)


		button1=ttk.Button(self, text="BACK", command=lambda: controller.show_frame(VehicleType))
		button2=ttk.Button(self, text="NEXT", command=adding) #add function to insert values into the table before going to next page

		button1.grid(row=4, column=0, sticky='w')
		button2.grid(row=4, column=1, sticky='w')

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