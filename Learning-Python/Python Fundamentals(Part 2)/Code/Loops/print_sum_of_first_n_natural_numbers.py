n = int(input("Enter the number of terms:"))
sum=0
for i in range(1, n+1):
    sum+=i
print("sum =",sum)

#or

n = int(input("Enter the number of terms:"))
sum=0
i=0
while(i<n):
    i+=1
    sum+=i
print("sum =",sum)