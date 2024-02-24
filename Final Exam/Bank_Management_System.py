from abc import ABC, abstractmethod
from random import randint

loan_status = True
loan_limit = 100000
accounts = []
bank_money = 0
total_loan_amount = 0

class Admin:
    def create_account(self, account):
        accounts.append(account)

    def show_accounts(self):
        print('\nAll Bank Accounts : ')
        for account in accounts:
            print(f"Name : {account.name}, Email : {account.email}, Balance : {account.balance}, Type : {account.type} \n")

    def delete_account(self, mail):
        flag = True
        for accountt in accounts:
            if accountt.email == mail:
                flag = False
                accounts.remove(accountt)
                break

        if flag == True:
            print('This Account Does not Exist\n')

    def change_loan_system(self, status):
        global loan_status 
        loan_status = status

        if loan_status == True:
            print('Loan is available')
        else:
            print('Loan is not available')

class User:
    def __init__(self, name, email, password, address, type, username) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.type = type
        self.account_number = 1000+len(accounts)
        self.balance = 0
        self.takeLoan = 0
        self.loan = 0
        self.history = []
        self.username = username

    def withdraw(self, amount):
        global bank_money 
        if amount >= 0 and amount <= self.balance:
            if amount > bank_money:
                print('The bank is bankrupt.\n')
            else:
                self.balance -= amount
                bank_money -= amount
                print(f"Your {amount} tk withdraw Successfully, Balance : {self.balance} \n")
                self.history.append(f'Withdraw : {amount}')
        else:
            print('Withdrawal amount exceeded\n')

    def deposit(self, amount):
        global bank_money 
        if amount >= 0:
            self.balance += amount
            bank_money += amount
            print(f"Your {amount} tk deposit Successfully, Balance : {self.balance} \n")
            self.history.append(f'Deposit : {amount}')
        else:
            print('Deposit Amount cannot negative\n')

    def takeloan(self, amount):
        global bank_money, total_loan_amount
        if self.takeLoan == 2:
            print('\nYou take loan at most two times\n')
        elif amount >= loan_limit:
            print('\nYou take loan at most 100000 tk\n')
        elif bank_money < amount:
            print('\nThe bank is bankrupt.\n')
        elif loan_status == False:
            print('\nLoan is not Available now\n')
        else:
            self.balance += amount
            bank_money -= amount
            self.takeLoan += 1
            self.loan += amount
            total_loan_amount += amount
            print(f'\nYour loan is successful,  Balance : {self.balance} \n')
            self.history.append(f'Loan : {amount}')

    def cheak_available_balance(self):
        print(f'Your Balance is : {self.balance}\n')

    def cheak_transaction_history(self):
        print('\nYour Loan History is : ')
        for his in self.history:
            print(his)
        print()

    def transfer_money(self, amount, to_username):
        global bank_money  
        if amount > bank_money:
            print('\nThe bank is bankrupt.\n')
            return

        for account in accounts:
            if account.username == to_username:
                if self.balance < amount:
                    print('\nYou balance is not enough\n')
                else:
                    self.balance -= amount
                    account.balance += amount
                    print(f'\nTransaction is successful, from {self.account_number} to {account.account_number}\n')
                    self.history.append(f'Transaction : {amount}')
                    account.history.append(f'Add by Transaction : {amount}')
                return
        print('Account does not exist')

currentUser = None

def main():
    # print('Hello')
    global currentUser
    while True:
        if currentUser == None:
            print('No User Logged in')
            print('--Choose your Option--')

            print('Option 1 : Admin Log in ')
            print('Option 2 : User Log in ')
            print('Option 3 : Exit ')

            op = int(input('Choose Option : '))

            if op == 1:
                password = input('Enter Admin Password : ')
                if password == '@admin':
                    print('Welcome Admin')
                    while True:
                        print('--Choose your Option--')
                        admin = Admin()
                        print('Option 1 : Create Account')
                        print('Option 2 : See all Accounts')
                        print('Option 3 : Delete Account')
                        print('Option 4 : On or Off the loan feature ')
                        print('Option 5 : Check Total Bank Balance')
                        print('Option 6 : Check Total Loan amount')
                        print('Option 7 : Logout')

                        ch = int(input('Choose Your Option : '))

                        if ch == 1:
                            name = input('Enter your name : ')
                            email = input('Enter your email : ')
                            password = input('Enter your password : ')
                            address = input('Enter your address : ')
                            type = input('Enter your Account Type (Savigs/Current): ')
                            username = input('Enter your Account username : ')

                            account = User(name, email, password, address, type, username)
                            admin.create_account(account)
                        elif ch == 2:
                            admin.show_accounts()
                        elif ch == 3:
                            email = input('Enter delete account email : ')
                            admin.delete_account(email)
                        elif ch == 4:
                            flag = True
                            opt = input('Enter option On/Off (True/False): ')
                            if opt == 'True':
                                flag = True
                            else:
                                flag = False
                            admin.change_loan_system(flag)
                        elif ch == 5:
                            print('Total Bank Balance is : ', bank_money)
                        elif ch == 6:
                            print('Total Loan amount is : ', total_loan_amount)
                        elif ch == 7:
                            currentUser = None
                            break
                else:
                    print('Incorrect Admin Password')
            elif op == 2:
                if len(accounts) == 0:
                    print('No account created in this bank')
                else:
                    username = input('Enter Username : ')
                    password = input('Enter Password : ')
                    flag = True
                    for account in accounts:
                        if account.username == username and account.password == password:
                            currentUser = account
                            flag = False

                    if flag:
                        print('Your username or Password Incorrect')
            elif op == 3:
                break
            else:
                print('Invalid Option')
        else:
            print(f'Welcome {currentUser.name}')

            print('Option 1: Withdraw')
            print('Option 2: Deposit')
            print('Option 3: Take Loan')
            print('Option 4: Cheak Available Balance')
            print('Option 5: Cheak your transaction history')
            print('Option 6: Transfer Money')
            print('Option 7: Logout')
            print('Option 8: Exit')
        
            ch = int(input('Choose Your Option : '))
        
            if ch == 1:
                amount = int(input('Enter your withdraw amount : '))
                currentUser.withdraw(amount)
            elif ch == 2:
                amount = int(input('Enter your Deposit amount : '))
                currentUser.deposit(amount)
            elif ch == 3:
                amount = int(input('Enter your loan amount : '))
                currentUser.takeloan(amount)
            elif ch == 4:
                currentUser.cheak_available_balance()
            elif ch == 5:
                currentUser.cheak_transaction_history()
            elif ch == 6:
                to_username = input('Enter transfer account username : ')
                amount = int(input('Amount : '))
                currentUser.transfer_money(amount,to_username)
            elif ch == 7:
                currentUser = None
            elif ch == 8:
                break
            else:
                print('Invalid Option')



if __name__ == '__main__':
    main()
