from tkinter import *
from pymysql import *
from datetime import *
from time import *
from tkinter import messagebox as msg
#project---- login screen (username,password)----admin login----employee login
#in adminn login---opens diff screen--add dept()--add eplopyee()--- create salary(min and max salary acc to desig)
#in employee login---opens diff screen--attendence--time in--time out-- password change --pf-- current month salary
class EmployeeLogin(Frame):

    def __init__(self,master):
        super().__init__(master)
        
        self.btnAttendence=Button(self,text='Attendence',command=self.callone)
        self.btnPasswdChange=Button(self,text='Change Password',command=self.calltwo)
        self.btnPF=Button(self,text='PF',command=self.callthree)
        self.btnCMSalary=Button(self,text='Current month Salary',command=self.callfour)
     
        self.btnAttendence.grid(row=0,column=0)
        self.btnPasswdChange.grid(row=0,column=1)
        self.btnPF.grid(row=1,column=0)
        self.btnCMSalary.grid(row=1,column=1)
        
        self.rowconfigure(0,pad=15)
        self.rowconfigure(1,pad=15)
       
        self.columnconfigure(0,pad=20)
        self.columnconfigure(1,pad=20)
         
             
        
        self.pack()
        
    def clear(self):
        self.txtusername.delete(0,'end')
        self.txtpassword.delete(0,'end')
        self.txtusername.focus()
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()
        
    def callone(self):
        root1=Tk()
        obj1=Attendence(root1)
        root1.title('Attendence')
        root1.geometry('350x250')
        root1.mainloop()
        
    def calltwo(self):
        root2=Tk()
        obj2=PasswdChange(root2)
        root2.title('Change Password')
        root2.geometry('350x250')
        root2.mainloop() 
        
    def callthree(self):
        root3=Tk()
        obj3=EPF(root3)
        root3.title('EPF')
        root3.geometry('350x250')
        root3.mainloop() 
     
    def callfour(self):
        root4=Tk()
        obj4=SalaryCalc(root4)
        root4.title('Salary Calculator')
        root4.geometry('450x350')
        root4.mainloop()
        
class Attendence(Frame):
    def __init__(self,master):
        super().__init__(master)
       
       
        self.lblEmpId=Label(self,text='Employee ID')
        self.txtEmpId=Entry(self)
        self.btnTimeIn=Button(self,text='Time In',command=self.timeIn) 
        self.btnTimeOut=Button(self,text='Time out',command=self.timeOut)
        
        
        self.lblEmpId.grid(row=0,column=0)
        self.txtEmpId.grid(row=0,column=1)
        self.btnTimeIn.grid(row=1,column=0)
        self.btnTimeOut.grid(row=1,column=1)
        
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        
       
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
        
    def clear(self):
        self.txtEmpId.delete(0,'end')
        self.txtEmpId.focus()
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor() 
        

    def usertime(self):
        dt=datetime.now()
        self.hh=dt.hour
        self.mm=dt.minute
        self.ss=dt.second
        self.d=dt.day
        self.m=dt.month
        self.y=dt.year
        self.alltime=str(self.hh)+":"+str(self.mm)+":"+str(self.ss)
        self.alldate=str(self.d)+":"+str(self.m)+":"+str(self.y)
         
    def timeIn(self):
        self.connect()
        self.usertime()
        empid=(int)(self.txtEmpId.get())
        self.timein=self.alltime
        timeout='waititng...'
        timediff='null'
        salary='null'
        date=self.alldate
        i=self.cur.execute("insert into time values(%d,'%s','%s','%s','%s','%s')"%(empid,date,self.timein,timeout,timediff,salary))
        if i>=1:
            self.con.commit()
            self.con.close()
            msg.showinfo('Confirmation','Welcome')
            self.clear()
    
    def timeOut(self):
        self.connect()
        self.usertime()
        empid=(int)(self.txtEmpId.get())
        timeout=self.alltime
        date=self.alldate
        i=self.cur.execute("select timein from time where empno=%d and date='%s'"%(empid,date))
        rs=self.cur.fetchall()
        if len(rs)>0:
            timein=rs[0][0]
        FMT='%H:%M:%S'
        tdelta= datetime.strptime(timeout,FMT)-datetime.strptime(timein,FMT)  
        i=self.cur.execute("update time set timeout='%s',timediff='%s' where empno='%s' and date='%s'"%(timeout,tdelta,empid,date))
        if i>=1:
            self.con.commit()
            msg.showinfo('Confirmation','Bye')
            self.con.close()
            
        self.connect()
        j=self.cur.execute("select * from employee where empno=%d"%(empid))
        rs=self.cur.fetchall()
        salary=rs[0][3]
        i=self.cur.execute("select * from time where date='%s' and empno=%d"%(date,empid))
        rs=self.cur.fetchall()
        time=rs[0][4]
        t=time.split(':')
        total_minutes= int(t[0])*60+int(t[1])*1+int(t[2])/60
        per_min_salary=salary/(30*8*60)
        new_salary=total_minutes*per_min_salary
        i=self.cur.execute("update time set salary='%s' where empno=%d and date='%s'"%(new_salary,empid,date))
        if i>=0:
            self.con.commit()
            self.con.close()    
            
            
            
