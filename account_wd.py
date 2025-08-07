from account import Account
import csv

class Account_wd:
    def __init__(self, name, account_number, initial_balance):
        # Initialize the account with name, account number, and initial balance
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance

    def d_w(self):
        # Allow the user to deposit or withdraw funds from their account
        while True:
            update_funds = input("Would you like to deposit, withdraw or nothing? (d/w/n): ").lower()
            if update_funds == "d":
                # Deposit funds into the account
                deposit = int(input("How much to deposit? "))
                self.balance += deposit
                print(f"You now have {self.balance}")
            elif update_funds == "w":
                # Withdraw funds from the account
                withdraw = int(input("How much to withdraw? "))
                self.balance -= withdraw
                print(f"You now have {self.balance}")
            elif update_funds == "n":
                print("No Further changes made to your account.")
                break
        return self.balance
        
             
    def display_info(self):
        # Display the updated account information to show the changes made
        print("Updated information")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")