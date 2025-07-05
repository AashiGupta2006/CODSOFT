#PROJECT-1:- CALCULATOR 
print("~~~ MINI CALCULATOR~~~")

num1 = float(input("Enter first number : ")) 
num2 = float(input("Enter second number : "))

print(" Press 1 for Addition. \n Press 2 for Subtraction. \n Press 3 for Multiplication. \n Press 4 for Division.")

choice = int(input("Enter your choice from 1-4 : "))

if choice == 1:
    print("The addition of the numbers entered is : " , (num1 + num2))
elif choice == 2 :
    print("The subtraction of the numbers entered is : ",(num1 - num2))
elif choice == 3 :
    print("The multiplication of the numbers entered is : " ,(num1 * num2))
elif choice == 4 :
    print("The division of the numbers entered is : ",(num1 / num2))
else : 
    print("Invalid choice entered. Please try again.")