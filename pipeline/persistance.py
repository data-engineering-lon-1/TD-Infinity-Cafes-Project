import mysql.connector
import os

from dotenv import load_dotenv
load_dotenv()


def connection(database: str):
    port = os.environ.get("mysql_port")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_password")
    try:
        return mysql.connector.connect(
        port=port, user=user, password=password, database=database
        )
    except:
        print("DB Error, Database not found")

def update(sql, data):
    mydb = connection("CapsuleCorp")
    mycursor = mydb.cursor()
    mycursor.execute(sql, data)
    mydb.commit()
    mycursor.close()
    mydb.close()

def query(sql):
    mydb = connection("CapsuleCorp")
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    query = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return query

# def populate_prod_tbl(thelist):

#     mydb = connection("CapsuleCorp")
#     mycursor = mydb.cursor()
#     uploadProductQuery = "INSERT INTO Product (id, size, item, price) VALUES (%s, %s, %s, %s)"

#     mycursor.executemany(uploadProductQuery, thelist)
#     mydb.commit()

#     mycursor.close()
#     mydb.close()

# def remove_duplicates_from_table():
#     mydb = connection("CapsuleCorp")
#     mycursor = mydb.cursor()
#     removeDupProductQuery = """WITH cte AS (
#         SELECT
#         id, size, item, price, 
#         ROW_NUMBER() OVER(
#             PARTITION BY
#             size, item, price
#             ORDER BY
#             size, item, price
#         ) row_num
#         FROM
#         Product
#         )
#         DELETE FROM cte
#         WHERE row_num > 1; """

#     mycursor.execute(removeDupProductQuery, multi=True)
#     mydb.commit()
#     mycursor.close()
#     mydb.close()



# """CREATE TABLE tmp SELECT id, size, item, price 
#     FROM Product;
#     GROUP BY(size, item, price);
#     DROP TABLE Product;
#     ALTER TABLE tmp RENAME TO Product; """


# """insert ignore"""
