from tkinter import *
import databaseAPI as db

def refreshButtonOnClick():
    db.readAsset(None, None)
    assetDisplay = Label(root,text=db.readResult)
    assetDisplay.pack()
#[(0, 'Windows 11', datetime.date(2025, 1, 1), 105.99, 'Jerrys Laptop', 'laptop-123-h123-f', 'NotePad S305', 'Asus', 'Laptop', '192.168.0.1', 8, 256)]

# Initialises window
root = Tk()

# Creating Menubar
menubar = Menu(root)
root.config(menu = menubar)

# Adding Assets Menu and Commands
assets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Assets', menu = assets)
assets.add_command(label ='New', command = None)
assets.add_command(label ='Update', command = None)
assets.add_command(label ='Remove', command = None)

# Adding Employees Menu and Commands
employees = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Employees', menu = employees)
employees.add_command(label ='New', command = None)
employees.add_command(label ='Update', command = None)
employees.add_command(label ='View All', command = None)
employees.add_command(label ='Remove', command = None)

# Adding Exit Button
ExitBtn = menubar.add_command(label ='Close', command = root.destroy)

# Creating Refresh Button
refreshBtn = Button(master=root,text ="Refresh", command=refreshButtonOnClick)
refreshBtn.pack()

# Creating Display Table
table = Frame(root)
i = 0
db.readAsset(None, None)
for x in db.readResult:
    for y in x:
        item = Label(table, text =y)
        item.grid(column= i%12, row=i//12)
        i = i + 1
        print("created grid item")
table.pack()

root.mainloop()