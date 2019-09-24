from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
class Admin(Frame):

    def __init__(self,master):
        super().__init__(master)
        
        
        self.btnDept=Button(self,text='Add Department',command=self.dept)
        self.btnEmployee=Button(self,text='Add Employee',command=self.addemployee)
        self.btnSalary=Button(self,text='Add Salary',command=self.salary)
            
        self.btnDept.grid(row=0,column=0)
        self.btnEmployee.grid(row=0,column=1)
        self.btnSalary.grid(row=0,column=2)
        
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        self.columnconfigure(2,pad=15)
            
        self.pack()
        
    def clear(self):
        self.txtusername.delete(0,'end')
        self.txtpassword.delete(0,'end')
        self.txtusername.focus()
     
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()    
          
         
    def dept(self):
        root1=Tk()
        obj1=Dept(root1)
        root1.title('Add Department')
        root1.geometry('450x350')
        root1.mainloop()
        
    def addemployee(self):
        root2=Tk()
        obj2=AddEmployee(root2)
        root2.geometry('450x450')
        root2.title('Add Employee')
        root2.mainloop()
        
    def salary(self):
        root4=Tk()
        obj4=Salary(root4)
        root4.geometry('450x450')
        root4.title('Add Salary Acc to Designation')
        root4.mainloop()
        
       

