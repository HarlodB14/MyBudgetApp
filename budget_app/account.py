"""
Account class for MyBudgetApp

Represents a financial account (bank account, credit card, cash, etc.).
"""

from typing import Optional
from datetime import datetime
from decimal import Decimal


class Account:
    """Represents a financial account in the budgeting system."""
    
    def __init__(self, name: str, account_type: str, initial_balance: float = 0.0):
        """
        Initialize a new Account.
        
        Args:
            name: Name of the account (e.g., "Checking Account", "Credit Card")
            account_type: Type of account ("checking", "savings", "credit", "cash", etc.)
            initial_balance: Starting balance of the account
        """
        self.name = name
        self.account_type = account_type
        self.balance = Decimal(str(initial_balance))
        self.created_at = datetime.now()
        self.is_active = True
        self.transactions = []  # Will contain Transaction objects
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"Account({self.name}: ${self.balance:.2f})"
    
    def __repr__(self) -> str:
        """Developer representation of the account."""
        return f"Account(name='{self.name}', type='{self.account_type}', balance={self.balance})"