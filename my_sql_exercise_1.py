from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()
try:
    with connect(host="localhost", user='root', password=password) as conn:
        show_databases = "SHOW DATABASES;"
        with conn.cursor() as cursor:
            cursor.execute(show_databases)
            print(cursor.fetchall())


except Error as e:(
    print(e))