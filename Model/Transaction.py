from Model.Category import Category


class Transaction:
    def __init__(self, category: Category, amount, date):
        self._category = category
        self._amount = amount
        self._date = date

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._category = new_category
