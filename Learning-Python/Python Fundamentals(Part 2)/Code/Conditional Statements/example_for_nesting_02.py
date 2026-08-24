username = input("Enter the username: ")
if(username != "admin"):
    print("username not found!")
else:
    password = input("Enter the password: ")
    if(password != "pass"):
        print("Password is incorrect!")
    else:
        print("Login succesful!")