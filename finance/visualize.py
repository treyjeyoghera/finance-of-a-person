import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Account, Transaction, Location

engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

def visualize():
    # Example visualization (you can customize this as needed)
    account_balances = session.query(Account.balance).all()
    balances = [balance for (balance,) in account_balances]
    
    plt.figure(figsize=(10, 6))
    plt.hist(balances, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Balance')
    plt.ylabel('Frequency')
    plt.title('Account Balance Distribution')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == '__main__':
    visualize()
