userage = int(input("Enter your age: "))
user_name = input("Enter your name: ")
def userIdentity(name, age):
    if userage < 16:
        print("You are too young")
    else:
        print("You are an adult")
        
userIdentity(user_name, userage)