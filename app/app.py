import os
import psycopg2
from flask import Flask

app = Flask(__name__)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/workshopdb"
)

@app.route("/")
def home():
    return "Hello from Agentic Workshop"

@app.route("/db-check")
def db_check():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT current_database();")
    db = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"Connected to database: {db}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
