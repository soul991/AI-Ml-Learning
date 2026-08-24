# Q2. Given a list of integers compute the average of all numbers in the list.

list = [24, 65, 98, 46, 37]
sum=0
for i in list:
    sum=sum+i
print(sum/(len(list)))
