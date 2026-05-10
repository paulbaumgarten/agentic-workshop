import os
import psycopg2

conn = psycopg2.connect(
    os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/workshopdb")
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

cur.close()
conn.close()
