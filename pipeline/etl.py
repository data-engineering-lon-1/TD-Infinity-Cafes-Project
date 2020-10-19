from pipeline.extract import read_unf_csv
from pipeline.transform import transform_rows
from pipeline.load import load_by_row

def etl(csvfile):
    data = read_unf_csv(csvfile)
    t_data = transform_rows(data)
    load_by_row(t_data)

etl('mainfile.csv')