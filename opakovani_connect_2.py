from mysql.connector import connect
with open("moje_heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        print(cursor.fetchall())


