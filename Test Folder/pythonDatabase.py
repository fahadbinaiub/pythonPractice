import psycopg2
print("Welcome to demo database!!!")

from config import config
connection = psycopg2.connect(host="localhost", port="5432", database="master",
                              user="postgres", password="hello")
def connect():
    connection = None
    params = config()
    print('Connecting to server.....')
    connection = psycopg2.connect(**params)

    crsr = connection.cursor()
    print('Postgres SQL version ')
    crsr.execute("Select version()")
    db_version = crsr.fetchone()
    print(db_version)

connect()
