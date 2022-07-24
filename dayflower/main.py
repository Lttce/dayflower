from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
import db.util


api = FastAPI()


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/users")
async def read_users():
    with db.util.get_connection() as conn:
        with conn.cursor("all", cursor_factory=RealDictCursor) as cur:
            cur.execute("select * from users;")
            all_row = cur.fetchall()
    return all_row
