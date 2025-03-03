from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

try:
    with connect(host="localhost", user='root', password=password) as conn:
        # create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"
        show_databases = "SHOW DATABASES;"
        with conn.cursor() as cursor:
            cursor.execute(show_databases)
            print(cursor.fetchall())

except Error as e:
    print(e)