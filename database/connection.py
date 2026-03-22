import os
import sqlite3

from dotenv import load_dotenv


load_dotenv()


def get_database_connection():
    db_name = os.getenv("DB_NAME", "marketing_pipeline.db")
    connection = sqlite3.connect(db_name)
    return connection