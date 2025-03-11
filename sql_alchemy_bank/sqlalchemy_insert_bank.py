from database_definition import Client, Account, Transaction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

with open("../moje_heslo.txt", "r") as file:
    password = file.read()

eng = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/bank')


Session = sessionmaker(bind=eng)
session = Session()

session.add_all(
    [
        #Account(account_number="987654321/0800", account_type="spořící účet", client_id=3),
        #Account(account_number="987655454/0800", account_type="běžný účet", client_id=1),
        #Account(account_number="443254321/0800", account_type="běžný účet", client_id=2)
    ]
)

result = session.query(Client.accounts)
for client in result:
    print(client)
#session.commit()