from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Account, Transaction, Location, Investment
from datetime import datetime

# Engine to connect to the database
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

# Create a Session class to interact with the database
Session = sessionmaker(bind=engine)

#  a function to add a user
def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username=username, password=password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    print("User added successfully.")

#  a function to update a user
def update_user():
    user_id = int(input("Enter user ID to update: "))
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        user.username = username
        user.password = password
        session.commit()
        print("User updated successfully.")
    else:
        print("User not found.")
    session.close()

#  a function to delete a user
def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")
    session.close()

#  a function to add an account
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

#  a function to update an account
def update_account():
    account_id = int(input("Enter account ID to update: "))
    session = Session()
    account = session.query(Account).filter(Account.id == account_id).first()
    if account:
        name = input("Enter new account name: ")
        balance = float(input("Enter new account balance: "))
        account.name = name
        account.balance = balance
        session.commit()
        print("Account updated successfully.")
    else:
        print("Account not found.")
    session.close()

#  a function to delete an account
def delete_account():
    account_id = int(input("Enter account ID to delete: "))
    session = Session()
    account = session.query(Account).filter(Account.id == account_id).first()
    if account:
        session.delete(account)
        session.commit()
        print("Account deleted successfully.")
    else:
        print("Account not found.")
    session.close()

# Define a function to add a location
def add_location():
    name = input("Enter location name: ")
    fare = float(input("Enter fare: "))
    distance = float(input("Enter distance: "))
    bankname = input("Enter bank name: ")
    location = Location(name=name, fare=fare, distance=distance, bankname=bankname)
    session = Session()
    session.add(location)
    session.commit()
    session.close()
    print("Location added successfully.")

#  a function to update a location
def update_location():
    location_id = int(input("Enter location ID to update: "))
    session = Session()
    location = session.query(Location).filter(Location.id == location_id).first()
    if location:
        name = input("Enter new location name: ")
        fare = float(input("Enter new fare: "))
        distance = float(input("Enter new distance: "))
        bankname = input("Enter new bank name: ")
        location.name = name
        location.fare = fare
        location.distance = distance
        location.bankname = bankname
        session.commit()
        print("Location updated successfully.")
    else:
        print("Location not found.")
    session.close()

#  a function to delete a location
def delete_location():
    location_id = int(input("Enter location ID to delete: "))
    session = Session()
    location = session.query(Location).filter(Location.id == location_id).first()
    if location:
        session.delete(location)
        session.commit()
        print("Location deleted successfully.")
    else:
        print("Location not found.")
    session.close()

#  a function to add a transaction
def add_transaction():
    account_id = int(input("Enter account ID: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    description = input("Enter description: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    transaction = Transaction(account_id=account_id, date=date, description=description, category=category, amount=amount)
    session = Session()
    session.add(transaction)
    session.commit()
    session.close()
    print("Transaction added successfully.")

#  a function to update a transaction
def update_transaction():
    transaction_id = int(input("Enter transaction ID to update: "))
    session = Session()
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        date_str = input("Enter new date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        description = input("Enter new description: ")
        category = input("Enter new category: ")
        amount = float(input("Enter new amount: "))
        transaction.date = date
        transaction.description = description
        transaction.category = category
        transaction.amount = amount
        session.commit()
        print("Transaction updated successfully.")
    else:
        print("Transaction not found.")
    session.close()

#  a function to delete a transaction
def delete_transaction():
    transaction_id = int(input("Enter transaction ID to delete: "))
    session = Session()
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        session.delete(transaction)
        session.commit()
        print("Transaction deleted successfully.")
    else:
        print("Transaction not found.")
    session.close()

#  a function to add an investment
def add_investment():
    account_id = int(input("Enter account ID: "))
    name = input("Enter investment name: ")
    amount = float(input("Enter investment amount: "))
    investment = Investment(account_id=account_id, name=name, amount=amount)
    session = Session()
    session.add(investment)
    session.commit()
    session.close()
    print("Investment added successfully.")

#  a function to update an investment
def update_investment():
    investment_id = int(input("Enter investment ID to update: "))
    session = Session()
    investment = session.query(Investment).filter(Investment.id == investment_id).first()
    if investment:
        name = input("Enter new investment name: ")
        amount = float(input("Enter new investment amount: "))
        investment.name = name
        investment.amount = amount
        session.commit()
        print("Investment updated successfully.")
    else:
        print("Investment not found.")
    session.close()

#  a function to delete an investment
def delete_investment():
    investment_id = int(input("Enter investment ID to delete: "))
    session = Session()
    investment = session.query(Investment).filter(Investment.id == investment_id).first()
    if investment:
        session.delete(investment)
        session.commit()
        print("Investment deleted successfully.")
    else:
        print("Investment not found.")
    session.close()

# The main CLI loop
def main():
    while True:
        print("\nMain Menu:")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Add Account")
        print("5. Update Account")
        print("6. Delete Account")
        print("7. Add Location")
        print("8. Update Location")
        print("9. Delete Location")
        print("10. Add Transaction")
        print("11. Update Transaction")
        print("12. Delete Transaction")
        print("13. Add Investment")
        print("14. Update Investment")
        print("15. Delete Investment")
        print("16. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            add_account()
        elif choice == '5':
            update_account()
        elif choice == '6':
            delete_account()
        elif choice == '7':
            add_location()
        elif choice == '8':
            update_location()
        elif choice == '9':
            delete_location()
        elif choice == '10':
            add_transaction()
        elif choice == '11':
            update_transaction()
        elif choice == '12':
            delete_transaction()
        elif choice == '13':
            add_investment()
        elif choice == '14':
            update_investment()
        elif choice == '15':
            delete_investment()
        elif choice == '16':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
