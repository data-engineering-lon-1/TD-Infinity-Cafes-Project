from pipeline.extract import read_unf_csv
import numpy as np
import pprint
import time

data = read_unf_csv('mainfile.csv')
def transform_row(row):
        clean = []
        item = []
        d_time = int(time.mktime(time.strptime(row[0], "%Y-%m-%d %H:%M:%S")))
        basket = row[3].split(',')
        items = np.array_split(basket, len(basket)/3)

        for part in items:
            
            item.append({'size':part[0], 'name':part[1], 'price':part[2]})
                     
        clean =[d_time,row[1], item, row[4], row[5]]

        return clean 

def transform_rows(data):
    cleaned_rows = []

    for row in data:
        cleaned_rows.append(transform_row(row))

    return cleaned_rows
#pprint.pprint(transform_rows(data))

