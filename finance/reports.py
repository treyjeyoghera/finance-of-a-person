import matplotlib.pyplot as plt
from models import Transaction,  Location, Investment
from cli import cli
import click
from sqlalchemy.orm import sessionmaker
from db import engine

Session = sessionmaker(bind=engine)

@cli.command()
def generate_report():
    session = Session()

    transactions = session.query(Transaction).all()

    total_expenses = sum(tr.amount for tr in transactions if tr.amount < 0)

    total_fare = sum(tr.fare for tr in session.query(Location).all())

    total_investments = sum(inv.amount for inv in session.query(Investment).all())

    income = sum(tr.amount for tr in transactions if tr.amount > 0)
    net_income = income - total_expenses

    click.echo(f"Total Expenses: {total_expenses}")
    click.echo(f"Total Fare: {total_fare}")
    click.echo(f"Total Investments: {total_investments}")
    click.echo(f"Net Income: {net_income}")

    session.close()

if __name__ == "__main__":
    cli()
