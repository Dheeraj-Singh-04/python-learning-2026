#### Conditional Statements (if, elif, else)

## if statement
age=20

if age>=18:
    print("You are allowed to vote in the elections")


## else
## The else statement executes a block of code if the condition in the if statement is False.

age=16

if age>=18:
    print("You are eligible for voting")
else:
    print("You are a minor")


## elif
## The elif statement allows you to check multiple conditions. It stands for "else if"

age=17

if age<13:
    print("You are a child")
elif age<18:
    print("You are a teenager")
else:
    print("You are an adult")

## Nested Condiitonal Statements

# You can place one or more if, elif, or else statements inside another if, elif, or else statement to create nested conditional statements.

## number even ,odd,negative

num=int(input("Enter the number"))

if num>0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

else:
    print("The number is zero or negative")
## Practical Examples

## Determine if a year is a leap year using nested condition statement

year=int(input("Enter the year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")

else:
    print(year,"is not a leap year")



## Loops
## for loop

<!-- for Loop
Used when you know how many times you want to iterate. -->

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

###The range() function is used to generate a sequence of numbers. It is commonly used with for loops.

##Syntax
range(start, stop, step)

Parameters
start → Starting number (default = 0)
stop → Ending number (not included)
step → Increment/decrement value (default = 1)

Start from start, keep moving by step, and stop before stop

for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10,1,-1):
    print(i)
for i in range(10,1,-2):
    print(i)
## strings

str="Krish Naik"

for i in str:
    print(i)

## while loop

## The while loop continues to execute as long as the condition is True.

count=0

while count<5:
    print(count)
    count=count+1



## Loop Control Statements

## break
## The break statement exits the loop permaturely

## break sstatement

for i in range(10):
    if i==5:
        break
    print(i)
   
## continue

## The continue statement skips the current iteration and continues with the next.

for i in range(10):
    if i%2==0:
        continue
    print(i)



## pass
## The pass statement is a null operation; it does nothing.

for i in range(5):
    if i==3:
        pass
    print(i)

## Nested loopss
## a loop inside a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")


#### Conclusion:
Loops are powerful constructs in Python that allow you to execute a block of code multiple times. By understanding and using for and while loops, along with loop control statements like break, continue, and pass, you can handle a wide range of programming tasks efficiently.
