from calcFunpackage.calcFunctions import *

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5. Exit")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice = input("Enter your choice : ")

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", division(num1, num2))