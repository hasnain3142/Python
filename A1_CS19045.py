#Imported sleep function from time module
from time import sleep

# GLOBAL ATTRIBUTES OF OBJECT: FOOD
def bakeshop_variables():
    global samosa_price, roll_price, cake_price, samosa_in_stock, roll_in_stock, cake_in_stock, total_sales
    # USED MOCK DATA
    samosa_price = 12
    roll_price = 15
    cake_price = 20
    samosa_in_stock = 20
    roll_in_stock = 30
    cake_in_stock = 15
    total_sales = 0

# GLOBAL ATTRIBUTES OF OBJECT: EMPLOYEE
# ARRANGED ALL ATTRIBUTES IN DICTIONARY DATA STRUCTURE
def employee_variables():
    global employees
    # USED MOCK DATA
# EMPLOYEE DICT-> ID : [Name, Sales, WageRate, HoursWorked]     
    employees = {1 : ["Sherlock", 0, 12, 0], 2 : ["Steve", 0, 15, 0], 3 : ["Peter", 0, 10, 0]}

# GLOBAL ATTRIBUTES OF OBJECT: BOUTIQUE
def boutique_variables():
    global clothing, amount, item, quantity
    clothing = {1: ('Small dress', 1000), 2: ('Medium dress', 3000), 3: ('Large dress', 5000)}
    amount = 5000
    quantity = 12
    item = 'cakes'

# HELPER FUNCTION FOR VALIDATING INPUT
def input_validator(string, values):
    while True:
        c = input(string)
        if c in values:
            return c
        print("INVALID INPUT, TRY AGAIN...")


# MAIN FUNCTION
def welcome():
    """
    DISPLAYS MAIN MENU OF THE PROGRAM
    """
    print("."*60)
    print(" BakeShop Management System ".center(60,'='))
    print("."*60)
    print("Which operation would you like to perform?")
    print("1. Take me to Bakeshop")
    print("2. Check Employee Data")
    print("3. Take me to Boutique")
    print("4. Exit")
    print()

    c = input_validator("Enter: ",['1','2','3','4'])
    print('-'*20)
    if c == '1':
        bakeshop()
    elif c == '2':
        employee()
    elif c == '3':
        boutique()
    elif c == '4':
        print("Bye, see you again :)")
        return

# MAIN FUNCTION ASSOCIATED WITH OBJECT: FOOD 
def bakeshop():
    print("="*19)
    print("Welcome to Bakeshop")
    print("="*19)
    print("Which operation would you like to perform?\n1. Check Stocks\n2. Add Stocks\n3. Calculate Bill\n4. Leave Bakeshop")
    print()
    c = input_validator("Enter: ",['1','2','3','4'])
    print('-'*20)
    if c == '1':
        check_stocks()
        sleep(1)
        bakeshop()
    elif c == '2':
        add_stocks()
    elif c == '3':
        calculate_bill()
    elif c == '4':
        welcome()

# FUNCTION ASSOCIATED WITH OBJECT: FOOD
def check_stocks():
    global samosa_in_stock, roll_in_stock, cake_in_stock
    print("ITEM {:>8}\nSamosas: {:>4}\nRolls: {:>6}\nCakes: {:>6}".format("QTY",samosa_in_stock, roll_in_stock, cake_in_stock))
    print('-'*20)

# FUNCTION ASSOCIATED WITH OBJECT: FOOD
def add_stocks():
    global samosa_in_stock, roll_in_stock, cake_in_stock
    print("Which item would you like to add in stocks?\n1. Samosas\n2. Rolls\n3. Cakes")
    c = input_validator("Enter: ",['1','2','3'])
    q = int(input("Enter quantity: "))
    if c == '1':
        samosa_in_stock += q
    elif c == '2':
        roll_in_stock += q
    elif c == '3':
        cake_in_stock += q
    sleep(1)
    print("Stocks updated successfully")
    print('-'*20)
    print("Do you want to contnue adding stocks?")
    n = input_validator("Press 'Y' or 'N'...: ",['Y','y','N','n']).lower()
    print('-'*20)
    if n == 'y':
        add_stocks()
    else:
        bakeshop()

