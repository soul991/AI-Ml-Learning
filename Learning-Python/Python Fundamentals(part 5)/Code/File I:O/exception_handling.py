try:    
    x = int(input("Enter the value:"))
    a = abs(10/x)
except ZeroDivisionError:   #There are built in error that we can use to avoid predicted errors
    print("Division by Zero is not permitable!")
except ValueError:
    print("Invalid Input!")
else:
    print(a)
finally: #This will be printed anyway
    print("The Python program has ended!")