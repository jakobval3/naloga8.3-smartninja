number_one = int(input("Type your first number here:"))
operation = input("Enter your operation here:")
number_two = int(input("Type your second number here:"))
if operation == "+":
    print(number_one + number_two)
elif operation == "-":
    print(number_one - number_two)
elif operation == "*":
    print(number_one * number_two)
elif operation == "/":
    print(number_one / number_two)
else:
    print("I don't recognize this operation.")
