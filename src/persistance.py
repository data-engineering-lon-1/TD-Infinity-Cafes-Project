import os
import pymysql
import sys
import logging
logger = logging.getLogger()

def connect_to_rds():
    rds_endpoint = os.environ.get('RDS_ENDPOINT')
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