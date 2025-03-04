from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

try:
    with connect(host="localhost", user='root', password=password, database="online_movie_rating") as conn:
        # create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"
        insert_data = """
         INSERT INTO movies (title)
         VALUES
             ("Terminátor"),
             ("Vetřelci");
         """
        with conn.cursor() as cursor:
            cursor.execute(insert_data)
            conn.commit()

except Error as e:
    print(e)


