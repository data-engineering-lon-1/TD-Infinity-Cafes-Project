import csv
import pprint
import uuid
import pandas as pd
import numpy
from persistance import connection, populate_prod_tbl, remove_duplicates_from_table
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
# Function to convert a csv file to a list of dictionaries.  Takes in one variable called &quot;variables_file&quot;
 
# def csv_dict_list(variables_file):
     
#     # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
#     the_csv = []
#     with open(variables_file) as f:
#         cf = csv.DictReader(f, fieldnames=['Datetime', 'Location', 'Name', 'OrderList', 'Payment', 'Price', 'CardDetails'])
#         for row in cf:
#             the_csv.append(row)
    
#     return the_csv




def cleaned_cc_num(rows):
    cleaned = []
    for row in rows:
        cleaned_row = []

        last_idx = len(row) - 1

        cleaned_column = None
        
        if row[last_idx] != None:
            cleaned_column = row[last_idx].split(',')[0]
        
        for idx in range(0, last_idx - 1):
            cleaned_row.append(row[idx])
        
        cleaned_row.append(cleaned_column)

        cleaned.append(cleaned_row)
    
    return cleaned
    
def read_unf_csv(csv_file):
    unf =[]
    with open(csv_file, 'r', newline='\n') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            unf.append(row)
    
    clean_data = cleaned_cc_num(unf)
    
    return clean_data

def remove_element(thelist: list, index: int):
    nfl = []
    for row in thelist:
        del row[index]
    nfl.append(thelist)
    return nfl

def read_orders_from_csv(csv_file):

    productlist = []
    final_product_list =[]
    items=[]

    csv_file = read_unf_csv(csv_file)

    for row in csv_file:
        basket = row[3].split(',')
        productlist.append(basket)

    for item in productlist:
        product = [item[0], item[1], item[2]] # [SIZE, P_NAME, P_PRICE]
        if product not in items: # items is a list of the products before adding a unque ID,             
            items.append(product) # this check to see if the product has already been processed 
            product = [str(uuid.uuid4()),item[0], item[1], item[2]] # add Unique ID to list 
            final_product_list.append(product)
        #print(product)
    return final_product_list

#TODO 
#In order to check the for duplicates in the database, first import all the data into an array
# as done before, loop through the data you want to add and check if it already is present
#if the data is not in the database, append to the database array 
#resave in the database

secondlist = [['de48b2b8-1448-413f-a9a7-a066ae4c6edb', 'Large', 'Hot chocolate', '2.9'], ['2a941ab7-b38c-448b-99e5-bb4a52114c2d', 'Large', 'Luxury hot chocolate', '2.7'], ['6f4cc28c-d9de-4fa7-9a59-0ef672fc0241', 'Large', 'Flavoured latte - Vanilla', '2.85'], ['3d928295-748e-4cd5-8bc0-1119c71c25be', 'Large', 'Cappuccino', 
'2.45'], ['b64d2fbf-9c24-4b5b-a50b-62a3cbd2cc45', 'Regular', 'Espresso', '1.5'], ['ecd0bb50-6029-41b6-9947-c52f214f6e74', '', 'Frappes - Chocolate Cookie', '2.75'], ['78ccbf1f-85ac-4e82-98c8-3b36c5480244', '', 'Cortado', '2.05'], ['351974b5-ba4d-42ca-bc3c-a96788cff415', '', 'Speciality Tea - Earl Grey', '1.3'], ['49f8c1fe-50fb-483c-a6e8-1738db71c8c4', 'Regular', 'Flavoured hot chocolate - Caramel', '2.6'], ['6cd2b2f3-7778-44eb-ab47-3f0fd8739335', '', 'Frappes - Strawberries & Cream', '2.75'], ['619c5abe-6ac1-44e1-a092-666903c11e90', 'Regular', 'Flavoured latte - Hazelnut', '2.55'], ['8adf8ae6-35e2-4185-9cd5-7f6df557efc4', 'Large', 'Flavoured latte - Hazelnut', '2.85'], ['be6dfc9c-5e20-475b-b046-4f3e60c4767f', 'Large', 'Filter coffee', '1.8'], ['0ee00bfb-603b-47d1-943e-49322e09d5e9', 'Large', 'Flavoured hot chocolate - Vanilla', '2.9'], ['5b2a80d7-42c6-472d-8d12-8309d5f88c52', '', 'Speciality Tea - Peppermint', '1.3'], ['08ff9916-462f-4d99-b348-5923da746086', '', 'Iced latte', '2.35'], ['30b612d2-a2c8-4fab-aeca-95841792e456', '', 'Flavoured iced latte - Caramel', '2.75'], ['36d8fe0b-b8ad-47c7-9f8d-8ef6305697c3', '', 'Flat white', '2.15'], ['5aa04fb8-16a6-426b-8aaf-fdf547491ff6', '', 'Speciality Tea - English breakfast', '1.3'], ['1267d150-b842-4dd3-b0f4-fee6db20b791', '', 'Speciality Tea - Green', '1.3'], ['7d90b5db-0cda-4766-ba7d-bcfabe0885c3', '', 'Red Label tea', '1.2'], ['1665ae80-37b1-4a52-8fa7-f3989c5ce233', 'Regular', 'Latte', '2.15'], ['24ec118d-df2e-4d20-82ec-bf26a8b45b4d', 'Regular', 'Flavoured latte - Gingerbread', '2.55'], ['cbd86e47-6c8d-4d34-b425-947ff0a70c30', 'Regular', 'Flavoured hot chocolate - Vanilla', '2.6'], ['5073ff71-9564-4f89-99a5-49adac61472d', '', 'Hot Chocolate', '1.4'], ['6791c7f6-1026-4e06-8f75-00632681fe5d', 'Large', 'Chai latte', '2.6'], ['9f4a8303-94ff-44a7-9a01-0d474a520e51', '', 'Smoothies - Berry Beautiful', '2.0'], ['30c10b3f-532a-4844-99f3-5374a8f714e2', '', 'Glass of milk', '0.7'], ['06ca4f71-2e3f-4e77-87bd-6489f36c6b2c', '', 'Babyccino', '0.0'], ['365ea085-85b4-48c8-9518-f4e2fbb3e452', '', 'Iced americano', '2.15'], ['783c34c0-6fb1-41de-810f-d72f1d3739f7', 'Regular', 'Flavoured latte - Vanilla', '2.55'], ['cee6ac04-2a31-4982-a30c-300e8499ca0c', 'Regular', 'Americano', '1.95'], ['f6be167b-be13-477d-b7dd-722d77325688', 'Regular', 'Cappuccino', '2.15'], ['0c3379f0-3dfe-4460-9177-0c2ba760c4e5', '', 'Flavoured iced latte - Hazelnut', '2.75'], ['2fa9dd51-8956-415a-ba18-de80e1fa64db', 'Large', 'Latte', '2.45']]

products = read_orders_from_csv('mainfile.csv')
#print(products)
#print(pd.DataFrame.from_dict(menu_p))
#populate_prod_tbl(secondlist)
remove_duplicates_from_table()

