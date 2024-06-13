from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Account, Transaction, Location, Investment
from datetime import datetime

#engine to connect to the database
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

# Create a Session class to interact with the database
Session = sessionmaker(bind=engine)


# Define a function to add a user

def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username=username, password=password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    print("User added successfully.")

# Define a function to add an account
def add_account():
    user_id = int(input("Enter user ID: "))
    name = input("Enter account name: ")
    balance = float(input("Enter account balance: "))
    account = Account(user_id=user_id, name=name, balance=balance)
    session = Session()
    session.add(account)
    session.commit()
    session.close()
    print("Account added successfully.")

# Define a function to add a location
def add_location():
    name = input("Enter location name: ")
    fare = int(input("Enter fare: "))
    distance = int(input("Enter distance: "))
    bankname = input("Enter bank name: ")
    location = Location(name=name, fare=fare, distance=distance, bankname=bankname)
    session = Session()
    session.add(location)
    session.commit()
    session.close()
    print("Location added successfully.")

# Define a function to add a transaction
def add_transaction():
    account_id = int(input("Enter account ID: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    description = input("Enter description: ")
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))
    transaction = Transaction(account_id=account_id, date=date, description=description, category=category, amount=amount)
    session = Session()
    session.add(transaction)
    session.commit()
    session.close()
    print("Transaction added successfully.")

# function to add an investment
def add_investment():
    account_id = int(input("Enter account ID: "))
    name = input("Enter investment name: ")
    amount = int(input("Enter investment amount: "))
    investment = Investment(account_id=account_id, name=name, amount=amount)
    session = Session()
    session.add(investment)
    session.commit()
    session.close()
    print("Investment added successfully.")

#  the main CLI loop
def main():
    while True:
        print("1. Add User")
        print("2. Add Account")
        print("3. Add Location")
        print("4. Add Transaction")
        print("5. Add Investment")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            add_account()
        elif choice == '3':
            add_location()
        elif choice == '4':
            add_transaction()
        elif choice == '5':
            add_investment()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
