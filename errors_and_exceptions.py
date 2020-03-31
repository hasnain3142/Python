while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError as v:
        print("Please enter a valid number, an error occured:",v)
    except KeyboardInterrupt:
        print("No Input")
        break
    else:
        print("The number you entered is",number)
        break
    finally:
        print("Attempted Input")