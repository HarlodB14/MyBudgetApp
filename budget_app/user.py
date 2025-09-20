"""
User class for MyBudgetApp

Represents a user of the budgeting application.
"""

from typing import List, Optional
from datetime import datetime


class User:
    """Represents a user of the budgeting system."""
    
    def __init__(self, username: str, email: str, first_name: str = "", last_name: str = ""):
        """
        Initialize a new User.
        
        Args:
            username: Unique username for the user
            email: User's email address
            first_name: User's first name (optional)
            last_name: User's last name (optional)
        """
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.budgets: List = []  # Will contain Budget objects
        self.accounts: List = []  # Will contain Account objects
    
    def __str__(self) -> str:
        """String representation of the user."""
        name = f"{self.first_name} {self.last_name}".strip()
        return f"User({self.username}: {name or self.email})"
    
    def __repr__(self) -> str:
        """Developer representation of the user."""
        return f"User(username='{self.username}', email='{self.email}')"