class PasswdChange(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.lblEmpId=Label(self,text='Employee ID')
        self.lblEmpName=Label(self,text='Employee Name')
        self.lblCurrentPasswd=Label(self,text='Current Password')
        self.lblPasswdChange=Label(self,text='Password change to...')
        
        self.txtEmpId=Entry(self)
        self.txtEmpName=Entry(self)
        self.txtCurrentPasswd=Entry(self)
        self.txtPasswdChange=Entry(self)
        
        self.btnDone=Button(self,text='Done',command=self.change)
       
        self.lblEmpId.grid(row=0,column=0)
        self.lblEmpName.grid(row=1,column=0)
        self.lblCurrentPasswd.grid(row=2,column=0)
        self.lblPasswdChange.grid(row=3,column=0)
        
        self.txtEmpId.grid(row=0,column=1)
        self.txtEmpName.grid(row=1,column=1)
        self.txtCurrentPasswd.grid(row=2,column=1)
        self.txtPasswdChange.grid(row=3,column=1)
        
        self.btnDone.grid(columnspan=2)
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.rowconfigure(3,pad=10)
        self.rowconfigure(4,pad=10)
        
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
        
    def clear(self):
        self.txtEmpId.delete(0,'end')
        self.txtEmpName.delete(0,'end')
        self.txtCurrentPasswd.delete(0,'end')
        self.txtPasswdChange.delete(0,'end')
        self.txtEmpId.focus()
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()    
        
    def change(self):
        self.connect()
        empid=(int)(self.txtEmpId.get())
        ename=self.txtEmpName.get()
        currentPasswd=self.txtCurrentPasswd.get()
        passwdChange=self.txtPasswdChange.get()
        i=self.cur.execute("update login set password='%s' where username='%s' and password='%s'"%(passwdChange,ename,currentPasswd))
        if i>=1:
            self.con.commit()
            msg.showinfo('Updation message','Password Updated')
            self.clear()
            self.con.close()
        else:
            msg.showerror('Information','Error')
            self.con.close()
        
class EPF(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.lblEmpId=Label(self,text='Employee ID')
        self.lblEmpName=Label(self,text='Employee Name')
        self.lblCurrentMonthEPF=Label(self,text='Current Month EPF')
       
        self.txtEmpId=Entry(self)
        self.txtEmpName=Entry(self)
        self.txtCurrentMonthEPF=Entry(self)
        
        self.lblEmpId.grid(row=0,column=0)
        self.lblEmpName.grid(row=1,column=0)
        self.lblCurrentMonthEPF.grid(row=2,column=0)
        self.btnSearch=Button(self,text='Search',command=self.pf)
        
        self.txtEmpId.grid(row=0,column=1)
        self.txtEmpName.grid(row=1,column=1)
        self.txtCurrentMonthEPF.grid(row=2,column=1)
        
        self.btnSearch.grid(columnspan=2)
        
        self.btnSearch=Button(self,text='Search')
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.rowconfigure(3,pad=10)
        
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
    def clear(self):
        self.txtEmpId.delete(0,'end')
        self.txtEmpName.delete(0,'end')
        self.txtCurrentMonthEPF.delete(0,'end')
        self.txtEmpId.focus()
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()    
        
    def pf(self):
        self.connect()
        empid=(int)(self.txtEmpId.get())
        self.cur.execute("select salary from time where empno=%d"%(empid))
        rs=self.cur.fetchall()
        sum=0
        for x in range(len(rs)):
            sum+=float(rs[x][0])
        pf=((sum*12)/100)
        self.txtCurrentMonthEPF.insert(0,pf)
        self.con.commit()
        msg.showinfo("confirmation","Welcome")
        self.con.close()
	    

class SalaryCalc(Frame):

    def __init__(self,master):
        super().__init__(master)
        
        self.lblEmpId=Label(self,text='Employee ID')
        self.lblEmpName=Label(self,text='Employee Name')
        self.lblTotalSalary=Label(self,text='Total Salary')
        
        self.txtEmpId=Entry(self)
        self.txtEmpName=Entry(self)
        self.txtCurrentSalary=Entry(self)
        
        self.btnSearch=Button(self,text='Calculate',command=self.salary)
        
        self.lblEmpId.grid(row=0,column=0)
        self.lblEmpName.grid(row=1,column=0)
        self.lblTotalSalary.grid(row=2,column=0)
        self.txtEmpId.grid(row=0,column=1)
        self.txtEmpName.grid(row=1,column=1)
        self.txtCurrentSalary.grid(row=2,column=1)
        
  
        self.btnSearch.grid(columnspan=2)
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.rowconfigure(3,pad=10)
        
        self.columnconfigure(0,pad=15)
        self.columnconfigure(1,pad=15)
        
        self.pack()
        
    def clear(self):
        self.txtEmpId.delete(0,'end')
        self.txtEmpName.delete(0,'end')
        self.txtCurrentSalary.delete(0,'end')
        self.txtEmpId.focus()
        
    def connect(self):
        self.con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        self.cur=self.con.cursor()

    def salary(self):
        self.connect()
        empid=(int)(self.txtEmpId.get())
        self.cur.execute("select salary from time where empno=%d"%(empid))
        rs=self.cur.fetchall()
        sum=0
        for x in range(len(rs)):
            sum+=float(rs[x][0])
        self.txtCurrentSalary.insert(0,sum)
        
    




            