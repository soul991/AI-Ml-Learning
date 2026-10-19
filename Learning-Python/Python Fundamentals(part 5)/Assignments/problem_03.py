# Create a program that:
# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2.Uses a list comprehension to create a new list with only numbers greater than 15
# 3.Prints the new list

lst = [5, 10, 15, 20, 25]
lst = [val for val in lst if val>15]
print(lst)