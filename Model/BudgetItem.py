from Model import User, Transaction


class BudgetItem:
    def __init__(self, name, transactions: Transaction, user: User):
        self.transactions = None
        self.owner = user
        self.name = name
        self.transactions = transactions

    def AddNewExpense(self, transaction: Transaction):
        self.transactions.append(transaction)

    def RemoveTransaction(self, transaction: Transaction):
        self.transactions.remove(transaction)
