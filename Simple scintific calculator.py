import math

print("Welcome to the scientific calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Exponential")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")
print("11. Quit")

while True:
    choice = input("Enter your choice: ")

    if choice == '11':
        break

    if choice in ('5', '6', '7', '8', '9', '10'):
        num = float(input("Enter a number: "))

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", num1 / num2)

    elif choice == '5':
        print("sqrt(", num, ") =", math.sqrt(num))

    elif choice == '6':
        print(num, "^", "e =", math.exp(num))

    elif choice == '7':
        print("log(", num, ") =", math.log10(num))

    elif choice == '8':
        print("sin(", num, ") =", math.sin(math.radians(num)))

    elif choice == '9':
        print("cos(", num, ") =", math.cos(math.radians(num)))

    elif choice == '10':
        print("tan(", num, ") =", math.tan(math.radians(num)))

    else:
        print("Invalid input")
