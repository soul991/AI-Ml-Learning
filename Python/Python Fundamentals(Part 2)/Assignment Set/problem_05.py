#Q5. Write a function to return the sum of digits of a given number, n.

def sum_cal():
    number = int(input("Enter the number:"))
    if number==0:
        return 0
    sum=0
    while(number>0):
        sum+=number%10
        number//=10
    return sum

print(sum_cal())