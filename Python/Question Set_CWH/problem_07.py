# Write a program to find the greatest of four numbers entered by the user.
liist=[]
i = 1
while(i<5):
    n = int(input(f"Enter the number{i}: "))
    liist.append(n)
    i+=1
number1, number2, number3, number4 = liist
if((number1>number2)and(number1)>(number3)and (number1)>(number4)):
    print("number1 is greatest")
elif((number2>number3)and(number2)>(number4)):
    print("number2 is greatest")
elif((number3>number4)):
    print("number3 is greatest")
else:
    print("number4 is greatest!")