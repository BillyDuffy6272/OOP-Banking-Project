from tabulate import tabulate
from account import Account
import csv

class Account_storage:
    def __init__(self, name, account_number, initial_balance):
        # Initialize the account storage with name, account number, and initial balance
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
				 
    def account_store(self):
        # Store the account information in a CSV file
        csv_filename = "account_info.csv"
        # Append the account information to the CSV file
        with open(csv_filename, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.name, self.account_number, self.balance])
	        
        # Display the account information in a table format for easy reading
        table_data = [["Name", "Number", "Balance"],
                      [self.name, self.account_number, self.balance]]
        table = tabulate(table_data, headers="firstrow", tablefmt="heavy_grid")
        print(table)
