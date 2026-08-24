#Q9. Write a function is_Prime(n) that returns True if n is a prime number
#and False otherwise, using a loop.
def is_Prime():
    a=int(input("Enter the number:"))
    i=2
    if ((a==0)or(a==1)):
        return False
    while(i<a):
        if(a%i==0):
            return False
        i+=1
    return True
print(is_Prime())