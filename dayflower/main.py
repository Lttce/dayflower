import psycopg2.extras
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

import db.util

api = FastAPI()


class User(BaseModel):
    user_id: str
    name: str
    bio: str


@api.get("/")
async def get_root():
    return {"message": "Hello World"}


@api.get("/api/v1/users/")
async def get_users() -> psycopg2.extras.Json:
    with db.util.get_connection() as conn:
        with conn.cursor("all", cursor_factory=RealDictCursor) as cur:
            cur.execute("select * from users;")
            all_row = cur.fetchall()
    return all_row


@api.post("/api/v1/user/")
async def add_user(user: User) -> User:
    with db.util.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "insert into users(id, name, bio) values (%s, %s, %s);",
                (user.user_id, user.name, user.bio),
            )
            # TODO: exception handling
    return user
