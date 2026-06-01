## sum of n numbers
# number=int(input("Enter a number=> "))
# count=0;
# for i in range(1,number+1):
#     count+=i
# print(f"Sum of {number} is {count}")

## find a factorial of a number
# number=int(input("Enter a number=> "))
# fact=1
# for i in range(1,number+1):
#     fact*=i
# print(f"Factorial of {number} is {fact}")

## Simple Calculator program
FirstNumber=int(input("Enter first number=> "))
SecondNumber=int(input("Enter second number=> "))
operation=input("Select operation: +,-,*,/ =>")

# if operation=='+':
#     print(f"Sum of {FirstNumber} and {SecondNumber} is => {FirstNumber+SecondNumber}")
# elif operation=='-':
#     print(f"Subtraction of {FirstNumber} and {SecondNumber} is => {FirstNumber-SecondNumber}")
# elif operation == '*':
#     print(f"Multiplication of {FirstNumber} and {SecondNumber} is => {FirstNumber*SecondNumber}")
# elif operation == '/':
#     print(f"Division of {FirstNumber} and {SecondNumber} is => {FirstNumber/SecondNumber}")
# else:
#     print("Select valid operation!")

# # same in better way
# if operation == '+':
#     result = FirstNumber + SecondNumber
# elif operation == '-':
#     result = FirstNumber - SecondNumber
# elif operation == '*':
#     result = FirstNumber * SecondNumber
# elif operation == '/':
#     if SecondNumber != 0:
#         result = FirstNumber / SecondNumber
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operation."

# print("Result:", result)

# ### Determine the ticket price based on age and whether the person is a student.
# # Ticket pricing based on age and student status

# # Take user input
# age = int(input("Enter your age: "))
# is_student = input("Are you a student? (yes/no): ").lower()

# # Determine ticket price
# if age < 5:
#     price = "Free"
# elif age <= 12:
#     price = "$10"
# elif age <= 17:
#     if is_student == 'yes':
#         price = "$12"
#     else:
#         price = "$15"
# elif age <= 64:
#     if is_student == 'yes':
#         price = "$18"
#     else:
#         price = "$25"
# else:
#     price = "$20"

# print("Ticket Price:", price)


## Complex Example 4: User Login System
#A simple user login system that checks the username and password.
# User login system

# Predefined username and password
# stored_username = "admin"
# stored_password = "password123"

# Take user input
# username = input("Enter username: ")
# password = input("Enter password: ")

# Check login credentials
# if username == stored_username:
#     if password == stored_password:
#         print("Login successful!")
#     else:
#         print("Incorrect password.")
# else:
#     print("Username not found.")

#### Complex Example 3: Employee Bonus Calculation

#Calculate an employee's bonus based on their performance rating and years of service.
# Employee bonus calculation

# Take user input
# years_of_service = int(input("Enter years of service: "))
# performance_rating = float(input("Enter performance rating (1.0 to 5.0): "))

# # Determine bonus percentage
# if performance_rating >= 4.5:
#     if years_of_service > 10:
#         bonus_percentage = 20
#     elif years_of_service > 5:
#         bonus_percentage = 15
#     else:
#         bonus_percentage = 10
# elif performance_rating >= 3.5:
#     if years_of_service > 10:
#         bonus_percentage = 15
#     elif years_of_service > 5:
#         bonus_percentage = 10
#     else:
#         bonus_percentage = 5
# else:
#     bonus_percentage = 0

# # Calculate bonus amount
# salary = float(input("Enter current salary: "))
# bonus_amount = salary * bonus_percentage / 100

# print("Bonus Amount: ${:.2f}".format(bonus_amount))

## Prime numbers between 1 and 100

# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)




# range function

#1-> range(stop)
#When only one argument is given, Python starts from 0.
#example
# for i in range(5):
#     print(i)


#2. range(start, stop)
#Starts from the specified number and ends before stop.
#example
# for i in range(2, 6):
#     print(i)

#3-> range(start, stop, step)
# Moves according to the step value.
#example
# for i in range(1, 10, 2):
#     print(i)

# 4-> Negative Step (Reverse Counting)
#example
for i in range(10, 0, -1):
    print(i)