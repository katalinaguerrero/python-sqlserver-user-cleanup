from dotenv import load_dotenv
import os
load_dotenv()  # carga .env en os.environ

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CSV_PATH = os.path.join(BASE_DIR, "data", "valid_users.csv")


DB_CONFIG = {
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "driver": os.getenv("DB_DRIVER", "{ODBC Driver 17 for SQL Server}")
}
