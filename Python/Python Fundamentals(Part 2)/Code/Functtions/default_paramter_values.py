#If we don't pass a value for a parameter, it should take value 2

def sum(a=4, b=3): #default parameter follows non-default parameters
    sum=a+b
    return sum

print(sum(7,5))