from src.transform import transform_rows
from src.load import load_by_row
from src.extract import read_data_from_s3

def etl(event, context):
    data = read_data_from_s3(event)
    t_data = transform_rows(data)
    load_by_row(t_data)