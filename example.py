#!/usr/bin/env python3
"""
Example usage of MyBudgetApp classes.

This demonstrates how to use the base classes to create a simple budgeting scenario.
"""

from budget_app import User, Account, Category, Transaction, Budget
from datetime import date


def main():
    """Demonstrate basic usage of the MyBudgetApp classes."""
    print("=== MyBudgetApp Example Usage ===\n")
    
    # Create a user
    user = User("alice_smith", "alice@example.com", "Alice", "Smith")
    print(f"Created user: {user}\n")
    
    # Create accounts
    checking = Account("Main Checking", "checking", 2500.00)
    savings = Account("Emergency Fund", "savings", 10000.00)
    credit_card = Account("Credit Card", "credit", -450.00)
    
    print("Created accounts:")
    for account in [checking, savings, credit_card]:
        print(f"  - {account}")
    print()
    
    # Create categories
    categories = [
        Category("Housing", "expense", 1200.00, "Rent and utilities"),
        Category("Food", "expense", 400.00, "Groceries and dining"),
        Category("Transportation", "expense", 300.00, "Gas and car maintenance"),
        Category("Entertainment", "expense", 200.00, "Movies, games, hobbies"),
        Category("Salary", "income", 0.00, "Monthly salary"),
        Category("Freelance", "income", 0.00, "Side income")
    ]
    
    print("Created categories:")
    for category in categories:
        print(f"  - {category}")
    print()
    
    # Create a monthly budget
    budget = Budget("February 2024 Budget", "monthly", date(2024, 2, 1))
    budget.accounts.extend([checking, savings, credit_card])
    budget.categories.extend(categories)
    
    print(f"Created budget: {budget}")
    print(f"Budget period: {budget.period} starting {budget.start_date}")
    print(f"Total budget limits: ${budget.total_budget_limit}\n")
    
    # Create some transactions
    transactions = [
        Transaction(4500.00, "Monthly salary deposit", "income", "Salary", "Main Checking"),
        Transaction(500.00, "Freelance project payment", "income", "Freelance", "Main Checking"),
        Transaction(1200.00, "Rent payment", "expense", "Housing", "Main Checking"),
        Transaction(85.50, "Grocery shopping", "expense", "Food", "Main Checking"),
        Transaction(45.00, "Gas station", "expense", "Transportation", "Credit Card"),
        Transaction(25.00, "Movie tickets", "expense", "Entertainment", "Credit Card"),
    ]
    
    budget.transactions.extend(transactions)
    
    print("Created transactions:")
    for transaction in transactions:
        print(f"  - {transaction}")
    print()
    
    # Display budget summary
    print("=== Budget Summary ===")
    print(f"Total Income: ${budget.total_income}")
    print(f"Total Expenses: ${budget.total_expenses}")
    print(f"Net Income: ${budget.net_income}")
    print()
    
    # Display category spending
    print("=== Category Spending ===")
    for category in budget.categories:
        if category.category_type == "expense":
            # Find transactions for this category
            category_transactions = [t for t in budget.transactions 
                                   if t.category == category.name and t.is_expense]
            spent = sum(abs(t.amount) for t in category_transactions)
            remaining = category.budget_limit - spent
            print(f"{category.name}: ${spent} / ${category.budget_limit} (${remaining} remaining)")
    print()
    
    print("✅ Example completed successfully!")


if __name__ == "__main__":
    main()