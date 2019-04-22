##Nhan Nguyen
##ITM 313
##Project 3


def print_menu():       ## menu bar
    print(31 * "-" , "menu" , 31 * "-")
    print("1. Draw a triangle")
    print("2. Draw a square")
    print("3. Draw a rectangle")
    print("4. Draw a bow tie")
    print("5. Exit")
    print(69 * "-")

def validSize(message): ##Validate input of User 
  while True:
    try: 
       inputSize = int(input(message))
       if inputSize > 50:   ##Error if Size greater than 50 
           raise ValueError
       elif inputSize < 1: ##Error if Size less than 1
           raise ValueError
    except ValueError:
       print("ERROR: Wrong size selection. Please enter a integer number from 1 to 50 to try again..\n")
       continue
    else:
       return inputSize 
       break

def validMenu(message): ##Validate input of User 
  while True:
    try: 
       inputMenu = int(input(message)) 
       if inputMenu > 5: ##Error if input menu greater than 50 
           raise ValueError
       elif inputMenu < 1: ##Error if input menu less than 1
           raise ValueError
    except ValueError:
       print("ERROR: Wrong menu selection. Please enter a integer number from 1 to 5 to try again..\n")
       continue
    else:
       return inputMenu 
       break

def one(): ##draw triangle
    print("Menu 1 has been selected")
    size = validSize("Please enter the size [1-50]: ")
    # number of spaces 
    k = 2*size - 2
    for i in range(0, size): 
        for j in range(0, k): 
            print(end=" ")  
        k = k - 1 
        for j in range(0, i+1): 
            # printing stars 
            print("* ", end="") 
        # ending line after each row 
        print("\r") 
  
 
def two(): ##draw square
    print("Menu 2 has been selected")
    size = validSize("Please enter the size [1-50]: ")
    for i in range(size):
        for j in range(size):
           print("*",end=" ")
        print()


def three(): ##draw rectangle
    print("Menu 3 has been selected")
    size = validSize("Please enter the size [1-50]: ")
    for i in range(int(size/2)):
        for j in range(size):
           print("*",end=" ")
        print()


def four(): ##draw bowtie
    print("Menu 4 has been selected")
    size = validSize("Please enter the size [5-50]: ")
    center = (size - 1)//2
    for i in range(size):
        spaces = 2*abs(i - center)
        stars = size - spaces
        print(stars*'*' + 2*spaces*' ' + stars*'*')
  
 
def five(): #exit program
    print("Menu 5 has been selected")
    print("program terminated!!!")
    return ""
 
def function(num): ##Switch function to select Menu
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
    }
    # get the function from switcher  
    func = switcher.get(num, lambda: "invalid number: please enter number from 1 to 5")
    return func()


def main():
    loop = True
    while loop: 
        print_menu() ## displays menu
        menu = validMenu("enter your choice [1-5]: ")
        print("")
        function(menu)
        if menu == 5:
            loop = False

main()





