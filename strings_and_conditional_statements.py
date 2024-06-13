# Strings and conditional statements in python 👇👇



class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        
    def add_customer(self, customer):
        self.customers.append(customer)
        
    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
        
    def get_balance(self):
        return self.balance

# Example usage
if __name__ == "__main__":
    # Create a bank
    my_bank = Bank("My Bank")
    
    # Create a customer
    customer1 = Customer("John Doe", 1)
    my_bank.add_customer(customer1)
    
    # Create accounts for the customer
    account1 = Account(1001, 500)
    account2 = Account(1002, 1000)
    
    customer1.add_account(account1)
    customer1.add_account(account2)
    
    # Deposit and withdraw money
    account1.deposit(200)
    account1.withdraw(100)
    
    # Check balances
    print(f"Balance for account 1001: ${account1.get_balance()}")
    print(f"Balance for account 1002: ${account2.get_balance()}")
    
    # Retrieve a customer and their account
    retrieved_customer = my_bank.get_customer(1)
    if retrieved_customer:
        print(f"Retrieved customer: {retrieved_customer.name}")
        retrieved_account = retrieved_customer.get_account(1001)
        if retrieved_account:
            print(f"Retrieved account balance: ${retrieved_account.get_balance()}")
