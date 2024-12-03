import sqlite3
from tkinter import *
from tkinter import ttk  # Themed tkinter
import tkinter.messagebox as msg  # For message boxes

# Set up the main window
window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file='registerbg.png')
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")
window.iconbitmap('Icon.ico')

# Top Heading
TopHeadingFrame = Frame(window, width=700, bd=3)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text='Medicine Management System - View Medicine',
                     font=('helvetica', 24), fg='yellow', bg='blue')
HeadingLabel.grid(row=0, column=0, padx=10, pady=10)

# Mid Frame for additional controls
MidFrame = Frame(window, width=700, bd=3)
MidFrame.pack(side=TOP)

# Frame to hold Treeview
view_frame = Frame(window, bd=1)
view_frame.pack(side=TOP, fill=X)

# Create the Treeview
tv = ttk.Treeview(view_frame,
                  columns=('MedicineName', 'MedicineID', 'Brand', 'Chemicalcomponent', 'MFG_Date', 'EXP_Date', 'Price'))
tv.heading('#1', text='MedicineName')
tv.heading('#2', text='MedicineID')
tv.heading('#3', text='Brand')
tv.heading('#4', text='Chemicalcomponent')
tv.heading('#5', text='MFG_Date')
tv.heading('#6', text='EXP_Date')
tv.heading('#7', text='Price')

tv.column('#0', width=0, stretch=NO)  # Hidden column for default index
tv.column('#1', width=150)
tv.column('#2', width=100)
tv.column('#3', width=150)
tv.column('#4', width=150)
tv.column('#5', width=100)
tv.column('#6', width=100)
tv.column('#7', width=100)
tv.pack(fill=X)

# Database connection and fetching data
conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM 'medicine'")  # Fetch all records from the 'medicine' table
data = cursor.fetchall()
conn.commit()
conn.close()

# Insert data into Treeview (Added functionality)
for row in data:
    tv.insert("", "end", values=row)  # Add each record to the Treeview

# Back Button functionality
def back():
    window.destroy()
    import home  # Navigate to the home module

# Back Button
back_btn = Button(MidFrame, text='BACK', command=back,
                  font=('helvetika', 16), fg='yellow', bg='brown')
back_btn.grid(row=8, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()
