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
            #print(part)
            item.append({'size':part[0], 'name':part[1], 'price':part[2]})
            #item.update 
            #print(item)          
        clean =[d_time,row[1], item, row[4], row[5]]
        #print(clean[2['size']])
        return clean 

def transform_rows(data):
    
    cleaned_rows = []
    for row in data:
        cleaned_rows.append(transform_row(row))

    return cleaned_rows
#     #print(cleaned_row)
#     product_list=[]
#     for row in cleaned_row:
#             basket = row[2].split(',')
#             product_list.append(basket)

#     for item in product_list:
#             product = [item[0], item[1], item[2]]

#     return [cleaned_row[0:2], product, cleaned_row[-2:]]




#pprint.pprint(transform_rows(data))

t_rows = transform_rows(data)
single_row = t_rows[2]
basket = single_row[2]
print(basket)
# #print(p[0]['name'])
newDict = {}

"""for p in basket:
    newDict.update(p)

prod =newDict

print(prod) """

for p in basket:
    for idx in range(0, len(basket)-1):
        newDict.update(p[idx])
    
prod =newDict


# print(p['price'])
#transform_rows(data)