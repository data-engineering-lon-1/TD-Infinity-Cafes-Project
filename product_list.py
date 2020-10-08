import csv
import pprint
import uuid
import pandas as pd
import numpy
 
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

#  for working out daily total:
#     daily_total(csvfile):
#         total = 0
#         x=read transaction from csv(csvfile)
#         for row in x:
#             x += int(row[2])
#     return x
# 


products = read_orders_from_csv('mainfile.csv')
pprint.pp(products)
#print(pd.DataFrame.from_dict(menu_p))


