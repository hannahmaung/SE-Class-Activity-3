#Simple calculator program, asks user what operation they want to do and the program calculates it 


# function called add, adds x and y
def add(a, b):
    return a + b

# function called subtract, subtracts x-y
def subtract(a, b):
    return a - b

# function called divide, divides x/y
def divide(a, b):
    return a / b

# Function called multiply, multipies x and y
def multiply(a, b):
    return a * b

print("Please enter the operation you would like to do")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

while True:
    # Take input from the user
    choice = input("Enter choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        a = float(input("\nEnter your first number: "))
        b = float(input("Enter your second number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))
        break
    else:
        print("Invalid Input")