class Dept(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.lblDeptNo=Label(self,text='Department Number')
        self.lblDept=Label(self,text='Department')
        
        self.txtDeptNo=Entry(self)
        self.txtDept=Entry(self)
        
        self.btnDepartment=Button(self,text='ADD',command=self.adddepartment)
        
        self.lblDeptNo.grid(row=0,column=0)
        self.lblDept.grid(row=1,column=0)
        self.txtDeptNo.grid(row=0,column=1)
        self.txtDept.grid(row=1,column=1)
        
        self.btnDepartment.grid(columnspan=2)
        
        self.rowconfigure(0,pad=15)
        self.rowconfigure(1,pad=15)
        self.rowconfigure(2,pad=15)
        self.rowconfigure(3,pad=15)
        
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
        
    def clear(self):
        self.txtDeptNo.delete(0,'end')
        self.txtDept.delete(0,'end')
        self.txtDeptNo.focus()
     
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()     
    
    def adddepartment(self):
        self.connect()
        deptnumber=(int)(self.txtDeptNo.get())
        department=self.txtDept.get()
        i=self.cur.execute("insert into dept values(%d,'%s')"%(deptnumber,department))
        if i>=1:
            self.con.commit()
            self.clear()
            msg.showinfo('Information','Record Saved')
            self.con.close()
        else:
            self.showerror('Information','Something went wrong')
        

class AddEmployee(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.lblEmpno=Label(self,text='Employee ID')
        self.lblEname=Label(self,text='Employee Name')
        self.lblDesig=Label(self,text='Designation')
        self.lblSalary=Label(self,text='Salary')
        self.lblDeptNo=Label(self,text='Department No.')
        
        self.txtEmpno=Entry(self)
        self.txtEname=Entry(self)
        self.txtDesig=Entry(self)
        self.txtSalary=Entry(self)
        self.txtDeptNo=Entry(self)
        
        self.btnSave=Button(self,text='Save',command=self.save)
        self.btnSearch=Button(self,text='Search',command=self.search)
        self.btnDelete=Button(self,text='Delete',command=self.delete)
        self.btnUpdate=Button(self,text='Update',command=self.update)
        self.btnExit=Button(self,text='Exit',command=self.exit)
        self.btnShow=Button(self,text='Show All',command=self.all)
        
        self.rowconfigure(0,pad=7)
        self.rowconfigure(1,pad=7)
        self.rowconfigure(2,pad=7)
        self.rowconfigure(3,pad=7)
        self.rowconfigure(4,pad=7)
        self.rowconfigure(5,pad=7)
        self.rowconfigure(5,pad=7)
        
        self.columnconfigure(0,pad=5)
        self.columnconfigure(1,pad=5)
        self.columnconfigure(2,pad=5)
        
        self.lblEmpno.grid(row=0,column=0)
        self.txtEmpno.grid(row=0,column=1)
        
        self.lblEname.grid(row=1,column=0)
        self.txtEname.grid(row=1,column=1)
        
        self.lblDesig.grid(row=2,column=0)
        self.txtDesig.grid(row=2,column=1)
        
        self.lblSalary.grid(row=3,column=0)
        self.txtSalary.grid(row=3,column=1)
        
        self.lblDeptNo.grid(row=4,column=0)
        self.txtDeptNo.grid(row=4,column=1)
        
        self.btnSave.grid(row=5,column=0)
        self.btnSearch.grid(row=5,column=1)
        self.btnDelete.grid(row=5,column=2)
        self.btnUpdate.grid(row=6,column=0)
        self.btnExit.grid(row=6,column=1)
        self.btnShow.grid(row=6,column=2)
        
        self.pack()
    
    def clear(self):
        self.txtEmpno.delete(0,'end')
        self.txtEname.delete(0,'end')
        self.txtDesig.delete(0,'end')
        self.txtSalary.delete(0,'end')
        self.txtDeptNo.delete(0,'end')
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()
        
    def save(self):
        self.connect()
        empno=(int)(self.txtEmpno.get())
        ename=self.txtEname.get()
        desig=self.txtDesig.get()
        salary=(float)(self.txtSalary.get())
        deptnumber=(int)(self.txtDeptNo.get())
        i=self.cur.execute("insert into employee values(%d,'%s','%s',%f,%d)"%(empno,ename,desig,salary,deptnumber))
        if i>=1:
            self.con.commit()
            msg.showinfo('Confirmation','Record Saved')
            self.clear()
            self.txtEmpno.focus()
            self.con.close()
            
    def search(self):  #colab
        self.connect()
        empno=(int)(self.txtEmpno.get())
        self.cur.execute("select * from employee where empno=%d"%(empno))
        rs=self.cur.fetchall()
        if len(rs)>0:
            self.txtEname.insert(0,rs[0][1])
            self.txtDesig.insert(0,rs[0][2])
            self.txtSalary.insert(0,rs[0][3])
            self.txtDeptNo.insert(0,rs[0][4])
        else:
            msg.showerror('Error info','Recod not found')
            
    def update(self):
        self.connect()
        empno=(int)(self.txtEmpno.get())
        ename=self.txtEname.get()
        desig=self.txtDesig.get()
        salary=(float)(self.txtSalary.get())
        deptnumber=(int)(self.txtDeptNo.get())
        i=self.cur.execute("update employee set ename='%s',desig='%s',salary=%f,deptno=%d where empno=%d"%(ename,desig,salary,deptnumber,empno))
        if i>=1:
            self.con.commit()
            msg.showinfo('Updation message','Record updated')
            self.clear()
            self.con.close()
            
    def delete(self):
        self.connect()
        empno=(int)(self.txtEmpno.get())
        i=self.cur.execute("delete from employee where empno=%d"%(empno))
        if i>=1:
            confirm=msg.askquestion('Confirmation box','Are r u sure to delete',icon='warning')
            if confirm =='yes':
                self.con.commit()
                self.con.close()
            else:
                msg.showerror('Info','Record not found')
                self.con.close()
        self.clear()
        
    def all(self):
        root3=Tk()
        obj3=EmpAll(root3)
        root3.geometry('350x450')
        root3.mainloop()
            
    def exit(self):
        exit(0)
        
class EmpAll(Frame):
    def __init__(self,master):
        super().__init__(master)
    
        self.lblEmpno=Label(self,text='Employee No')
        self.lblEname=Label(self,text='Employee Name')
        self.lblDesig=Label(self,text='Designation')
        self.lblSalary=Label(self,text='Salary')
        self.lblDeptNo=Label(self,text='Department Number')
        
        self.rowconfigure(0,pad=10)
        
        self.columnconfigure(0,pad=10)
        self.columnconfigure(1,pad=10)
        self.columnconfigure(2,pad=10)
        self.columnconfigure(3,pad=10)
        self.columnconfigure(4,pad=10)
        
        self.lblEmpno.grid(row=0,column=1)
        self.lblEname.grid(row=0,column=2)
        self.lblDesig.grid(row=0,column=3)
        self.lblSalary.grid(row=0,column=4)
        self.lblDeptNo.grid(row=0,column=5)
        
        con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        cur=con.cursor()
        cur.execute("select * from employee")
        rs=cur.fetchall()
        i=0
        for x in range(len(rs)):
            i+=1
            self.rowconfigure(x,pad=10)
            self.l1=Label(self,text=rs[x][0])
            self.l2=Label(self,text=rs[x][1])
            self.l3=Label(self,text=rs[x][2])
            self.l4=Label(self,text=rs[x][3])
            self.l4=Label(self,text=rs[x][4])
            
            self.l1.grid(row=i,column=1)
            self.l2.grid(row=i,column=2)
            self.l3.grid(row=i,column=3)
            self.l4.grid(row=i,column=4)
            self.l4.grid(row=i,column=5)
            
        self.pack()        
        
class Salary(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.lblDesig=Label(self,text='Designation')
        self.lblMinSalary=Label(self,text='Mininmum Salary')
        self.lblMaxSalary=Label(self,text='Maximum Salary')
        
        self.txtDesig=Entry(self)
        self.txtMinSalary=Entry(self)
        self.txtMaxSalary=Entry(self)
        
        self.btnAdd=Button(self,text='Add',command=self.add)
        
        self.lblDesig.grid(row=0,column=0)
        self.lblMinSalary.grid(row=1,column=0)
        self.lblMaxSalary.grid(row=2,column=0)
        
        self.txtDesig.grid(row=0,column=1)
        self.txtMinSalary.grid(row=1,column=1)
        self.txtMaxSalary.grid(row=2,column=1)
        
        self.btnAdd.grid(columnspan=2)
        
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
    
    def clear(self):
        self.txtDesig.delete(0,'end')
        self.txtMinSalary.delete(0,'end')
        self.txtMaxSalary.delete(0,'end')
        self.txtDesig.focus()
     
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor() 
        
    def add(self):
        self.connect()
        desig=self.txtDesig.get()
        minsal=(float)(self.txtMinSalary.get())
        maxsal=(float)(self.txtMaxSalary.get())
        i=self.cur.execute("insert into desig_salary values('%s',%f,%f)"%(desig,minsal,maxsal))
        if i>=1:
            self.con.commit()
            self.clear()
            msg.showinfo('Information','Record Saved')
            self.con.close()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        