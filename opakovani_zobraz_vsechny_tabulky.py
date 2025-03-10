"""dejte print vsech tabulek v databazi car_rental. Databazi definujte v connect funkci. Prikaz na to je
SHOW TABLES"""


from mysql.connector import connect
with open("moje_heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password, database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())

