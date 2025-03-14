from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Relationship
from sqlalchemy import Column, String, Integer, Date, DateTime, Float
from datetime import datetime


with open("../moje_heslo.txt", "r") as file:
    password = file.read()


base = declarative_base()

class Client(base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(100), nullable=False)
    date_birth = Column(Date, nullable=False)
    accounts = relationship("Account")


class Account(base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_number = Column(String(30), nullable=False)
    account_type = Column(String(30), nullable=False)
    client_id = Column(Integer, ForeignKey(column="clients.id", ondelete="CASCADE"))  # column určuje jaký sloupec v jaké databázi to bere. ondelete CASCADE pri smazani klienta smaze vsechny ostatni ucty klienta

    def __repr__(self):
        return f"cislo uctu: {self.account_number}, typu uctu: {self.account_type}"
class Transaction(base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    acc_num_out = Column(Integer, ForeignKey(column="accounts.id"))
    acc_num_in = Column(Integer, ForeignKey(column="accounts.id"))
    transaction_time = Column(DateTime, nullable=False, default=datetime.now)




