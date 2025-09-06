class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance +=amount
        return f"Deposited {amount}. New balance: {self.balance}"
    def withdrawal(self,user, amount):
        if user  != self.owner:
            return f"invalid user"
        if self.balance < amount:
            return f"insufficient fund current balance: {self.balance}"
        else:
            self.balance -= amount
            return f"{user} withdraw {amount} balance {self.balance}"
    def check_balance(self):
        return self.balance
        
acc = BankAccount("Alice",1000)
print(acc.balance)
print(acc.owner)
print(acc.withdrawal("tim", 200))
print(acc.withdrawal("Alice",500))
print(acc.balance)
print(acc.owner)
print(acc.balance)
