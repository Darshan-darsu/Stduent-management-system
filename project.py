from tkinter import *
from tkinter import ttk
import mysql.connector

class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management")
		self.root.geometry("1380x800+0+0")
         #displaying head of system
		title=Label(self.root,text="Student Management System",bd=20,relief=GROOVE,font=("time new roman",40,"bold"),bg="Black",fg="White")
		title.pack(side=TOP,fill=X)#where to display
		# varibales 

		self.Roll_No_Var=StringVar()
		self.Name_Var=StringVar()
		self.Contact_Var=StringVar()
		self.Gender_Var=StringVar()
		self.Address_Var=StringVar()
		self.Email_Var=StringVar()
		self.DOB_Var=StringVar()

		
		# Left side table details
		manage_frame=Frame(self.root,bd=5,bg="crimson",relief=RIDGE)
		manage_frame.place(x=10,y=120,height=560,width=450)

		#inside left table
		m_title=Label(manage_frame,text="Manage students",bg="crimson",fg="white",font=("time new roman",25,"bold"))
		m_title.grid(row=0,columnspan=2,pady=10)

		#Roll no
		lb1_roll=Label(manage_frame,text="Roll_No ",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		#Roll_No text field
		txt_field=Entry(manage_frame,textvariable=self.Roll_No_Var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_field.grid(row=1,column=1,pady=10,padx=20,sticky="w")
		#Name
		lb1_Name=Label(manage_frame,text="Name ",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		#Name text field
		txt_field=Entry(manage_frame,textvariable=self.Name_Var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_field.grid(row=2,column=1,pady=10,padx=20,sticky="w")	
        #Email
		lb1_Email=Label(manage_frame,text="Email",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		#Name text field
		txt_field=Entry(manage_frame,textvariable=self.Email_Var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_field.grid(row=3,column=1,pady=10,padx=20,sticky="w")	


		
		#Gender
		lb1_Gender=Label(manage_frame,text="Gender ",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		#Gender text field
		combo_gender=ttk.Combobox(manage_frame,textvariable=self.Gender_Var,font=("time new roman",14,"bold"),state="readonly")
		combo_gender['values']=("Male","Female","Other")
		combo_gender.grid(row=4,column=1,pady=10,padx=20)
		

 		# Contact
		lb1_Contact=Label(manage_frame,text="Contact ",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		#Contact text field
		txt_field=Entry(manage_frame,textvariable=self.Contact_Var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_field.grid(row=5,column=1,pady=10,padx=20,sticky="w")	

		#D.O.B
		lb1_Contact=Label(manage_frame,text="D.O.B",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Contact.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		#D.O.B text field
		txt_field=Entry(manage_frame,textvariable=self.DOB_Var,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_field.grid(row=6,column=1,pady=10,padx=20,sticky="w")


		#Address
		lb1_Adress=Label(manage_frame,text="Address ",bg="crimson",fg="white",font=("time new roman",20,"bold"))
		lb1_Adress.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		#Address text field
		self.txt_Address=Text(manage_frame,width=29,height=3,font=("",10))
		self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


########## button #######
		button_Frame=Frame(manage_frame,bd=4,relief=GROOVE,bg="crimson")
		button_Frame.place(x=10,y=490,width=410)
		addbtn=Button(button_Frame,text="add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
		Updatebtn=Button(button_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
		Deletebtn=Button(button_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
		Clearbtn=Button(button_Frame,text="clear",width=10,command=self.clear).grid(row=0,column=4,padx=10,pady=10)





 ################  # Right side table details ############################     

		Details_frame=Frame(self.root,bd=5,bg="crimson",relief=RIDGE)
		Details_frame.place(x=500,y=120,height=560,width=850)
#########search thing ####
		lb1_Search=Label(Details_frame,text="Search by",bg='crimson',fg="white",font=("time new roman",25,"bold"))
		lb1_Search.grid(row=0,column=0,padx=20,pady=10,sticky="w")
####### tuple thing ##
		combo_search=ttk.Combobox(Details_frame,width=10,font=("time new roman",14,"bold"),state="readonly")
		combo_search['values']=("Name","Roll_No","Contact")
		combo_search.grid(row=0,column=1,pady=10,padx=20)

			#####search field ####
		txt_search=Entry(Details_frame,width=18,font=("time new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_search.grid(row=0,column=2,pady=10,sticky="w")

		Searchbtn=Button(Details_frame,text="Search",width=15).grid(row=0,column=3,padx=10,pady=10)
		Showallbtn=Button(Details_frame,text="Showall",width=15).grid(row=0,column=4,padx=10,pady=10)

		##table frame ############
		Table_frame=Frame(Details_frame,bd=4,bg="crimson",relief=RIDGE)
		Table_frame.place(x=10,y=70,height=470,width=810)

##scroll bar for details
		scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
		self.student_table=ttk.Treeview(Table_frame,columns=("Roll_No","Name","Email","Contact","Gender","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.student_table.xview)
		scroll_y.config(command=self.student_table.yview)

		self.student_table.heading("Roll_No",text="Roll_No")
		self.student_table.heading("Name",text="Name")
		self.student_table.heading("Email",text="Email")
		self.student_table.heading("Gender",text="Gender")

		self.student_table.heading("Contact",text="Contact")
		self.student_table.heading("D.O.B",text="D.O.B")
		self.student_table.heading("Address",text="Address")
		self.student_table["show"]='headings'
		self.student_table.column("Roll_No",width=100)
		self.student_table.column("Name",width=100)
		self.student_table.column("Email",width=100)
		self.student_table.column("Contact",width=150)
		self.student_table.column("Address",width=150)
		self.student_table.column("D.O.B",width=100)
		self.student_table.column("Gender",width=100)

		self.student_table.pack(fill=BOTH,expand=1)
		self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()
	
	def add_student(self):
		con=mysql.connector.connect(host="localhost",user="root",password="root@123",database="students")
		cur=con.cursor()
		cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_Var.get(),
			self.Name_Var.get(),
			self.Email_Var.get(),
			self.Contact_Var.get(),
			self.Gender_Var.get(),
			self.DOB_Var.get(),
			self.txt_Address.get('1.0',END)
			))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()


	###fetch data
	def fetch_data(self):
		con=mysql.connector.connect(host="localhost",user="root",password="root@123",database="students")
		cur=con.cursor()
		cur.execute("select * from student")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert("",END,values=row)
				con.commit()
		con.close()

##########clear #########
	def clear(self):
		self.Roll_No_Var.set(''),
		self.Name_Var.set(''),
		self.Email_Var.set(''),
		self.Contact_Var.set(''),
		self.Gender_Var.set(''),
		self.DOB_Var.set(""),
		self.txt_Address.delete('1.0',END)



	def get_cursor(self,ev):
		cursor_row=self.student_table.focus()
		contents=self.student_table.item(cursor_row)
		row=contents["values"]
		self.Roll_No_Var.set(row[0]),
		self.Name_Var.set(row[1]),
		self.Email_Var.set(row[2]),
		self.Contact_Var.set(row[3]),
		self.Gender_Var.set(row[4]),
		self.DOB_Var.set(row[5]),
		self.txt_Address.delete('1.0',END)
		self.txt_Address.insert(END,row[6])

	def update_data(self):
		con=mysql.connector.connect(host="localhost",user="root",password="root@123",database="students")
		cur=con.cursor()
		cur.execute("update into student set Name=%s,Email=%s,Contact=%s,Gender=%s,DOB=%s,Address=%s where Roll_No=%s",(self.Name_Var.get(),
			self.Email_Var.get(),
			self.Contact_Var.get(),
			self.Gender_Var.get(),
			self.DOB_Var.get(),
			self.txt_Address.get('1.0',END),
			self.Roll_No_Var.get()
			))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def delete_data(self):
		con=mysql.connector.connect(host="localhost",user="root",password="root@123",database="students")
		cur=con.cursor()
		cur.execute("delete from student where Roll_No=%s",self.Roll_No_Var.get())
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
		




		
		
		



root=Tk()
ob=Student(root)
root.mainloop()