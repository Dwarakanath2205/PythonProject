import sqlite3
from re import search
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk #themed tkinter

window=Tk()
window.geometry('900x600')
reg_image= PhotoImage(file='registerbg.png')
bg_label=Label(window,image=reg_image)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")
window.iconbitmap('Icon.ico')
TopHeadingFrame=Frame(window, width=700,bd=3)
TopHeadingFrame.pack(side=TOP)
HeadingLabel=Label(TopHeadingFrame,text='Medicine Management System-Search Medicine',
                   font=('helvetica',24),fg='yellow',bg='blue')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame=Frame(window, width=700,bd=3)
MidFrame.pack(side=TOP)

view_frame=Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)

conn=sqlite3.connect('medicine.db')
cursor=conn.cursor()
cursor.execute("""create table if not exists 'medicine'
 (MedicineName text,MedicineID int,Brand text,Chemicalcomponent text,MFG_Date int,EXP_Date text,Price int)""")
conn.commit()

tv=ttk.Treeview(view_frame,
                columns=('MedicineName','MedicineID','Brand','Chemicalcomponent','MFG_Date','EXP_Date','Price'))
tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineID')
tv.heading('#3',text='Brand')
tv.heading('#4',text='Chemicalcomponent')
tv.heading('#5',text='MFG_Date')
tv.heading('#6',text='EXP_Date')
tv.heading('#7',text='Price')

tv.column('#0',width=0,stretch=NO)
tv.column('#1',width=50)
tv.column('#2',width=50)
tv.column('#3',width=50)
tv.column('#4',width=50)
tv.column('#5',width=50)
tv.column('#6',width=50)
tv.column('#7',width=50)
tv.pack(fill=X)

# Define an Entry widget to accept MedicineName
medicine_name_label = Label(MidFrame, text="Enter Medicine Name", font=('helvetica', 16),fg='yellow',bg='green')
medicine_name_label.grid(row=0, column=0, padx=10, pady=10)

MedicineName = Entry(MidFrame, font=('helvetica', 16))
MedicineName.grid(row=0, column=1, padx=10, pady=10)


def search():
    entered_name = MedicineName.get()  # Get the input from the Entry widget
    if not entered_name:
        msg.showerror("Error", "Please enter a Medicine Name!")
        return

    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()

    # Query the database for the entered MedicineName
    cursor.execute("SELECT * FROM 'medicine' WHERE MedicineName = ?", (entered_name,))
    data = cursor.fetchall()
    conn.close()

    if data:
        # Clear the Treeview before adding new data
        for item in tv.get_children():
            tv.delete(item)

        # Insert the fetched data into the Treeview
        for row in data:
            tv.insert("", "end", values=row)
    else:
        msg.showinfo("No Results", "No medicine found with the entered name.")


# Attach the search function to the SEARCH button
search_btn = Button(MidFrame, text='SEARCH', command=search,
                    font=('helvetica', 16), fg='yellow', bg='brown')
search_btn.grid(row=1, column=1, padx=10, pady=10)


def back():
    window.destroy()
    import home
back_btn=Button(MidFrame,text='BACK',command=back,
                 font=('helvetika',16),fg='yellow',bg='brown')
back_btn.grid(row=1,column=0,padx=10,pady=10)






window.mainloop()