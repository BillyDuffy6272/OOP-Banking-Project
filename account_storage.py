from tabulate import tabulate
from account import Account
import csv

class Account_storage:
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
				 
    def account_store(self):
        csv_filename = "account_info.csv"
        with open(csv_filename, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.name, self.account_number, self.balance])
	        
        table_data = [["Name", "Number", "Balance"],
                      [self.name, self.account_number, self.balance]]
        table = tabulate(table_data, headers="firstrow", tablefmt="heavy_grid")
        print(table)
