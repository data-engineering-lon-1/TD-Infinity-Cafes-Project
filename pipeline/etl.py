from pipeline.extract import read_unf_csv
from pipeline.transform import transform_rows
from pipeline.load import load_by_row

def etl():
    data = read_unf_csv('C:/Users/mylaptop/final_proj/Team-NicSquared/mainfile.csv')
    t_data = transform_rows(data)
    load_by_row(t_data)

etl()