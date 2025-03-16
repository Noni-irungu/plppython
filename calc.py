# A simple calculator to show my understanding of the various
#concepts learned in python so far.

def BasicCalculator():
    print("Welcome to your Basic Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number of the operation you want (1/2/3/4/): ")

# Float is used instead of int because it allows both whole and decimal numbers.
    if operation in ('1', '2', '3', '4'):
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        if operation == '1':
            print(f"The result is: {num_1 + num_2}")
        elif operation == '2':
            print(f"The result is: {num_1 - num_2}")
        elif operation == '3':
            print(f"The result is: {num_1 * num_2}")
        elif operation == '4':
            if num_2 != 0:
                print(f"The result is: {num_1 / num_2}")
            else:
                print("Error! Division by zero not allowed.")
    else:
        print("Invalid input! Please enter a valid operation.")

BasicCalculator()
