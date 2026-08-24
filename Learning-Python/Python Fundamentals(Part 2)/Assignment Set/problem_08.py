#Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create a
#function calculator(a, b, operation) that performs addition, subtraction, 
#multiplication, or division based on the operation parameter.
#[parameter can have values '+', '-', '*'& '/'.]

def calculator(a, b, operation):
    if(operation=='+'):
        return a+b
    elif(operation=='-'):
            return a-b
    elif(operation=='*'):
            return a*b
    elif(operation=='/'):
            return a/b
    else:
          print("Invalid operation!")
    return calculator(a, b, operation)

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
operation = input("Enter the opertion:")
print(calculator(a, b, operation))