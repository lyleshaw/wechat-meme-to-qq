import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
env_dist = os.environ
CQ_API_URL = env_dist.get("CQ_API_URL")
SQL_USER = env_dist.get("SQL_USER")
SQL_PASS = env_dist.get("SQL_PASS")
SQL_DB = env_dist.get("SQL_DB")
SQL_HOST = env_dist.get("SQL_HOST")
SQL_PORT = env_dist.get("SQL_PORT")
SQL_URL: str = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (SQL_USER, SQL_PASS, SQL_HOST, SQL_PORT, SQL_DB)
