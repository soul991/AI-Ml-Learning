class Employee:
    start_time = "9:00 a.m."
    end_time = "5:00 p.m."

class Admin_Stuffs:
    def __init__(self, role):
        self.role = role


staff1 = Admin_Stuffs("Manager")

print(f"The time shift for {staff1.role} is from {Employee.start_time} to {Employee.end_time}")
