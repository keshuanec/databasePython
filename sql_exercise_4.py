"""
Úkol 4
Napište funkci get_instruments_count, která zobrazí počet nástrojů pro každou kategorii. Funkce by měla jako argument
přijmout spojení. Vrátí záznamy tvořené slovníky se dvěma klíči - 'family' a 'count'. Ukázka volání funkce:

...
result = get_instruments_count(connection)
print(result)
({'family': 'keyboard', 'count': 2}, ...)
Nápověda
Chcete-li získat výsledek ve formě slovníků, použijte při vytváření kurzoru třídu DictCursor.
"""
from mysql.connector import connect

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

conn = connect(host="localhost", user='root', password=password, database="music")
def get_instruments_count(connection):
    get_count_sql = """SELECT family, count(*) as count FROM instruments GROUP BY family;"""

    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_count_sql)
    result = cursor.fetchall()
    return result

print(get_instruments_count(conn))
