# Reminder: When selecting an option, please specify the name!

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

print("Choose an option:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input("> ")
message = True

if operation == "add":
    print("The result is: " + str(num1 + num2))

elif operation == "subtract":
    print("The result is: " + str(num1 - num2))

elif operation == "multiply":
    print("The result is: " + str(num1 * num2))

elif operation == "divide":
    if (num2 != 0):
        print("The result is: " + str(num1 / num2))
    else:
        print("Syntax ERROR: Can't divide by 0")
        message = False

if message == True:
    print("Operation complete!")
