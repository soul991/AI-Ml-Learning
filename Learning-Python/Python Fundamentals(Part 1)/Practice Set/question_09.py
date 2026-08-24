'''Q10.
Take a decimal number as input (like 45.78) and output its: 
integar part - 45
fractional part - .78'''

a = float(input("Enter the decimal number: "))

b = float(a) - int(a)
c = int(a)

print ("The integar part is", c , "& the float part is", b)