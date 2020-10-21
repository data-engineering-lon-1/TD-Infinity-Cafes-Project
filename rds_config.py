#config file containing credentials for RDS MySQL instance
rds_endpoint  = os.environ.get('RDS_endpoint')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
db_name = "Transactions_Prod" 
db_con = None
