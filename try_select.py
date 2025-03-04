from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

try:
    with connect(host="localhost", user='root', password=password, database="online_movie_rating") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM movies")
        result = cursor.fetchall()
        for row in result:
            print(*row)

except Error as e:
    print(e)



