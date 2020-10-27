import time
import numpy as np

#REMOVING PII FROM EACH ROW IN THE EXTRACTED DATA
def transform_row(row):
    clean = []
    item = []
    #CONVERTING DATE TIME FORMAT TO EPOCH
    d_time = int(time.mktime(time.strptime(row[0], "%Y-%m-%d %H:%M:%S")))
    #ASSIGNING ROW[3] TO VARIABLE AND SPLITTING THE "BASKET" ROW INTO ITS INDIVIDUAL PRODUCTS,
    #LEN(BASKET) IS DIVIDED BY 3 BECAUSE EACH PRODUCT HAS 3 COMPONENTS (SIZE,NAME,PRICE)
    basket = row[3].split(",")
    items = np.array_split(basket, len(basket) / 3)
    # CREATE DICT IDENTIFYING VALUES OF EACH PRODUCT IN THE BASKET BY ASSIGNING THEM TO KEYS FOR REFERENCE LATER
    for part in items:

        item.append({"size": str(part[0]), "name": str(part[1]), "price": part[2]})
    #PUTTING TOGETHER ALL CLEANED DATA INTO ONE LIST
    clean = [d_time, row[1], item, row[4], row[5]]

    return clean


def transform_rows(data):
    cleaned_rows = []
    #TRANSFORMING EACH ROW IN THE DATA ONE BY ONE THEN ADDING IT TO THE EMPTY LIST
    for row in data:
        cleaned_rows.append(transform_row(row))

    return cleaned_rows