# FUNCTION ASSOCIATED WITH OBJECT: FOOD
def calculate_bill():
    global total_sales, samosa_in_stock, roll_in_stock, cake_in_stock, samosa_price, roll_price, cake_price, employees
    # Currently we have 3 employees with id 1, 2 and 3
    id = int(input_validator("Enter your employee id: ", ['1','2','3']))
    print("Enter your Order ")
    s = int(input("Quantity of samosas: "))
    r = int(input("Quantity of rolls: "))
    c = int(input("Quantity of cakes: "))
    print()
    sleep(1)
    if s > samosa_in_stock or r > roll_in_stock or c > cake_in_stock:
        print("WARNING! We are out of stocks.")
        print("Kindly add items in stocks")
        print('-'*20)
        print()
        bakeshop()
    else:
        sp, rp, cp = s*samosa_price, r*roll_price, c*cake_price
        total = sp + rp + cp
        print()
        print(
        "Bill\n\
    Item     QTY   PRICE\n\
    Samosas  {}     {:>}\n\
    Rolls    {}     {:>}\n\
    Cakes    {}     {:>}\n\
    -------------------\n\
    Total          {}".format(s, sp,r, rp,c, cp,total ))
        samosa_in_stock -= s
        roll_in_stock -= r
        cake_in_stock -= c
        employees[id][1] += 1
        total_sales += 1
        sleep(1)
        print()
        bakeshop()

# MAIN FUNCTION ASSOCIATED WITH OBJECT: EMPLOYEE
def employee():
    global total_sales, employees
    print(24*"=")
    print("Welcome to Emloyee Data")
    print(24*"=")
    print("Which operation would you like to perform?")
    print("1. Check total sales\n2. Check Employee List\n3. Set Wage Rate\n4. Update Hours Worked\n5. Calculate Payment\n6. Exit")
    print()
    c = input_validator("Enter: ",['1','2','3','4','5','6'])
    print('-'*20)
    if c == '1':
        print("Total Sales of Bakeshop are:",total_sales)
        print('-'*20)
        sleep(2)
        employee()
    elif c == '2':
        employee_list()
        employee()
    elif c == '3':
        set_wage_rate()
    elif c == '4':
        update_hours_worked()
    elif c == '5':
        calculate_payment()
        employee()
    elif c == '6':
        welcome()

# FUNCTION ASSOCIATED WITH OBJECT: EMPLOYEE
def employee_list():
    print('{:5} {:10} {:10} {:10} {:10}'.format("ID", "NAME", "SALES", "WAGE RATE", "HOURS WORKED"))
    for i in employees:
        print("{:<5} {:10} {:>5} {:>14} {:>13}".format(i, employees[i][0], employees[i][1], employees[i][2], employees[i][3]))
    print('-'*25)
    sleep(2)

# FUNCTION ASSOCIATED WITH OBJECT: EMPLOYEE
def set_wage_rate():
    employee_list()
    print()
    id = int(input_validator("Enter employee id: ",['1','2','3']))
    rate = int(input('Enter: '))
    employees[id][2] = rate
    print("Wage Rate Set Successfully")
    print('-'*20)
    print("Do you wish to continue setting wage rates?")
    n = input_validator("Press 'Y' or 'N'...: ",['Y','y','N','n']).lower()
    print('-'*25)
    if n == 'y':
        set_wage_rate()
    else:
        employee()

# FUNCTION ASSOCIATED WITH OBJECT: EMPLOYEE
def update_hours_worked():
    employee_list()
    id = int(input_validator("Enter employee id: ",['1','2','3']))
    hours = int(input("Enter hours worked: "))
    employees[id][3] += hours
    print("Hours updated successfully")
    print('-'*20)
    print("Do you wish to continue updating hours?")
    n = input_validator("Press 'Y' or 'N'...: ",['Y','y','N','n']).lower()
    print('-'*25)
    if n == 'y':
        update_hours_worked()
    else:
        employee()

# FUNCTION ASSOCIATED WITH OBJECT: EMPLOYEE
def calculate_payment():
    print("{:10} {:>10}".format("Employee","Payment"))
    print('-'*22)
    for i in employees.values():
        print("{:10} {:10}".format(i[0], i[2]*i[3]))
    print('-'*25)
    sleep(2)


