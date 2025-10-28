#Arran McLoughlin - 2300317
#https://github.com/ArranMcL/assetTracking

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

    def insertAssetOnClick():
        if oDef.get() == "Select an OS" or not pounds.get().isdigit() or \
        not pence.get().isdigit() or notes.get() == "" or name.get() == "" or \
        model.get() == "" or manufacturer.get() == "" or tDef.get() == "Select a Type" or \
        IP.get() == "" or not ram.get().isdigit() or not storage.get().isdigit():
            errorLabel = Label(table, text="Something isn't right! Please take a look over the form and try again.", fg = "red")
            errorLabel.grid(column = 0, row = 12)
        else:
            db.createAsset(oDef.get(), cal.get_date(), pounds.get() + "." + pence.get(),
            notes.get(), name.get(), model.get(), manufacturer.get(), tDef.get(), IP.get(),
            ram.get(), storage.get())
            refreshButtonOnClick()
        

    def detectCurrentDevice():
        print("")

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
    oses = ["Windows", "Linux", "Mac"]
    oDef = StringVar(value="Select an OS")
    os = OptionMenu(table, oDef, *oses)
    os.grid(column=1,row=3)

    purchaseDateLabel = Label(table, text="Purchase Date")
    purchaseDateLabel.grid(column=0,row=4)
    cal = Calendar(table, year=2025, month=1, day=10, date_pattern='yyyy-mm-dd')
    cal.grid(column=1,row=4)

    purchasePriceLabel = Label(table, text="Purchase Price")
    purchasePriceLabel.grid(column=0,row=5)
    priceSelector = Frame(table, bg="white")
    poundsLabel = Label(priceSelector, text="$")
    pounds = Entry(priceSelector, width=5)
    penceLabel = Label(priceSelector, text=".")
    pence = Entry(priceSelector, width=3)
    poundsLabel.grid(column=0, row=0)
    pounds.grid(column=1, row=0)
    penceLabel.grid(column=2, row=0)
    pence.grid(column=3, row=0)
    priceSelector.grid(column=1,row=5) 

    notesLabel = Label(table, text="Notes")
    notesLabel.grid(column=0,row=6)
    notes = Entry(table)
    notes.grid(column=1,row=6)

    typeLabel = Label(table, text="Type")
    typeLabel.grid(column=0,row=7)
    types = ["PC", "Laptop", "Server", "Phone", "Tablet", "Printer"]
    tDef = StringVar(value="Select a Type")
    dType = OptionMenu(table, tDef, *types)
    dType.grid(column=1,row=7)

    IPLabel = Label(table, text="IPv4")
    IPLabel.grid(column=0,row=8)
    IP = Entry(table)
    IP.grid(column=1,row=8)

    ramLabel = Label(table, text="Ram (GB)")
    ramLabel.grid(column=0,row=9)
    ram = Entry(table)
    ram.grid(column=1,row=9)

    storageLabel = Label(table, text="Storage (GB)")
    storageLabel.grid(column=0,row=10)
    storage = Entry(table)
    storage.grid(column=1,row=10)

    autoBtn = Button(table, text="Use Current Device", command=detectCurrentDevice)
    autoBtn.grid(column=0, row=11)

    submitBtn = Button(table, text="Submit", command=insertAssetOnClick)
    submitBtn.grid(column=1, row=11)

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