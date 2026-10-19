#[output for item in iterable if condition]

#Using Basic loop
square = []
for i in range(1, 6):
    square.append(i*i)
print(square)
# print(square)

#Using list comprehension
square = [i*i for i in range(1,6)]
print(square)

square = [i*i for i in range(6) if i%2!=0]
print(square)


#Including If-else conditions
lst = [-2, 4, -9, 4, 5, 7, -3]
lst = [0 if val<0 else val for val in lst]
print(lst)

#Converting all words of a list from lowercase to uppercase
lower = ["code", "python", "cgec"]
lower = [vals.upper() for vals in lower]
print(lower)