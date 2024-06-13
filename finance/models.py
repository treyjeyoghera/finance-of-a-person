from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import pbkdf2_sha256 as sha256

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    accounts = relationship('Account', back_populates='user', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = sha256.hash(password)

    def verify_password(self, password):
        return sha256.verify(password, self.password_hash)

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account', cascade='all, delete-orphan')
    investments = relationship('Investment', back_populates='account', cascade='all, delete-orphan')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='transactions')

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fare = Column(Float, nullable=False)
    distance = Column(Float, nullable=False)
    bankname = Column(String, nullable=False)

class Investment(Base):
    __tablename__ = 'investments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='investments')

class Debt(Base):
    __tablename__ = 'debts'
    debt_id = Column(Integer, primary_key=True)
    name = Column(String)
    date_acquired = Column(Date)
    date_paid = Column(Date)
    phone_no = Column(String)