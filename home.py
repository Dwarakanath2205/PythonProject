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
HeadingLabel=Label(TopHeadingFrame,text='Medicine Management System-Home',
                   font=('helvetica',24),fg='yellow',bg='blue')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)
MidFrame=Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)
def add():
    window.destroy()
    import add_medicine
add_btn=Button(MidFrame,text='ADD MEDICINE',command=add,
                 font=('helvetika',16),fg='yellow',bg='brown')
add_btn.grid(row=0,column=1,padx=10,pady=10)
def view():
    window.destroy()
    import view_medicine
view_btn=Button(MidFrame,text='VIEW MEDICINE',command=view,
                 font=('helvetika',16),fg='yellow',bg='brown')
view_btn.grid(row=1,column=1,padx=10,pady=10)
def search():
    window.destroy()
    import search_medicine

search_btn=Button(MidFrame,text='SEARCH MEDICINE',command=search,
                 font=('helvetika',16),fg='yellow',bg='brown')
search_btn.grid(row=2,column=1,padx=10,pady=10)

def delete():
    window.destroy()
    import delete_medicine
delete_btn=Button(MidFrame,text='DELETE',command=delete,
                 font=('helvetika',16),fg='yellow',bg='brown')
delete_btn.grid(row=3,column=1,padx=10,pady=10)

def logout():
    window.destroy()
    import login
login_btn=Button(MidFrame,text='LOGOUT',command=logout,
                 font=('helvetika',16),fg='yellow',bg='brown')
login_btn.grid(row=4,column=1,padx=10,pady=10)



window.mainloop()

