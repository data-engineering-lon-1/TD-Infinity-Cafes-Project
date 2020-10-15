import csv

def read_unf_csv(csv_file):
    extracted_data =[]
    with open(csv_file, 'r', newline='\n') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            extracted_data.append(row)
    
    
    
    return extracted_data
