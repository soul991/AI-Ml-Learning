# Q4. Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

numbers = (23, 45, 18, 11, 46, 78)
even_numbers =[]
odd_numbers =[]
for i in numbers:
    if(i%2==0):
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
even_tuple= tuple(even_numbers)
odd_tuple= tuple(odd_numbers)
print(f"Even numbers{even_tuple}")
print(f"Odd numbers{odd_tuple}") 