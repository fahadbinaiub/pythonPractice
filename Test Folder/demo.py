import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "master",
    user = "postgres",
    password = "hello"
)

cur = con.cursor()

cur.execute("select * from demo")
rows = cur.fetchall()

for r in rows:
    print(f"ID {r[0]} Name {r[1]} Salary {r[2]}")
cur.close()

con.close()
