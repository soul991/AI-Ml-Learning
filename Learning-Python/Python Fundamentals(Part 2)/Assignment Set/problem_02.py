# Write a code that takes two integers a and b
# and prints all even  numbers between them (inclusive).

a = int(input("Enter value of one digit: "))
b = int(input("Enter value of another digit: "))

if(a==b):
    print("Enter two different digits!")
if(a>b):
    while(a>=b):
        if(b%2==0):
            print(b)
        b+=1
elif(b>a):
    while(b>=a):
            if(a%2==0):
                print(a)
            a+=1