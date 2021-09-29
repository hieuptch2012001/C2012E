import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres', password='hieu111299'
)

conn.autocommit = True

cursor = conn.cursor()

sql = '''CREATE DATABASE mydb'''
        
cursor.execute(sql)
print("Database created successfully.........")

conn.close()
