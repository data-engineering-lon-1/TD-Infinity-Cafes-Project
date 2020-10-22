import os
import pymysql
import sys
import logger

from dotenv import load_dotenv
load_dotenv()

def connect_to_rds():
    rds_endpoint  = os.environ.get('RDS_endpoint')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASS')
    db_name = "Transactions_Prod" 

    try:
        db_connection = pymysql.connect(rds_endpoint, user=db_user, passwd=db_password, db=db_name, connect_timeout=10)
        
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()
        
    logger.info("SUCCESSFUL: Connected to MySQL instance")

    return db_connection

def update(sql, data):
    mydb = connect_to_rds()
    mycursor = mydb.cursor()
    mycursor.execute(sql, data)
    mydb.commit()
    mycursor.close()
    mydb.close()

def query(sql):
    mydb = connect_to_rds()
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
