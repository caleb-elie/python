# def addNumber(x, y):
#     return x + y
# print(addNumber(3, 5))
name = True

def add_number(currentYear, year):
    while name:
        enterYourName = input("My name is: ")
        if enterYourName == "":
            print("Name cannot be empty. Please try again.")
        else:
            print(f"Hello, {enterYourName}!")
             
            age = currentYear - year
            print(f"You are approximately {age} years old.")
            break 
currentYear = 2024
birthYear = int(input("Enter your birth year: "))
add_number(currentYear, birthYear)
