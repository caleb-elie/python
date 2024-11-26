num = int(input("Gimme a number: "))
if num % 2 == 0:
    print("Divisible by 2")
else:
    print("Not divisible by 2")
    
if num % 4 == 0:
        print("Divisible by 4")
else:
    print("Not divisible by 4")
           
Num = int(input("Enter a number again: "))
check = int(input("Enter the check now: "))
if Num % check == 0:
    print(f"wow !!, it is divisible by {check}")
else:
    print("Try again")