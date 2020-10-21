#from pipeline.extract import read_unf_csv
from pipeline.transform import transform_rows
from pipeline.load import load_by_row
from lambda_f import read_data_from_s3

def etl():
    data = read_data_from_s3()
    t_data = transform_rows(data)
    load_by_row(t_data)

etl()