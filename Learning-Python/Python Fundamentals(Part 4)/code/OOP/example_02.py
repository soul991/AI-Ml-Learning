class Student:
    def __init__(self, name, cgpa, college): #parametrized constructor
        self.name = name
        self.cgpa = cgpa
        self.college = college

    def get_college(self):
        return self.college

stud_1 = Student("Rahul", 8.98, "CGEC")
stud_2 = Student("Arindam", 9.2, "JGEC")
stud_3 = Student("Kabirul", 8.99, "KGEC")

print(f"{stud_1.name} scored {stud_1.cgpa} from {stud_1.get_college()}")
print(f"{stud_2.name} scored {stud_2.cgpa} from {stud_2.get_college()}")
print(f"{stud_3.name} scored {stud_3.cgpa} from {stud_3.get_college()}")