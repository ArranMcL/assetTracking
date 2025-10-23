from tkinter import *
import databaseAPI as db

def clearTable():
    for widget in table.winfo_children():
        widget.destroy()

# Reads assets from database and displays them in a table
def refreshButtonOnClick():
    # Creating Display Table
    clearTable()
    i = 0
    db.readAsset(None, None)
    keys = ["ID","Name","Model","Manufacturer","Operating System","Purchase Date","Purchase Price","Notes","Type","IP","RAM","Storage"]
    for z, k in enumerate(keys):
        item = Label(table, text=k, bg="red")
        item.grid(column=z%12, row=0, padx=(1, 1), pady=(1, 1))
    for x in db.readResult:
        for y in x:
            item = Label(table, text =y, bg="white")
            item.grid(column= i%12, row=(i+12)//12, padx=(1, 1), pady=(1, 1))
            i = i + 1
    table.pack(padx=(5, 5), pady=(5, 5), side=TOP, anchor=NW)

# Opens a form to insert a new item
def insertAssetOnClick():
    clearTable()

# Initialises window
root = Tk()
menubar = Menu(root)
root.config(menu = menubar)
root.title("Asset Tracker")
root.geometry("1000x500")
table = Frame(root, bg="white")

# Adding Assets Menu and Commands
assets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Assets', menu = assets)
assets.add_command(label ='New', command = insertAssetOnClick)
assets.add_command(label ='Update', command = None)
assets.add_command(label ='Remove', command = None)

# Adding Employees Menu and Commands
employees = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Employees', menu = employees)
employees.add_command(label ='New', command = None)
employees.add_command(label ='Update', command = None)
employees.add_command(label ='View All', command = None)
employees.add_command(label ='Remove', command = None)

# Adding Refresh Button
refreshBtn = menubar.add_command(label ='Refresh', command=refreshButtonOnClick)

# Adding Exit Button
ExitBtn = menubar.add_command(label ='Close', command = root.destroy)

# Init Table
refreshButtonOnClick()

root.mainloop()