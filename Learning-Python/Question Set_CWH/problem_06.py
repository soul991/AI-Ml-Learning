# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
s = {}
i=1
while(i<5):
    name = input(f"Enter the name of friend{i}: ")
    favourite_language=input(f"Enter the favourite language of frind{i}: ")
    s.update({name:favourite_language})
    i+=1
print(s)