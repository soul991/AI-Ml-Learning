# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A Palindrome is a string which is same when we read it forward & backward.
# Eg -“madam”, “racecar” etc.

string = input("Enter the string:")
reversed_string=""

for ch in string:
    reversed_string=ch+reversed_string
print(reversed_string)
if(string==reversed_string):
    print("The string is pallindrome!")
else:
    print("The string is not pallindrome!")