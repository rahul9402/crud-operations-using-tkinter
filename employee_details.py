
from tkinter import *
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(host='127.0.0.1',user='root',password='rahul',db='employee')
cursor = db.cursor()

access = Tk()
access.geometry('700x600')
access.title('Employee Details')
access.configure(bg='blue')

def calculate():
    emp_annualsalary.set(emp_salary.get() * 12)

def add():
    id = emp_id.get()
    name = emp_name.get()
    mail = emp_mail.get()
    designation = emp_designation.get()
    salary = emp_salary.get()
    annualsalary = emp_annualsalary.get()
    cursor.execute('insert into empdetails values(%s,%s,%s,%s,%s,%s)',[id,name,mail,designation,salary,annualsalary])
    db.commit()
    tkinter.messagebox.showinfo('Employee Details','Employee Details Added')

def view():
    id = emp_id.get()
    cursor.execute('select * from empdetails where empid=%s',[id])
    data = cursor.fetchone()
    if data!=None:
        emp_name.set(data[1])
        emp_mail.set(data[2])
        emp_designation.set(data[3])
        emp_salary.set(data[4])
        emp_annualsalary.set(data[5])
    else:
        tkinter.messagebox.showwarning('Employee Details','No Data Found')

def update():
    id = emp_id.get()
    name = emp_name.get()
    mail = emp_mail.get()
    designation = emp_designation.get()
    salary = emp_salary.get()
    annualsalary = emp_annualsalary.get()
    cursor.execute('update empdetails set empname=%s,empmail=%s,empdesignation=%s,empsalary=%s,empannualsalary=%s '
                   'where empid=%s',[name, mail, designation, salary, annualsalary,id])
    db.commit()
    tkinter.messagebox.showinfo('Employee Details', 'Employee Details Updated')

def clear():
    emp_id.set('')
    emp_name.set('')
    emp_mail.set('')
    emp_designation.set('')
    emp_salary.set('')
    emp_annualsalary.set('')

def delete():
    id = emp_id.get()
    cursor.execute('delete from empdetails where empid=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Employee Details', 'Employee Details Deleted')

def overall():
    global viewpage
    viewpage = Toplevel(access)
    viewpage.geometry('1250x400')
    viewpage.title('Show Employee Details')
    viewpage.configure(bg='yellow')

    cursor.execute('select * from empdetails')
    data = cursor.fetchall()
    row = len(data)
    column = len(data[0])

    Label(viewpage,text='Emp Id',font=('calibri',13,'bold'),bg='yellow').grid(row=0,column=0)
    Label(viewpage, text='Emp Name', font=('calibri', 13, 'bold'), bg='yellow').grid(row=0, column=1)
    Label(viewpage, text='Emp Mail', font=('calibri', 13, 'bold'), bg='yellow').grid(row=0, column=2)
    Label(viewpage, text='Emp Designation', font=('calibri', 13, 'bold'), bg='yellow').grid(row=0, column=3)
    Label(viewpage, text='Emp Salary', font=('calibri', 13, 'bold'), bg='yellow').grid(row=0, column=4)
    Label(viewpage, text='Emp AnnualSalary', font=('calibri', 13, 'bold'), bg='yellow').grid(row=0, column=5)

    for i in range(row):
        for j in range(column):
            s = Entry(viewpage,font=('calibri',15))
            s.grid(row=i+1,column=j)
            s.insert(END,data[i][j])

    viewpage.mainloop()

Label(access,text='Employee Details',font=('calibri',20)).place(x=250,y=10)

emp_id_label = Label(access,text='Employee Id',font=('calibri',15),bg='blue',fg='lightblue')
emp_id_label.place(x=100,y=80)

emp_name_label = Label(access,text='Employee Name',font=('calibri',15),bg='blue',fg='lightblue')
emp_name_label.place(x=100,y=130)

emp_mail_label = Label(access,text='Employee Mail',font=('calibri',15),bg='blue',fg='lightblue')
emp_mail_label.place(x=100,y=180)

emp_designation_label = Label(access,text='Employee Designation',font=('calibri',15),bg='blue',fg='lightblue')
emp_designation_label.place(x=100,y=230)

emp_salary_label = Label(access,text='Employee Salary',font=('calibri',15),bg='blue',fg='lightblue')
emp_salary_label.place(x=100,y=280)

emp_annualsalary_label = Label(access,text='Employee Annual Salary',font=('calibri',15),bg='blue',fg='lightblue')
emp_annualsalary_label.place(x=100,y=330)

emp_id = StringVar()
emp_id_entry = Entry(access,textvariable=emp_id,font=('calibri',15),bg='blue',fg='lightblue')
emp_id_entry.place(x=330,y=80)

emp_name = StringVar()
emp_name_entry = Entry(access,textvariable=emp_name,font=('calibri',15),bg='blue',fg='lightblue')
emp_name_entry.place(x=330,y=130)

emp_mail = StringVar()
emp_mail_entry = Entry(access,textvariable=emp_mail,font=('calibri',15),bg='blue',fg='lightblue')
emp_mail_entry.place(x=330,y=180)

emp_designation = StringVar()
emp_designation_entry = Entry(access,textvariable=emp_designation,font=('calibri',15),bg='blue',fg='lightblue')
emp_designation_entry.place(x=330,y=230)

emp_salary = IntVar()
emp_salary_entry = Entry(access,textvariable=emp_salary,font=('calibri',15),bg='blue',fg='lightblue')
emp_salary_entry.place(x=330,y=280)

emp_annualsalary = IntVar()
emp_annualsalary_entry = Entry(access,textvariable=emp_annualsalary,font=('calibri',15),bg='blue',fg='lightblue')
emp_annualsalary_entry.place(x=330,y=330)

btn_cal = Button(access,text='Calculate',font=('calibri',15),bg='lightblue',fg='blue',command=calculate)
btn_cal.place(x=580,y=280)

btn_add = Button(access,text='Add',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=add)
btn_add.place(x=100,y=400)

btn_view = Button(access,text='View',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=view)
btn_view.place(x=300,y=400)

btn_upd = Button(access,text='Update',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=update)
btn_upd.place(x=500,y=400)

btn_del = Button(access,text='Delete',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=delete)
btn_del.place(x=100,y=500)

btn_clr = Button(access,text='Clear',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=clear)
btn_clr.place(x=300,y=500)

btn_ovr = Button(access,text='Overall',font=('calibri',15),bg='lightblue',fg='blue',width=8,height=1,command=overall)
btn_ovr.place(x=500,y=500)

access.mainloop()