import os
import random
import requests
import psycopg2
from fastapi import FastAPI

app = FastAPI()

WELCOME_URL = os.getenv("WELCOME_URL", "http://mini-demo-welcome:8081/welcome")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "mini-demo-postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "appdb")
POSTGRES_USER = os.getenv("POSTGRES_USER", "appuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "apppassword")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

def get_random_user():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT,
    )
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, email FROM users ORDER BY RANDOM() LIMIT 1;"
            )
            row = cur.fetchone()
            if not row:
                return None
            return {"id": row[0], "name": row[1], "email": row[2]}
    finally:
        conn.close()

@app.get("/api/info")
def info():
    welcome_resp = requests.get(WELCOME_URL, timeout=3)
    welcome_msg = welcome_resp.json()["message"]

    user = get_random_user()

    return {
        "service": "api-service",
        "welcome": welcome_msg,
        "user": user,
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
