#nesting is a process where we put a if else statement
#in an another if else statement

username = input("Enter the username: ")
password = input("Enter the password: ")

if(username == "admin" and password == "pass"):
    print("Login Successful!")
else:
    if(username != "admin"):
        print("username is incorrect")

    else:
        print("password is incorrect")