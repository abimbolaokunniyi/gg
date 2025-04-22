# looping through numbers 1 to 5
for number in range (1,6):
	print(number)

# a program that checks whether each number 1 t0 15 is even or odd
for number in range (1,16):
	if number % 2 == 0:
		print (f"{number} is even")
	else:
		print (f"{number} is odd")
		
# simple calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# ask for operation
operation = input("choose a desired operator (+,-,*,/): ")

# perform calculation
if operation == "+" :
   result = num1 + num2
   print(f"The result of addition is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")