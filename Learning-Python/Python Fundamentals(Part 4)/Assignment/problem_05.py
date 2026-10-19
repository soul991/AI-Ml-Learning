# Q5. Create a base class Vehicles with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike).

class Vehicles:
    brand = "BMW"
    model = "V2.5"

class Cars(Vehicles):
    def __init__(self, seats):
        self.seats = seats

class Bikes(Vehicles):
    def __init__(self, engine_cc):
        self.engine_cc = engine_cc

car1 = Cars(4)
car2 = Cars(8)

bike1 = Bikes(650)
bike2 = Bikes(350)

a = input("Enter the vehicle type you want to preview: " ).lower()
if(a=="bikes"):
    b = input("Which bike do you want to preview? ")
    if(b=="bike1"):
        print(f"This bike is from {bike1.brand} with model number {bike1.model} and has a {bike1.engine_cc}cc engine.")
    else:
        print(f"This bike is from {bike2.brand} with model number {bike2.model} and has a {bike2.engine_cc}cc engine.")
else:
    b = input("Which car do you want to preview? ")
    if(b=="car1"):
        print(f"This car is from {car1.brand} with model number {car1.model} and has {car1.seats}seats.")
    else:
        print(f"This car is from {car2.brand} with model number {car2.model} and has {car2.seats}seats.")