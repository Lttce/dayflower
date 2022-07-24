import os
import psycopg2
import dotenv


def test_db_connection():
    dotenv.load_dotenv()
    with psycopg2.connect(
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host="localhost",
        port=os.environ.get("DB_PORT"),
        options=f"-c search_path={os.environ.get('DB_SCHEMA')}",
    ) as conn:
        with conn.cursor("test") as cur:
            cur.execute("select 1;")
            assert conn.closed == 0
