import mysql.connector 

#Database Connection
DB = mysql.connector.connect(
  host="lochnagar.abertay.ac.uk",
  user="sql2300317",
  password="podcast-into-colour-assume",
  database="sql2300317"
)

#Most recent Select Result
readResult = []

#ASSET CRUD
def createAsset(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12):
    mycursor = DB.cursor()
    sql = "INSERT INTO atAsset (ID, sysName, model, manufacturer, OS, purchaseDate, purchasePrice, notes, deviceType, IP, ram, storage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12)
    mycursor.execute(sql, val)
    DB.commit()
    
def readAsset(field, where):
    global readResult
    mycursor = DB.cursor()

    if field is None and where is None:
        mycursor.execute("SELECT * FROM atAsset")
    else:
        sql = f"SELECT * FROM atAsset WHERE {field} = %s"
        mycursor.execute(sql, (where,))

    readResult = mycursor.fetchall()

def updateAsset(setF, setV, whereF, whereV):
    mycursor = DB.cursor()
    sql = "UPDATE atAsset SET %s = %s WHERE %s = %s"    
    val = (setF, setV, whereF, whereV)
    mycursor.execute(sql, val)
    DB.commit()

#EMPLOYEE CRUD
def createEmployee(v1, v2, v3, v4):
    mycursor = DB.cursor()
    sql = "INSERT INTO atEmployee (depID, email, fName, lName) VALUES (%s, %s, %s, %s)"
    val = (v1, v2, v3, v4)
    mycursor.execute(sql, val)
    DB.commit()
    
def readEmployee(field, where):
    global readResult
    mycursor = DB.cursor()

    if field is None and where is None:
        mycursor.execute("SELECT * FROM atEmployee")
    else:
        sql = f"SELECT * FROM atEmployee WHERE {field} = %s"
        mycursor.execute(sql, (where,))

    readResult = mycursor.fetchall()

def updateEmployee(setF, setV, whereF, whereV):
    mycursor = DB.cursor()
    sql = "UPDATE atEmployee SET %s = %s WHERE %s = %s"    
    val = (setF, setV, whereF, whereV)
    mycursor.execute(sql, val)
    DB.commit()