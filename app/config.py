import os, json

with open(os.environ['DB_CRED_FILE_PATH']) as f:
  cred = json.load(f)

with open(os.environ['DB_CONNECTION_FILE_PATH']) as f:
  conn = json.load(f)

DB_STRING = "mysql+pymysql://"+cred["username"]+":"+cred["password"]+"@"+conn["primary_endpoint"]+"/"+conn["db_name"]+"?charset=utf8mb4"