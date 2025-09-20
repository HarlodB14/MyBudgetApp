"""
Transaction class for MyBudgetApp

Represents individual financial transactions (income or expenses).
"""

from typing import Optional
from datetime import datetime
from decimal import Decimal


class Transaction:
    """Represents a financial transaction in the budgeting system."""
    
    def __init__(self, amount: float, description: str, transaction_type: str = "expense",
                 category: Optional[str] = None, account: Optional[str] = None, 
                 date: Optional[datetime] = None):
        """
        Initialize a new Transaction.
        
        Args:
            amount: Amount of the transaction (positive for income, negative or positive for expenses)
            description: Description of the transaction
            transaction_type: Type of transaction ("income" or "expense")
            category: Name of the category this transaction belongs to
            account: Name of the account this transaction is from/to
            date: Date of the transaction (defaults to current time)
        """
        self.amount = Decimal(str(amount))
        self.description = description
        self.transaction_type = transaction_type  # "income" or "expense"
        self.category = category
        self.account = account
        self.date = date or datetime.now()
        self.is_recurring = False
        self.tags = []  # List of tags for additional categorization
    
    @property
    def is_income(self) -> bool:
        """Check if this transaction is income."""
        return self.transaction_type == "income"
    
    @property
    def is_expense(self) -> bool:
        """Check if this transaction is an expense."""
        return self.transaction_type == "expense"
    
    def __str__(self) -> str:
        """String representation of the transaction."""
        sign = "+" if self.is_income else "-"
        return f"Transaction({sign}${abs(self.amount):.2f}: {self.description})"
    
    def __repr__(self) -> str:
        """Developer representation of the transaction."""
        return (f"Transaction(amount={self.amount}, type='{self.transaction_type}', "
                f"description='{self.description}')")