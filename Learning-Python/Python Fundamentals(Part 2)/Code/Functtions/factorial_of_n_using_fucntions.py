def cal_fact(n):
    factorial =1
    for i in range(1, n+1):
        factorial*=i
    return factorial

n = int(input("Enter the value:"))
print(cal_fact(n))