from tkinter import *
import sqlite3
import tkinter.messagebox as msg
window=Tk()
window.geometry('900x600')
reg_image= PhotoImage(file='registerbg.png')
bg_label=Label(window,image=reg_image)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")
window.iconbitmap('Icon.ico')
TopHeadingFrame=Frame(window, width=700,bd=3)
TopHeadingFrame.pack(side=TOP)
HeadingLabel=Label(TopHeadingFrame,text='Medicine Management System-Register',
                   font=('helvetica',24),fg='yellow',bg='blue')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)
MidFrame=Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)
conn=sqlite3.connect('medicine.db')
cursor=conn.cursor()
cursor.execute("""create table if not exists 'userdata'
 (Name text,ID int,UserName text,Password text,Mobile int,Email text)""")
conn.commit()
name=StringVar()
name.set('')
NameLabel=Label(MidFrame,text='Name',font=('helvetika',16),fg='yellow',bg='green')
NameLabel.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font=('helvetika',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)
id=IntVar()
id.set('')
IdLabel=Label(MidFrame,text='Id',font=('helvetika',16),fg='yellow',bg='green')
IdLabel.grid(row=1,column=0,padx=10,pady=10)
IdTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=id)
IdTextBox.grid(row=1,column=1,padx=10,pady=10)
username=StringVar()
username.set('')
usernameLabel=Label(MidFrame,text='username',
                    font=('helvetika',16),fg='yellow',bg='green')
usernameLabel.grid(row=2,column=0,padx=10,pady=10)
usernameTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=username)
usernameTextBox.grid(row=2,column=1,padx=10,pady=10)
password=StringVar()
password.set('')
passwordLabel=Label(MidFrame,text='password',
                    font=('helvetika',16),fg='yellow',bg='green')
passwordLabel.grid(row=3,column=0,padx=10,pady=10)
passwordTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=password)
passwordTextBox.grid(row=3,column=1,padx=10,pady=10)
mobile=StringVar()
mobile.set('')
mobileLabel=Label(MidFrame,text='mobile',font=('helvetika',16),fg='yellow',bg='green')
mobileLabel.grid(row=4,column=0,padx=10,pady=10)
mobileText=Entry(MidFrame,font=('helvetika',16),textvariable=mobile)
mobileText.grid(row=4,column=1,padx=10,pady=10)
email=StringVar()
email.set('')
emailLabel=Label(MidFrame,text='email',font=('helvetika',16),fg='yellow',bg='green')
emailLabel.grid(row=5,column=0,padx=10,pady=10)
emailText=Entry(MidFrame,font=('helvetika',16),textvariable=email)
emailText.grid(row=5,column=1,padx=10,pady=10)
def register():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'userdata'
     (name,id,username,password,mobile,email)values(?,?,?,?,?,?)""",
                   (str(name.get()),str(id.get()),str(username.get()),
                               str(password.get()),(mobile.get()),(email.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('confirmation','new user added',icon='info')
    else:
        msg.showinfo('Error','new user not added',icon='warning')


def login():
    window.destroy()
    import login

if cursor.rowcount > 0:
    msg.showinfo('confirmation', 'new user added', icon='info')
else:
    msg.showinfo('Error', 'new user not added', icon='warning')
submit_btn=Button(MidFrame,text='SUBMIT',command=register,
                  font=('helvetika',18),fg='yellow',bg='brown')
submit_btn.grid(row=6,column=1,padx=10,pady=10)
AlreadyUserLabel=Label(MidFrame,text='already a user?',
                       font=('helvetika',16),fg='yellow',bg='green')
AlreadyUserLabel.grid(row=7,column=0,padx=10,pady=10)
login_btn=Button(MidFrame,text='LOGIN',command=login,
                 font=('helvetika',16),fg='yellow',bg='brown')
login_btn.grid(row=7,column=1,padx=10,pady=10)






window.mainloop()




