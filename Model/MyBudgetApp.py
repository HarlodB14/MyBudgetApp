from idlelib.pyparse import trans

from Model import User
from Model.BudgetItem import BudgetItem
from Model.Transaction import Transaction


class MyBudgetApp:

    def __init__(self, budget_items: BudgetItem):
        self.budget_items = []
        self.budget_items = budget_items
