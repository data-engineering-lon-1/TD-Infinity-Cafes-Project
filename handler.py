from src.transform import transform_rows
from src.load import load_by_row
from src.extract import read_data_from_s3
import json


def etl(event, context):
    data = read_data_from_s3(event)
    print("Raw", data[0])
    t_data = transform_rows(data)
    print("Transformed", t_data[0])
    load_by_row(t_data)