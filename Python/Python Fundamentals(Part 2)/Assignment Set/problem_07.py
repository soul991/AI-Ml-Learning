while True:
    user_input = input("Enter the number: ")
    
    if user_input == "Quit":
        break
    elif user_input == "quit":
        break
    n = int(user_input)
    if n > 0:
        print("Entered number is positive")
    elif n < 0:
        print("Entered number is negative")
    else:
        print("Entered number is invalid")

print("Out of the loop!")