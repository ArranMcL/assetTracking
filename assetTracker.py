from tkinter import *
import databaseAPI as db
from tkcalendar import Calendar, DateEntry

def clearTable():
    for widget in table.winfo_children():
        widget.destroy()

# Reads assets from database and displays them in a table
def refreshButtonOnClick():
    clearTable()
    i = 0
    db.readAsset(None, None)
    keys = ["ID","Operating System","Purchase Date","Purchase Price","Notes","Name","Model","Manufacturer","Type","IP","RAM","Storage"]
    for z, k in enumerate(keys):
        item = Label(table, text=k, bg="red")
        item.grid(column=z%12, row=0, padx=(1, 1), pady=(1, 1))
    for x in db.readResult:
        for y in x:
            item = Label(table, text =y, bg="white")
            item.grid(column= i%12, row=(i+12)//12, padx=(1, 1), pady=(1, 1))
            i = i + 1
    table.pack(padx=(5, 5), pady=(5, 5), side=TOP, anchor=NW)

# Opens a form to insert a new asset
def newAssetForm():
    clearTable()

    nameLabel = Label(table, text="Device Name")
    nameLabel.grid(column=0,row=0)
    name = Entry(table)
    name.grid(column=1,row=0)

    modelLabel = Label(table, text="Model")
    modelLabel.grid(column=0,row=1)
    model = Entry(table)
    model.grid(column=1,row=1)

    manufacturerLabel = Label(table, text="Manufacturer")
    manufacturerLabel.grid(column=0,row=2)
    manufacturer = Entry(table)
    manufacturer.grid(column=1,row=2)

    osLabel = Label(table, text="OS")
    osLabel.grid(column=0,row=3)
    os = Entry(table)
    os.grid(column=1,row=3)

    purchaseDateLabel = Label(table, text="Purchase Date")
    purchaseDateLabel.grid(column=0,row=4)
    cal = Calendar(table, year=2025, month=1, day=1)
    cal.grid(column=1,row=4)



# Sends insert to database
def insertAssetOnClick():
    print("")

# --------------------
#     MAIN WINDOW
# --------------------

root = Tk()
menubar = Menu(root)
root.config(menu = menubar)
root.title("Asset Tracker")
root.geometry("1000x500")
table = Frame(root, bg="white")

# Adding Assets Menu and Commands
assets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='󰍹   Assets', menu = assets)
assets.add_command(label ='New', command = newAssetForm)
assets.add_command(label ='Update', command = None)
assets.add_command(label ='Remove', command = None)

# Adding Employees Menu and Commands
employees = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='   Employees', menu = employees)
employees.add_command(label ='New', command = None)
employees.add_command(label ='Update', command = None)
employees.add_command(label ='View All', command = None)
employees.add_command(label ='Remove', command = None)

# Adding Refresh Button
refreshBtn = menubar.add_command(label ='   Refresh', command=refreshButtonOnClick)

# Adding Exit Button
ExitBtn = menubar.add_command(label ='   Close', command = root.destroy)

# Init Table
refreshButtonOnClick()

root.mainloop()