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
HeadingLabel=Label(TopHeadingFrame,text='Medicine Management System-Add Medicine',
                   font=('helvetica',24),fg='yellow',bg='blue')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame=Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)
conn=sqlite3.connect('medicine.db')
cursor=conn.cursor()
cursor.execute("""create table if not exists 'medicine'
 (MedicineName text,MedicineID int,Brand text,Chemicalcomponent text,MFG_Date int,EXP_Date text,Price int)""")
conn.commit()
medicine_name=StringVar()
medicine_name.set('')
medicine_nameLabel=Label(MidFrame,text='Medicine Name',font=('helvetika',16),fg='yellow',bg='green')
medicine_nameLabel.grid(row=0,column=0,padx=10,pady=10)
medicine_nameTextBox = Entry(MidFrame,font=('helvetika',16),textvariable=medicine_name)
medicine_nameTextBox.grid(row=0,column=1,padx=10,pady=10)
medicine_Id=IntVar()
medicine_Id.set('')
medicine_IdLabel=Label(MidFrame,text='Medicine Id',font=('helvetika',16),fg='yellow',bg='green')
medicine_IdLabel.grid(row=1,column=0,padx=10,pady=10)
medicine_IdTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=medicine_Id)
medicine_IdTextBox.grid(row=1,column=1,padx=10,pady=10)
brand=StringVar()
brand.set('')
brandLabel=Label(MidFrame,text='Brand Name',
                    font=('helvetika',16),fg='yellow',bg='green')
brandLabel.grid(row=2,column=0,padx=10,pady=10)
brandTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=brand)
brandTextBox.grid(row=2,column=1,padx=10,pady=10)
chemical_component=StringVar()
chemical_component.set('')
chemical_componentLabel=Label(MidFrame,text='chemical component',
                    font=('helvetika',16),fg='yellow',bg='green')
chemical_componentLabel.grid(row=3,column=0,padx=10,pady=10)
chemical_componentTextBox=Entry(MidFrame,font=('helvetika',16),textvariable=chemical_component)
chemical_componentTextBox.grid(row=3,column=1,padx=10,pady=10)
mfg=StringVar()
mfg.set('')
mfgLabel=Label(MidFrame,text='MFG Date',font=('helvetika',16),fg='yellow',bg='green')
mfgLabel.grid(row=4,column=0,padx=10,pady=10)
mfgText=Entry(MidFrame,font=('helvetika',16),textvariable=mfg)
mfgText.grid(row=4,column=1,padx=10,pady=10)
exp=StringVar()
exp.set('')
expLabel=Label(MidFrame,text='EXP Date',font=('helvetika',16),fg='yellow',bg='green')
expLabel.grid(row=5,column=0,padx=10,pady=10)
expText=Entry(MidFrame,font=('helvetika',16),textvariable=exp)
expText.grid(row=5,column=1,padx=10,pady=10)
price=StringVar()
price.set('')
priceLabel=Label(MidFrame,text='Price',font=('helvetika',16),fg='yellow',bg='green')
priceLabel.grid(row=6,column=0,padx=10,pady=10)
priceText=Entry(MidFrame,font=('helvetika',16),textvariable=price)
priceText.grid(row=6,column=1,padx=10,pady=10)
def add():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'medicine'
     (MedicineName,MedicineID,Brand,Chemicalcomponent,MFG_Date,EXP_Date,Price)values(?,?,?,?,?,?,?)""",
                   (str(medicine_name.get()),str(medicine_Id.get()),str(brand.get()),
                               str(chemical_component.get()),(mfg.get()),(exp.get()),(price.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('ADD MEDICINE','new medicine added',icon='info')
    else:
        msg.showinfo('Error','new medicine not added',icon='warning')


def back():
    window.destroy()
    import home

add_btn=Button(MidFrame,text='ADD',command=add,
                  font=('helvetika',18),fg='yellow',bg='brown')
add_btn.grid(row=7,column=1,padx=10,pady=10)

back_btn=Button(MidFrame,text='BACK',command=back,
                 font=('helvetika',16),fg='yellow',bg='brown')
back_btn.grid(row=8,column=1,padx=10,pady=10)




window.mainloop()