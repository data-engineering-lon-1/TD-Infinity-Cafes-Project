from pipeline.extract import read_unf_csv
from transform import transform_rows, transform_row
from transform import data

row = transform_rows(data)
def load_location_row(row):
    location = transform_row[1]

    sql = """INSERT INTO Location (l_name) VALUES(%s) """


def load_product_row(row):

    sql = """INSERT INTO Product ( id, size, name, price) VALUES (%s, %s, %s, %s)"""


def load_transaction_row(row):
    transaction = [row[0],row[1],row[3], row[4]]
    print(transaction)

print(load_transaction_row(row))