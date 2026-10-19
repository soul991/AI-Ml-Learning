class Employee:
    start_time = "9:00 a.m."
    end_time = "5:00 p.m."

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

emp1 =Teacher("Math")
print(f"Starting time of {emp1.subject} subject teacher is {emp1.start_time} and ending time is {emp1.end_time}")