# MAIN FUNCTION ASSOCIATED WITH OBJECT: BOUTIQUE
def boutique():
    global amount, item, quantity
    print(20 * '=')
    print("Welcome to Boutique")
    print(20 * '=')
    print("SELECT ANY OPERATION:")
    print("1. View Deal\n2. Change Deal\n3. View Clothing\n4. Add Clothing\n5. Start Shopping\n6. Exit")
    print()
    c = input_validator("Enter: ",['1','2','3','4','5','6'])
    print('-'*20)
    if c == '1':
        print(f"SALE OF THE YEAR\nOn Shopping of {amount} RS\nYou will get {quantity} tasty {item} from our Bakeshop")
        print('-'*25)
        sleep(2)
        boutique()
    elif c == '2':
        change_deal()
        boutique()
    elif c == '3':
        view_clothing()
        sleep(1)
        boutique()
    elif c == '4':
        add_clothing()
        boutique()
    elif c == '5':
        shopping()
        boutique()
    elif c == '6':
        welcome()

# FUNCTION ASSOCIATED WITH OBJECT: BOUTIQUE
def change_deal():
    global amount, item, quantity
    print("SELECT any item to include in deal:\n1. Samosas\n2. Rolls\n3. Cakes")
    i = input_validator("Enter item: ",['1','2','3'])
    if i == '1':
        item = 'samosas'
    elif i == '2':
        item = 'rolls'
    elif i == '3':
        item = 'cakes'
    quantity = input("Enter quantity: ")
    amount = int(input("Enter amount of money: "))
    sleep(2)
    print("DEAL UPDATED SUCCESSFULLY")
    print('-'*25)

# FUNCTION ASSOCIATED WITH OBJECT: BOUTIQUE
def view_clothing():
    global clothing
    print(f"{'ITEM':15} {'PRICE':>10}")
    for i in clothing.values():
        print(f"{i[0]:15} {i[1]:>10}")
    print('-'*25)

# FUNCTION ASSOCIATED WITH OBJECT: BOUTIQUE
def add_clothing():
    global clothing
    name = input("Enter name of clothing: ")
    price = int(input("Enter price of clothing: "))
    key = len(clothing) + 1
    clothing[key] = (name,price)
    sleep(2)
    print("Clothing Updated Successfully")
    print('-'*25)

# HELPER FUNCTION FOR FUNCTION SHOPPING
def deal(item, quantity):
    item -= quantity
    if item < 0:
        print("SORRY FOR INCONVINENCE, UNFORTUNATELY WE ARE OUT OF STOCKS!")
        print("We will complete your order soon after updating aur stocks")
        return 0
    else:
        print("Enjoy your feast, Goodbye!")
        return item


# FUNCTION ASSOCIATED WITH OBJECT: BOUTIQUE
def shopping():
    global clothing, amount, quantity, item, samosa_in_stock, roll_in_stock, cake_in_stock
    bill = 0
    while True:
        print("SELECT THE ITEM YOU HAVE PURHASED:")
        print("{:2} {:20} {:>17}".format("ID", "ITEM", "PRICE"))
        for i in clothing:
            print("{:<2} {:20} {:>17}".format(i, clothing[i][0], clothing[i][1]))
        c = int(input_validator("Enter ID: ",[str(i) for i in clothing.keys()]))
        q = int(input("Enter quantity: "))
        bill += clothing[c][1] * q
        print("Do you want to continue shopping?")
        n = input_validator("Press 'Y' or 'N':",['y','Y','n','N']).lower()
        if n == 'n':
            break
    print("Calculating...")
    sleep(1)
    print(f"Your total bill is {bill} RS.")
    print('-'*25)
    if bill >= amount:
        print(f"Congratulations! on shopping of {bill} RS\nYou have been given free {quantity} {item} from our bakeshop.")
        quantity = int(quantity)
        if item == 'samosas':
            samosa_in_stock = deal(samosa_in_stock, quantity)
        elif item == 'rolls':
            roll_in_stock = deal(roll_in_stock, quantity)
        elif item == 'cakes':
            cake_in_stock = deal(cake_in_stock, quantity)
        print('-' * 20)
        sleep(2)


# FUNCTION FOR STARTING PROGRAM
def start():
    bakeshop_variables()
    employee_variables()
    boutique_variables()
    welcome()

start()