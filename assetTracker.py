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
    keys = ["ID","Operating System","Purchase Date","Purchase Price ($)","Notes","Name","Model","Manufacturer","Type","IP","RAM (GB)","Storage (GB)","Employee Email"]
    for z, k in enumerate(keys):
        item = Label(table, text=k, bg="white", font='Helvetica 10 bold')
        item.grid(column=z%13, row=0, padx=(1, 1), pady=(1, 1), sticky="w")
    for x in db.readResult:
        for y in x:
            item = Label(table, text =y, bg="white")
            item.grid(column= i%13, row=(i+13)//13, padx=(1, 1), pady=(1, 1))
            i = i + 1
    table.pack(padx=(5, 5), pady=(5, 5), side=TOP, anchor=NW)

# Opens a form to insert a new asset
def newAssetForm():
    clearTable()

    def insertAssetOnClick():
        if oDef.get() == "Select an OS" or not pounds.get().isdigit() or \
        not pence.get().isdigit() or notes.get() == "" or name.get() == "" or \
        model.get() == "" or manufacturer.get() == "" or tDef.get() == "Select a Type" or \
        IP.get() == "" or not ram.get().isdigit() or not storage.get().isdigit() or \
        eDef.get() == "Select an Employee":
            errorLabel = Label(table, text="Something isn't right! Please take a look over the form and try again.", fg = "red")
            errorLabel.grid(column = 0, row = 13)
        else:
            db.createAsset(oDef.get(), cal.get_date(), pounds.get() + "." + pence.get(),
            notes.get(), name.get(), model.get(), manufacturer.get(), tDef.get(), IP.get(),
            ram.get(), storage.get(), eDef.get())
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

    db.readEmployee(None, None)
    employeesList = []
    for x in db.readResult:
        employeesList.append(x[0])
    employeeLabel = Label(table, text="Employee")
    employeeLabel.grid(column=0,row=11)
    eDef = StringVar(value="Select an Employee")
    employee = OptionMenu(table, eDef, *employeesList)
    employee.grid(column=1,row=11)

    autoBtn = Button(table, text="Use Current Device", command=detectCurrentDevice)
    autoBtn.grid(column=0, row=12)

    submitBtn = Button(table, text="Submit", command=insertAssetOnClick)
    submitBtn.grid(column=1, row=12)

# Opens a form to insert a new employee
def newEmployeeForm():
    clearTable()
    def insertEmployeeOnClick():
        deparment = 5
        dupeEmail = 0
        if dDef.get() == "Finance":
            deparment = 0
        elif dDef.get() == "Human Resources":
            deparment = 1
        elif dDef.get() == "Operations":
            deparment = 2
        elif dDef.get() == "Sales":
            deparment = 3
        elif dDef.get() == "Information Technology":
            deparment = 4

        db.readEmployee(None, None)
        for x in db.readResult:
            if x[0] == email.get():
                dupeEmail = 1
        if deparment == 5 or dupeEmail == 1:
            errorLabel = Label(table, text="Something isn't right! Please take a look over the form and try again.", fg = "red")
            errorLabel.grid(column = 0, row = 12)
        else:
            db.createEmployee(deparment, email.get(), fName.get(), lName.get())
            refreshButtonOnClick()

    fNameLabel = Label(table, text="First Name")
    fNameLabel.grid(column=0,row=0)
    fName = Entry(table)
    fName.grid(column=1,row=0)

    lNameLabel = Label(table, text="Last Name")
    lNameLabel.grid(column=0,row=1)
    lName = Entry(table)
    lName.grid(column=1,row=1)

    emailLabel = Label(table, text="Email")
    emailLabel.grid(column=0,row=2)
    email = Entry(table)
    email.grid(column=1,row=2)

    DepartmentLabel = Label(table, text="Department")
    DepartmentLabel.grid(column=0,row=3)
    deps = ["Finance", "Human Resources", "Operations", "Sales", "Information Technology"]
    dDef = StringVar(value="Select a Department")
    dType = OptionMenu(table, dDef, *deps)
    dType.grid(column=1,row=3)

    submitBtn = Button(table, text="Submit", command=insertEmployeeOnClick)
    submitBtn.grid(column=1, row=4)


# --------------------
#     MAIN WINDOW
# --------------------

root = Tk()
menubar = Menu(root)
root.config(menu = menubar)
root.title("Asset Tracker")
root.geometry("1500x750")
table = Frame(root, bg="white")

# Adding Assets Menu and Commands
assets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='󰍹   Assets', menu = assets)
assets.add_command(label ='New', command = newAssetForm)
assets.add_command(label ='Update', command = updateAssetForm)
assets.add_command(label ='Remove', command = None)

# Adding Employees Menu and Commands
employees = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='   Employees', menu = employees)
employees.add_command(label ='New', command = newEmployeeForm)
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