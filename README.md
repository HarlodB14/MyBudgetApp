# MyBudgetApp
Personal Budgeting tool

## Overview
MyBudgetApp is a simple personal budgeting application with base classes for managing personal finances. The application provides a foundation for tracking income, expenses, and budgets across different categories and accounts.

## Base Classes

### User
Represents a user of the budgeting system with basic profile information.

### Account  
Represents financial accounts (checking, savings, credit cards, cash) with balance tracking.

### Category
Represents spending/income categories for organizing transactions with budget limits.

### Transaction
Represents individual financial transactions (income or expenses) with categorization.

### Budget
Represents the main budget container that manages categories, transactions, and accounts for a specific period.

## Quick Start

```python
from budget_app import User, Account, Category, Transaction, Budget

# Create a user
user = User("john_doe", "john@example.com", "John", "Doe")

# Create accounts
checking = Account("Checking Account", "checking", 1000.0)

# Create categories
food = Category("Food", "expense", 500.0, "Monthly food budget")

# Create transactions
expense = Transaction(50.0, "Grocery shopping", "expense", "Food", "Checking Account")

# Create and manage budget
budget = Budget("Monthly Budget", "monthly")
budget.accounts.append(checking)
budget.categories.append(food)
budget.transactions.append(expense)
```

## Example Usage
See `example.py` for a comprehensive demonstration of the base classes in action.
