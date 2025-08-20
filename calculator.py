# Project Overview: Create a simple calculator that can perform basic arithmetic operations such 
# as addition, subtraction, multiplication, and division. Each operation will be implemented as a 
# separate function, and the user can choose which operation to perform. add(a, b) for addition 
# subtract(a, b) for subtraction multiply(a, b) for multiplication divide(a, b) for division


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by zero."
    return a/b
def calculator():
    print("Welcome to the simple calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice=input("Select choice (1/2/3/4):")
    if choice in ["1","2","3","4"]:
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
        except:
            print("Invalid choice. Please enter numeric values.")
        try:
            if choice=="1":
                print(f"The result is: {add(num1,num2)}")
            elif choice=="2":
                print(f"The result is: {subtract(num1,num2)}")
            elif choice=="3":
                print(f"The result is: {multiply(num1,num2)}")
            elif choice=="4":
                print(f"The result is: {divide(num1,num2)}")
        except:
            pass
    else:
        print("Invalid choice. Please select a valid option.")

calculator()

