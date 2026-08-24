# Q4. Write a function to return the count the number of digits in a number, n. 

def counter():
    number = int(input("Enter the number:"))
    if number==0:
        return 1
    number = abs(number)
    count=0
    while(0<number):
       number//=10
       count+=1
print(counter())