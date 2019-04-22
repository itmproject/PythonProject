##Nhan Nguyen
class BankingAccount:

    def __init__(self):
        self.balance = 0 
        print(15* " ","Welcome to Illinois TechCash Service")

    def get_balance(self):
        return self.balance

    def deposit(self): #deposit to balance
        amount_d = float(input("Enter amount to be Deposited: "))
        amount_w = 0
        self.balance += amount_d
        print("\nAmount Deposited= ${:,.2f}".format(amount_d))
        #current_time = datetime.datetime.now().strftime("%B %d,%Y: %H:%M:%S")
        #f = open("transaction.txt", "w+")
        #f.write("%s" %(current_time))
        ##L = [current_time, 10*" ", amount_d,10*" ", amount_w ,10*" ",self.balance, 10*" ", self.interest]
        ##f.writelines(L)
        #f.close()

    def withdraw(self): ##withdrawn from balance
        amount_w = float(input("Enter amount to be Withdrawed: "))
        amount_d = 0
        if self.balance >= amount_w:
            self.balance -=amount_w
            print("\nYou withdrawed= ${:,.2f}".format(amount_w))
        else:
            print("\nInsufficient Balance. ")
        #current_time = datetime.datetime.now()
        #f = open("transaction.txt", "w+")
        #L = [current_time, 10*" ", amount_d,10*" ", amount_w ,10*" ",self.balance, 10*" ", self.interest]
        #f.writelines(L)
        #f.close()


    def display(self):
        print("Available Balance= ${:,.2f}\n".format(self.balance))
    
    def interest(self): ##calculate interest accrued
        rate = 1 ##percentage
        time = 1 ##years
        interest_accrued = (self.balance * rate)/100 
        future_balance = interest_accrued + self.balance
        print("After 1 year with 1% in interest accrued, you will have= ${:,.2f}\n".format(future_balance))

    def menu(self): ##dislay menu 
        print("")
        print(31 * "-", "menu", 31 * "-")
        print("1. Account Balance")
        print("2. Amount Withdrawn")
        print("3. Amount Deposite")
        print("4. Interest Accrued")
        print("5. Exit")
        print(69 * "-")
   


