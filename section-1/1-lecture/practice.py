#varible-> is a box, which is used to store the data
# name="dheeraj"
# age=21
# state="punjab"
# country="india"
# print("Name:",name)
# print("Age:",age)
# print("State:",state)
# print("Country:",country)

#question
#Write a Python program to print "Hello, World!"
#print("Hello World")

# 2 Write a Python program that takes a user input and prints it.
# name=input("Enter your name")
# print(f"Your name is {name}")

# 3 Write a Python program to check if a number is positive, negative, or zero.
# number=int(input("Enter a number=> ")) #make sure to convert it into int, as input method considered input as strig
# if(number==0):
#     print("Number is zero")
# elif(number<0):
#     print("Number is negative")
# else:
#     print("Number is positive")

#  4 Write a Python program to find the largest of three numbers.
# num1=int(input("Enter first number=> "))
# num2=int(input("Enter second number=> "))
# num3=int(input("Enter third number=> "))
# if(num1>num2):
#     if(num1>num3):
#         print(f"First number is greater {num1}")
#     else:
#         print(f"Third number is greater {num3}")
# elif(num1<num2):
#     if(num2>num3):
#         print(f"Second number is greater {num2}")
#     else:
#         print(f"Third number is greater {num3}")
# else:
#     print(f"Third number is greater {num3}")

# Write a Python program to swap the values of two variables.
num1=int(input("Enter first number=> "))
num2 =int(input("Enter second number=> "))
print(f"Number's before swaping are => first number=> {num1} and second number=> {num2}")
swapNum=num1
num1=num2
num2=swapNum
print(f"Number's after swapping are=> First number=> {num1} AND second number=> {num2}")