'''
Banking system
1.create accounts
2.deposit money
3.withdraw money
4.Transfer mOney
5.view Trasaction history


classes to be build:
1. Account
2.savings account
3.current Account
4.Bank

'''


class Account:
    def __init__(self,accno,name,balance=0):
        self.accno=accno
        self.name = name
        self.__balance = balance
        self.transactions = []
    
    def deposit(self,amount):
        self.__balance += amount
        self.transactions.append(f'Deposited : {amount}')
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            self.transactions.append(f'withdrawed: {amount}')
    
    def get_balance(self):
        return self.__balance
    
    def show_transactions(self):
        print(f'\nTransactions History for {self.name}')
        for t in self.transactions:
            print('-',t)
    
class savingsaccount(Account):
    def __init__(self,accno,name,balance =0):
        super().__init__(accno,name,balance)
        self.min_balance =500
    def withdraw(self, amount):
        if self.get_balance() - amount < self.min_balance:
            print("minimum balance need to be maintained")
        else:
            super().withdraw(amount)
    
class currentaccount(Account):
    def __init__(self,accno,name,balance=0):
        super().__init__(accno,name,balance)
        self.overdraft_limit = 1000
    def withdraw(self,amount):
        if self.get_balance() + self.overdraft_limit < amount:
            print('overdraft limmit exceeded')
        else:
            super().withdraw(amount)

class Bank:
    def __init__(self):
        self.accounts = {}
    def create_accounts(self,acc_type,accno,name,balance):
        if acc_type == 'savings':
            self.accounts[accno] = savingsaccount(accno,name,balance)
        elif acc_type == 'current':
            self.accounts[accno] = currentaccount(accno,name,balance)
    def get_account(self,accno):
        return self.accounts.get(accno)
    def transfer(self,from_acc,to_acc,amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if sender and receiver:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print("Transaction successful")
        else:
            print("Invalid account number")
    
def main():
    bank = Bank()
    while True:
        print("\n---- Banking System-----")
        print("1.Create Account")
        print("2.Deposit")
        print('3.Withdraw')
        print('4.Transfer')
        print('5.Balance')
        print('6.Transaction')
        print('7.Exit')
        choice = input("Enter your choice")
        if choice == '1':
            acc_type = input("Type (savings/current):")
            accno = input("Account Number:")
            name = input("Name")
            balance = int(input("Initial Balance:"))
            bank.create_accounts(acc_type,accno,name,balance)
        elif choice == '2':
            accno = input("Account number:")
            amt = int(input("Amount:"))
            acc = bank.get_account(accno)
            if acc:
                acc.deposit(amt)
        elif choice == '3':
            accno = input("Enter the account number:")
            amt = int(input("Amount:"))
            acc = bank.get_account(accno)
            if acc:
                acc.withdraw(amt)
        elif choice == '4':
            from_acc = input("Enter from account:")
            to_acc = input("Enter the to account:")
            amt = int(input("Enter the amount:"))
            bank.transfer(from_acc,to_acc,amt)
        elif choice == '5':
            accno = input("Enter the account number:")
            acc = bank.get_account(accno)
            if acc:
                print("Balance: ",acc.get_balance())
        elif choice == '6':
            accno = input("Enter the  Account number:")
            acc = bank.get_account(accno)
            if acc:
                acc.show_transactions()
        elif choice == '7':
            break

if __name__ == "__main__":
    main()