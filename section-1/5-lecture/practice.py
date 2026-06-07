#Create a list of the first 20 positive integers. Print the list.
new_list=list(range(1,21))
# print(new_list)

# Print the first, middle, and last elements of the list created in question 1.
# first_element=new_list[0]
# last_element=new_list[-1]
# list_len=len(new_list) 
# middle_element=new_list[list_len//2]
# print(f"First element=> {first_element} , middle element=> {middle_element} and last element=> {last_element}")

# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Question 1
# first_five_elem=new_list[0:5]
# last_five_elem=new_list[-5:]
# specific_elem=new_list[5:16]
# print(specific_elem)


#note List Comprehension is a concise way to create a new list by applying an expression to each item of an iterable, optionally filtering elements with a condition.
# example
# [expression for item in iterable if condition]
# [i for i in range(1, 11) if i % 2 == 0]


#Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
# square_list=[i**2 for i in range(1,11)]
# print(square_list)

# Using List Comprehension, create a list of all even numbers from 1 to 20.
# even_no_list=[i for i in range(1,21) if i%2==0]
# print(even_no_list)

# numbers = [5, 12, 8, 25, 3, 18, 30]
# # Using List Comprehension, create a new list containing only the numbers that are greater than 10.
# new_number=[i for i in numbers if i>10]
# print(new_number)

words = ["apple", "banana", "kiwi", "mango", "orange"]
# Using List Comprehension, create a new list containing the length of each word.
new_word=[len(i) for i in words ]
print(new_word)