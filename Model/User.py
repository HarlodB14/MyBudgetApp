from Model.BudgetItem import BudgetItem

class User:
    def __init__(self, name):
        self.name = name
        self._budget_items = []

    @property
    def budget_items(self):
        return self._budget_items

    def add_budget_item(self, item):
        if not isinstance(item, BudgetItem):
            raise TypeError(f"Item moet een BudgetItem zijn, geen {type(item).__name__}")
        self._budget_items.append(item)
