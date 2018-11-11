import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
LARGE_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 9)

class TSE(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container=ttk.Frame(self)				#

		container.grid()

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}							

		for F in (Employee_login,Customer_details, VehicleType, CAR, BIKE): 

			frame=F(container, self)		

			self.frames[F]=frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(Employee_login)			

	def show_frame(self, cont):
		frame=self.frames[cont]
		frame.tkraise()	


class Employee_login(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
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

		button1=tk.Button(self, text="LOGIN", command=lambda: controller.show_frame(Customer_details))
		button1.grid(row=4, column=0, sticky='W')

class Customer_details(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		
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

		button1=tk.Button(self, text="BACK", command=lambda: controller.show_frame(Employee_login))
		button1.grid(row=5, column=1, sticky='w')
		button2=tk.Button(self, text="NEXT", command=lambda: controller.show_frame(VehicleType))
		button2.grid(row=5, column=2, sticky='w')

class VehicleType(tk.Frame):
	def choice1(s):
		self.choice=s
		self.show_frame(CAR)
	def choice2(s):
		self.choice=s
		self.show_frame(BIKE)
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
		label=tk.Label(self, text="CAR DETAILS", font=LARGE_FONT)
		label.grid(row=0,column=1,sticky='w')

		#adding radio buttons for choosing car
		cars=[ ("SWIFT", 1), ("POLO", 2), ("XUV",3), ("FORTUNER", 4)]
		label1=tk.Label(self, text="Choose Car: ", font=SMALL_FONT)
		label1.grid(row=1,column=0, sticky=W)

		var=IntVar()
		c_val=1
		for val, car in enumerate(cars):
			tk.Radiobutton(self, text=car, padx=20,variable=var, value=val).grid(row=1, column=c_val, sticky='w')
			c_val=c_val+1
		def opencal(msg):
			popup=tk.Toplevel()

			def print_sel():
				select1=cal.selection_get()
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

class BIKE(tk.Frame):

	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
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