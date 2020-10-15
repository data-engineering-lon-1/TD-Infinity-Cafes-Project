import mysql.connector

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="CapsuleCorp"
)


