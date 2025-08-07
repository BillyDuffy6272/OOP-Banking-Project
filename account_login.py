import csv
from account import Account
from account_storage import Account_storage
from account_wd import Account_wd

class Account_Login:
	def __init__(self, name, account_number, account_balance):
		self.name = name
		self.account_number = account_number
		self.balance = account_balance

	def login(self):
		name = input("What is the account name? ")
		account_number = input("What is the account number? ")
		csv_filename = "account_info.csv"
		user_found = False
		account_balance = 0
		with open(csv_filename, mode="r") as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				if row[0] == name and row[1] == account_number:
					user_found = True
					account_balance = int(row[2])
					return row[0], row[1], account_balance
					break
		if user_found == True:
			print(" ")
			print(" ")
			print(" ")
			print(f"Login successful! Welcome, {name}.")
			print(f"You account number is: {account_number}")
			print(f"Your balance is: {account_balance}")
			return account_balance
		elif  user_found == False:
			print("Login failed. Account not found.")
			exit()