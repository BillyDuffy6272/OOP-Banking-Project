import csv
from account import Account
from account_storage import Account_storage
from account_wd import Account_wd
# Import information, variables, and classes from other files

class Account_Login:
	def __init__(self, name, account_number, account_balance):
		# Initialize the account login with name, account number, and balance
		self.name = name
		self.account_number = account_number
		self.balance = account_balance

	def login(self):
		#Save the account name and number from user input
		name = input("What is the account name? ")
		account_number = input("What is the account number? ")
		csv_filename = "account_info.csv"
		user_found = False
		account_balance = 0
		# Compare the user input with the csv file 
		with open(csv_filename, mode="r") as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				# If the name and account number match, set user_found to True and return the account details
				if row[0] == name and row[1] == account_number:
					user_found = True
					account_balance = int(row[2])
					return row[0], row[1], account_balance
					break
		if user_found == True:
			print(" ")
			print(" ")
			print(" ")
			# Display the account information after successful login
			print(f"Login successful! Welcome, {name}.")
			print(f"You account number is: {account_number}")
			print(f"Your balance is: {account_balance}")
			return account_balance
		elif  user_found == False:
			# If the user is not found, error message showing login failed
			print("Login failed. Account not found.")
			exit()