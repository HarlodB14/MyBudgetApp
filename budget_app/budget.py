"""
Budget class for MyBudgetApp

Represents the main budget that contains categories, transactions, and accounts.
"""

from typing import List, Optional, Dict
from datetime import datetime, date
from decimal import Decimal


class Budget:
    """Represents a budget in the budgeting system."""
    
    def __init__(self, name: str, period: str = "monthly", start_date: Optional[date] = None):
        """
        Initialize a new Budget.
        
        Args:
            name: Name of the budget (e.g., "Monthly Budget 2024")
            period: Budget period ("monthly", "weekly", "yearly", "custom")
            start_date: Start date of the budget period (defaults to current date)
        """
        self.name = name
        self.period = period
        self.start_date = start_date or date.today()
        self.created_at = datetime.now()
        self.is_active = True
        
        # Collections of related objects
        self.categories: List = []  # Will contain Category objects
        self.transactions: List = []  # Will contain Transaction objects
        self.accounts: List = []  # Will contain Account objects
    
    @property
    def total_income(self) -> Decimal:
        """Calculate total income for this budget."""
        return sum(transaction.amount for transaction in self.transactions 
                  if transaction.is_income)
    
    @property
    def total_expenses(self) -> Decimal:
        """Calculate total expenses for this budget."""
        return sum(abs(transaction.amount) for transaction in self.transactions 
                  if transaction.is_expense)
    
    @property
    def net_income(self) -> Decimal:
        """Calculate net income (income - expenses)."""
        return self.total_income - self.total_expenses
    
    @property
    def total_budget_limit(self) -> Decimal:
        """Calculate total budget limits across all expense categories."""
        return sum(category.budget_limit for category in self.categories 
                  if category.category_type == "expense")
    
    def __str__(self) -> str:
        """String representation of the budget."""
        return f"Budget({self.name}: {self.period})"
    
    def __repr__(self) -> str:
        """Developer representation of the budget."""
        return f"Budget(name='{self.name}', period='{self.period}', start_date={self.start_date})"