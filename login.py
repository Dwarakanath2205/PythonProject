import sqlite3
from tkinter import *
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
HeadingLabel=Label(TopHeadingFrame,text='Medicine Management System-Login',
                   font=('helvetica',24),fg='yellow',bg='blue')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)
MidFrame=Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)
username=StringVar()
username.set('')
usernameLabel=Label(MidFrame,text='username',
                    font=('helvetika',16),fg='yellow',bg='green')
usernameLabel.grid(row=2,column=0,padx=10,pady=10)
usernameTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=username)
usernameTextBox.grid(row=2,column=1,padx=10,pady=10)
password=StringVar()
password.set('')
passwordLabel=Label(MidFrame,text='password',font=('helvetika',16),fg='yellow',bg='green')
passwordLabel.grid(row=3,column=0,padx=10,pady=10)
passwordTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=password)
passwordTextBox.grid(row=3,column=1,padx=10,pady=10)
def register():
    window.destroy()
    import register
def login():
    conn=sqlite3.connect('medicine.db')
    cursor=conn.cursor()
    cursor.execute("""select*from 'userdata' where
    UserName= ? and password= ?""",(username.get(),password.get()))
    if len(list(cursor.fetchall()))>0:
        msg.showinfo('Login confirmation','Login Successfull',icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('Login Error','User Not Defined',icon='warning')





submit_btn=Button(MidFrame,text='Register',command=register,
                  font=('helvetika',18),fg='yellow',bg='brown')
submit_btn.grid(row=5,column=1,padx=10,pady=10)
NotUserLabel=Label(MidFrame,text='Not a user yet?',
                       font=('helvetika',16),fg='yellow',bg='green')
NotUserLabel.grid(row=5,column=0,padx=10,pady=10)
login_btn=Button(MidFrame,text='LOGIN',command=login,
                 font=('helvetika',16),fg='yellow',bg='brown')
login_btn.grid(row=4,column=1,padx=10,pady=10)
window.mainloop()
