##Project 4 
##Nhan Nguyen
##Program that subtracts a withdrawl from a Checking Account.
import datetime
from Banking import BankingAccount

s = BankingAccount()

def validMenu(self): ##Validate input of User 
    while True:
        try: 
            inputMenu = int(input(self)) 
            if inputMenu > 5: ##Error if input menu greater than 5
                raise ValueError
            elif inputMenu < 1: ##Error if input menu less than 1
                raise ValueError
        except ValueError:
            print("ERROR: Wrong menu selection. Please enter a integer number from 1 to 5 to try again..\n")
            continue
        else:
            return inputMenu 
            break

def validDepos(self): ##Validate deposite amountof User 
    while True:
        try: 
            inputMenu = int(input(self)) 
            if inputMenu < 1: ##Error if input menu greater than 5
                raise ValueError
        except ValueError:
            print("Negative Entries Are Not Allowed. Please try again\n")
            continue
        else:
            return inputMenu 
            break



def one(): ##Show Account Balance
    print("Menu 1 has been selected")
    print(40* "_","\n")
    s.display()
    s.interest()
    print(40* "_")
 
def two(): ##Get amount of withdrawn from user
    print("Menu 2 has been selected")
    print(40* "_","\n")
    s.withdraw()
    s.display()
    s.interest()
    print(40* "_")

def three(): ##Get amount of deposit from user
    print("Menu 3 has been selected")
    print(40* "_","\n")
    s.deposit()
    s.display()
    s.interest()
    print(40* "_")

def four(): ##Show Interest Accrued
    print("Menu 4 has been selected")
    print(40* "_","\n")
    s.display()
    s.interest()
    print(40* "_")
  
 
def five(): #exit program
    print("Menu 5 has been selected")
    print("program terminated!!!")
    return ""

def transaction():
    current_time = datetime.datetime.now()
    f = open("transaction.txt", "w+")
    L = ["Date", 10*" ", "Deposite",10*" ", "Withdrawn" ,10*" ","Balance",10*" ", "Interest Accrued \n"]
    f.writelines(L)
    f.close()


def function(num): ##switch function to select Menu
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
        }
    #Get the function from switcher
    func = switcher.get(num, lambda: "Invalid Number: please enter number from 1 to 5")
    return func()


def main():
    loop = True
    transaction()
    while loop:
        s.menu()
        menu = validMenu("Enter your choice from 1 to 5: ")
        print("")
        function(menu)
        if menu == 5:
            loop = False

main()

