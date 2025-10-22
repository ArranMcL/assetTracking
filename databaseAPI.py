import mysql.connector 

#Database Connection
DB = mysql.connector.connect(
  host="lochnagar.abertay.ac.uk",
  user="sql2300317",
  password="podcast-into-colour-assume",
  database="sql2300317"
)
#Most recent Select Result
selectResult = ""

#ASSETS
def insertAsset(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12):
    mycursor = DB.cursor()

    sql = "INSERT INTO atAsset (ID, OS, purchaseDate, purchasePrice, notes, sysName, model, manufacturer, deviceType, IP, ram, storage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12)
    mycursor.execute(sql, val)
    DB.commit()

    print(mycursor.rowcount, "record inserted.")

def selectAsset(field, where):
    mycursor = DB.cursor()

    if field or where is None:
        sql = "SELECT * FROM atAsset"
    else:
        sql = "SELECT * FROM atAsset WHERE " + field + " = '" + where + "'"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    selectResult = myresult