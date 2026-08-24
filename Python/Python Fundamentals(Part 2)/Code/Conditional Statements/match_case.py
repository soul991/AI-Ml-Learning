Color = input("Enter the colour: ")

match Color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("You have entered a wrong!")