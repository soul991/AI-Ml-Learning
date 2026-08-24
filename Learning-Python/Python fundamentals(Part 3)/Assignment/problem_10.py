#Q10. Ask the user for a string and print:
#• All unique characters
#• The count of unique characters
strr = input("Enter a string: ")
unique_chars = set(strr)
print(f"Unique characters {unique_chars}")
print(f"Count of unique characters {len(unique_chars)}")