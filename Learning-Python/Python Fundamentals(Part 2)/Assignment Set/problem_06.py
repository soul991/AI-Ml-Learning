# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 
# 3 and 5.
n = 1
while(1<=n<=100):
    if(n%15==0):
        print(n,end=',' )
    n+=1

print("these are the number between 1 to 100 which are divisible by both 3 and 5")