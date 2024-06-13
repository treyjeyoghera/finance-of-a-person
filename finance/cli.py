import click
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,User,Location,Account,Transaction

engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass
@cli.command()
def create_user():
    username = click.prompt("Enter username")
    password = click.prompt("Enter password", hide_input=True, confirmation_prompt=True)
    
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    click.echo("User created successfully")

@cli.command()
def create_account():
    
    name = click.prompt("Enter account name")
    balance = click.prompt("Enter initial balance", type=float)
    user_id = click.prompt("Enter user ID")
    
    account = Account(name=name, balance=balance, user_id=user_id)
    session.add(account)
    session.commit()
    click.echo("Account created successfully")

@cli.command()

def create_transaction():
    date = click.prompt("Enter transaction date (YYYY-MM-DD)")
    description = click.prompt("Enter transaction description")
    category = click.prompt("Enter transaction category")
    amount = click.prompt("Enter transaction amount", type=float)
    account_id = click.prompt("Enter account ID")
    
    transaction = Transaction(date=date, description=description, category=category, amount=amount, account_id=account_id)
    session.add(transaction)
    session.commit()
    click.echo("Transaction created successfully")
@cli.command()
def create_location():
    name = click.prompt("Enter location name")
    fare = click.prompt("Enter fare", type=float)
    distance = click.prompt("Enter distance", type=float)
    bankname = click.prompt("Enter bank name")
    
    location = Location(name=name, fare=fare, distance=distance, bankname=bankname)
    session.add(location)
    session.commit()
    click.echo("Location created successfully")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()
