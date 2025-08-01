class Account:
    def __init__(self, account_name=None, account_number=None, initial_balance=0.0):
        self.name = account_name
        self.account_number = account_number
        self.balance = initial_balance

    def signup(self,name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        print("Account created successfully!")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
