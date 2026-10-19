#Function which walks like a duck and quacks like a duck

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Accountant:
    def get_designation(self):
        print("designation = Accountant")


t1 = Employee()
t1.get_designation()

t2 = Accountant()
t2.get_designation()