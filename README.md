# Personal Finance Manager

**Author**: Treyjey Oghera  
**Date**: June 2024

## Project Name: Personal Finance Manager

The Personal Finance Manager is a Python application designed to help individuals manage their finances effectively. It provides a user-friendly Command Line Interface (CLI) that allows users to easily track their income, expenses, and financial goals.

## Features

- **User Management**: Users can create accounts and manage their personal finance data securely. Each user can create multiple accounts to track different aspects of their finances, such as savings, expenses, and investments.
- **Database Management**: The application uses Object-Relational Mapping (ORM) with SQLAlchemy to manage the database. It includes tables for users, accounts, transactions, and locations, designed to efficiently store and retrieve financial data.
- **CLI Interface**: The CLI provides a set of commands that users can use to interact with the application. Users can create new accounts, add transactions, view their financial data, and generate reports. The CLI is designed to be intuitive and easy to use, even for users who are not familiar with command-line interfaces.
- **Data Visualization**: The application can generate visualizations of financial data. Users can view their income and expenses over time, track their progress towards financial goals, and identify areas where they can save money.
- **Financial Reporting**: Detailed financial reports summarize income, expenses, and savings. These reports help users gain insights into their financial habits and make informed decisions about their finances.
- **Security**: The application prioritizes the security of user data. It uses encryption to protect sensitive information and implements best practices for data storage and access control.

## Project Structure

The project is organized into the following directories:

- `finance/`
  - `cli/`: Contains CLI-related scripts.
  - `app/`: Contains application logic.
  - `models/`: Contains database models.
  - `reports/`: Contains report generation scripts.
  - `db.py`: Main script to run the application.

Other files include:

- `Pipfile` and `Pipfile.lock`: For dependency management.
- `README.md`: This documentation file.

## Requirements

- Python 3.10 or higher
- SQLAlchemy
- Click

## Getting Started

### Installation

Clone the repository and install dependencies using Pipenv:

```sh
git clone https://github.com/yourusername/personal_finance_manager.git
cd personal_finance_manager
pipenv install
