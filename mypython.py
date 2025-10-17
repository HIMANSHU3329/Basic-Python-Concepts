#Task 1: Perform Basic Mathematical Operations
# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform the basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero is not allowed)"

# Step 3: Display the results
print("\nResults of the operations:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


# Task 2: Create a Personalized Greeting

# Step 1: Take user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate first name and last name into a full name
full_name = first_name + " " + last_name

# Step 3: Print a personalized greeting using the full name
print(f"\nHello, {full_name}! Welcome to the program.")
