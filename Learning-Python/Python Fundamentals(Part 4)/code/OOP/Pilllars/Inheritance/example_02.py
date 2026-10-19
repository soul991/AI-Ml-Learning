class Employee:
    start_time = "9:00 a.m."
    end_time = "5:00 p.m."

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

    def change_time(self, new_end_time):
        self.end_time = new_end_time

emp1 =Teacher("Math")
emp1.change_time("6 p.m.")
print(f"Starting time of {emp1.subject} subject teacher is {emp1.start_time} and ending time is {emp1.end_time}")