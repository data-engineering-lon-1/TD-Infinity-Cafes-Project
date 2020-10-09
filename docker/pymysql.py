import mysql.connector

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="firstdb"
)

print(mydb)
mycursor = mydb.cursor()

getPeopleQuery = "SELECT * FROM people"
createPersonQuery = "INSERT INTO people (forename, surname) VALUES (%s, %s)"
mycursor.execute(getPeopleQuery)
myresult = mycursor.fetchall()
print(len(myresult))

for row in myresult:
    print(row)

#mycursor.execute(createPersonQuery, ("James", "Buchanan"))

mydb.commit()
mycursor.close()
mydb.close()