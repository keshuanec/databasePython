"""
vyber bookings, ktere maji vyssi hodnotu nez 500 (total_amount)
"""

from mysql.connector import connect

with open("moje_heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password, database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bookings WHERE total_amount > 500")
        print(cursor.fetchall())