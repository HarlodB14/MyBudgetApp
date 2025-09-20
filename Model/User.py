from Model import Transaction
from Model.BudgetItem import BudgetItem


class User:
    def __init__(self, name,budget_items: BudgetItem):
        self.name = name
        self.budget_items = []



