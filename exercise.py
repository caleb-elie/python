user_input = input("Select: add, subtract, multiply, divide: ").lower()
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Perform the selected operation
if user_input == "add":
    x = number
    y = 4
    print(f"The addition of {x} and {y} gives {x + y}")

elif user_input == "subtract":
    x = number
    y = 4
    print(f"The subtraction of {y} from {x} gives {x - y}")

elif user_input == "multiply":
    x = number
    y = 4
    print(f"The multiplication of {x} and {y} gives {x * y}")

elif user_input == "divide":
    x = number
    y = 4
    if y != 0:
        print(f"The division of {x} by {y} gives {x / y}")
    else:
        print("Division by zero is not allowed!")

else:
    print("Not valid input!")
