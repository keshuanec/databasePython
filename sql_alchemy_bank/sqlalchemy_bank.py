from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

with open("../moje_heslo.txt", "r") as file:
    password = file.read()

eng = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/')
Session = sessionmaker(bind=eng)
session = Session()

result = session.execute(text("CREATE DATABASE IF NOT EXISTS bank"))



print(result)


"""vytvorit databazi bank"""