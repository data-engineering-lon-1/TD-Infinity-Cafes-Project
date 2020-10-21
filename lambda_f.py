import json
import boto3
import sys
import csv
import pymysql
import os
import logging
import uuid
from pipeline.persistance import query, update
from pipeline.transform import transform_rows, transform_row, data

def read_data_from_s3(event):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_and_key = event["Records"][0]["s3"]["object"]["key"]
    s3 = boto3.client("s3")
    all_s3_objects = s3.list_objects(Bucket = 'bucket-name') 
    
    
    get_extracted_date = s3_client.get_object(Bucket=bucket, Key=s3_and_key)
    data = extracted_data['Body'].read().decode('unt-8').split("\n")
    
    extracted_data =[]
    
    reader = csv.reader(data)
    for row in reader:
        extracted_data.append(row)
    
    return extracted_data

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def connect_to_rds():
        rds_endpoint  = os.environ.get('RDS_endpoint')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASS')
        db_name = "Transactions_Prod" 
        db_con = None

        try:
            db_connection = pymysql.connect(rds_endpoint, user=db_user, passwd=db_password, db=db_name, connect_timeout=10)
            
        except pymysql.MySQLError as e:
            logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
            logger.error(e)
            sys.exit()
            
        logger.info("SUCCESSFUL: Connected to MySQL instance")

        return db_connection

def load_location_row_handler(row, event, context):

    l_id = None
    location_name = row[1]
    checkDbQuery = f"""SELECT id from Location WHERE l_name ='{location_name}'"""
    updateDbQuery = "INSERT INTO Location (id, l_name) VALUES (%s, %s)"

    check = query(checkDbQuery)

    if len(check) == 0:
        l_id = str(uuid.uuid4())
        update(updateDbQuery, (l_id, location_name))
    else:
        l_id = check[0][0]
    
    return l_id            

def load_transaction_row_handler(row, l_id, event, context):

    updateDbQuery = "INSERT INTO Transaction (id, date_time, l_id, payment_type, total) VALUES (%s, %s, %s, %s, %s)"
    tsac_id = str(uuid.uuid4())
    date_time = row[0]
    payment_type = row[3]
    total = row[4]

    update(updateDbQuery, (tsac_id, date_time, l_id, payment_type, float(total)))

    return tsac_id

def load_product_row(row, event, context):
    p_id = None
    updateDbQuery = """INSERT INTO Product ( id, size, name, price) VALUES (%s, %s, %s, %s)"""
    id_dict = {}
    basket = row[2]

    for product in basket:
        size = product['size']
        name = product['name']
        price = float(product['price'])
        checkDbQuery = f"SELECT id from Product WHERE size ='{size}' AND name ='{name}' AND price ={price}"
        check = query(checkDbQuery)
        if len(check) == 0:
            p_id = str(uuid.uuid4())
            update(updateDbQuery, (p_id, size, name, price))
        else:
            p_id = check[0][0]
        prod = {p_id: price}
        id_dict.update(prod)
        
    return id_dict


def load_orders_row(d_time, tsac_id, p_id, price,event, context):
    updateDbQuery = "INSERT INTO Orders (date_time, tsac_id, prod_id, price) VALUES (%s, %s, %s, %s)"

    update(updateDbQuery, (d_time, tsac_id, p_id, price))

def load_by_row(t_data):

    for row in t_data:

        date = row[0]
        l_id = load_location_row(row)
        tsac_id = load_transaction_row(row, l_id)
        id_list = load_product_row(row)

        for p_id, price in id_list.items():

            load_orders_row(date, tsac_id, p_id, price)