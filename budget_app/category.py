"""
Category class for MyBudgetApp

Represents a spending/income category for organizing transactions.
"""

from typing import Optional
from decimal import Decimal


class Category:
    """Represents a spending or income category in the budgeting system."""
    
    def __init__(self, name: str, category_type: str = "expense", budget_limit: float = 0.0, 
                 description: str = ""):
        """
        Initialize a new Category.
        
        Args:
            name: Name of the category (e.g., "Food", "Transportation", "Salary")
            category_type: Type of category ("expense" or "income")
            budget_limit: Budget limit for this category (mainly for expense categories)
            description: Optional description of the category
        """
        self.name = name
        self.category_type = category_type  # "expense" or "income"
        self.budget_limit = Decimal(str(budget_limit))
        self.description = description
        self.is_active = True
        self.transactions = []  # Will contain Transaction objects
    
    @property
    def spent_amount(self) -> Decimal:
        """Calculate total amount spent in this category."""
        return sum(abs(transaction.amount) for transaction in self.transactions 
                  if transaction.transaction_type == "expense")
    
    @property
    def remaining_budget(self) -> Decimal:
        """Calculate remaining budget for this category."""
        if self.category_type == "expense" and self.budget_limit > 0:
            return self.budget_limit - self.spent_amount
        return Decimal('0')
    
    def __str__(self) -> str:
        """String representation of the category."""
        return f"Category({self.name}: {self.category_type})"
    
    def __repr__(self) -> str:
        """Developer representation of the category."""
        return f"Category(name='{self.name}', type='{self.category_type}', limit={self.budget_limit})"