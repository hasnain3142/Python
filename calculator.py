def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("Welcome")

while True:
    print("Select any one of the following operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    n = int(input("Enter operation no. "))
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    if n == 1:
        print("Result: ",add(a,b))
    elif n == 2:
        print("Result: ",subtract(a,b))
    elif n == 3:
        print("Result: ",multiply(a,b))
    elif n == 4:
        print("Result: ",divide(a,b))
    else: print("Invalid Operation")
    c = input("Press 'Y' to continue using My Calculator: ").upper()
    if c!="Y":
        break

