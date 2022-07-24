import dotenv
import psycopg2
import os
from psycopg2.extensions import connection

dotenv.load_dotenv()


def get_connection() -> connection:
    return psycopg2.connect(
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        options=f"-c search_path={os.environ.get('DB_SCHEMA')}",
    )
