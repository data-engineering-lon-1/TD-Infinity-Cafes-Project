import pandas as pd
import uuid
import mysql.connector
import numpy
from dotenv import load_dotenv
load_dotenv()
file_a = 'mainfile.csv'

def read_unf(csvfile):
    colnames=['date_time', 'location', 'name', 'basket', 'payment_type', 't_price', 'payment_info']
    try:
        df=pd.read_csv(csvfile, names=colnames,header=None, encoding = "utf-8")
    except:
        print("ERROR: csv file cannot be found")

    #ASSIGNING RANDOM ID'S FOR EACH TRANSACTION
    #df['tsac_id']=[uuid.uuid4() for _ in range(len(df.index))] #df.index 
    df['date_time'] = pd.to_datetime(df['date_time'])
    #df.index = df['date_time']

    return df

#SETS THE UUIDS ONCE SO ALL DATA MATCHES 
df=read_unf(file_a)

def concat(csvfile):
    #EXTRACTING THE BASKET AND SPLITTING THE CONTENTS INTO THE SEPARATE ITEMS INSIDE THE BASKET
    basket_contents=pd.concat([df[['tsac_id']], df['basket'].str.split(',', expand=True)], axis=1)

    return basket_contents

def read_basket_from_csv(csvfile):

    basket_contents=concat(csvfile)
    #MAXIMUM 5 ITEMS IN BASKET EACH ITEM IN FORM SIZE:NAME:PRICE
    basket_contents_1=basket_contents.filter(['tsac_id', 0, 1, 2])

    basket_contents_2=basket_contents.filter(['tsac_id', 3, 4, 5])
    #LINKING POSITIONS IN LIST TO THEIR CORRECT FUTURE COLUMNS
    basket_contents_2=basket_contents_2.rename(columns={3:0, 4:1, 5:2})

    basket_contents_3=basket_contents.filter(['tsac_id', 6, 7, 8])
    basket_contents_3=basket_contents_3.rename(columns={6:0, 7:1, 8:2})


    basket_contents_4=basket_contents.filter(['tsac_id', 9, 10, 11])
    basket_contents_4=basket_contents_4.rename(columns={9:0, 10:1, 11:2})


    basket_contents_5=basket_contents.filter(['tsac_id', 12, 13, 14])
    basket_contents_5=basket_contents_5.rename(columns={12:0, 13:1, 14:2})
    
    basket_contents=basket_contents_1.append([basket_contents_2, basket_contents_3, basket_contents_4, basket_contents_5], ignore_index=True)
    basket_contents=basket_contents.rename(columns={0:'size', 1:'item', 2:'price'}) #RENAME COLUMNS
    #DROP EMPTY SPACES FOR THE BASKETS WITH LESS THAN 5 ITEMS
    basket_contents=basket_contents.dropna()   
    # FOR CREATING THE ORDER TABLE MERGER
    basket_contents=basket_contents.sort_values(by=['tsac_id'])  

    basket_contents=basket_contents.reset_index(drop=True)

    return basket_contents


def prod_tbl(csvfile):
    basket_contents=read_basket_from_csv(csvfile)

    product=basket_contents.drop(['tsac_id'], axis=1)
    product=product.drop_duplicates()
    product=product.sort_values(by=['item']).reset_index(drop=True)
    product['p_id'] = [uuid.uuid4() for _ in range(len(product.index))] # product.index 
    return product    

def location_tbl(csvfile):
    
    location=df.filter(['location']).drop_duplicates()
    location=location.reset_index(drop=True)
    location.columns=['l_name']
    location['l_id']=location.index + 1    
    return location 

def transac_tbl(csvfile):

    location=location_tbl(csvfile)
    #MERGE LOCATIONS TO TRANSACTIONS SO WE CAN SPLIT TRANSACTIONS BY THE CAFE'S (IN FUTURE)
    transacs=(pd.merge(df, location, left_on='location', right_on='l_name', how='left')).drop(['location','l_name','date_time','name','basket', 'payment_info'], axis=1)
    return transacs


def order_tbl(csvfile):

    basket_contents = read_basket_from_csv(csvfile)
    product = prod_tbl(csvfile)
    
    #TABLE MERGERS
    the_orders=(pd.merge(basket_contents, product, left_on=['size','item','price'],
    right_on=['size','item','price'], how='left')).drop(['item','size','price'], axis=1)

    date_time=df.filter(['tsac_id','date_time'])
    the_orders=(pd.merge(the_orders, date_time, left_on='tsac_id', right_on='tsac_id', how='left'))

    return the_orders


print(order_tbl(file_a))
#print(prod_tbl(file_a))
#print(read_unf('mainfile.csv'))
#print(transac_tbl(file_a))

#TODO for script line 23 needs to take same argument as csvfile 


