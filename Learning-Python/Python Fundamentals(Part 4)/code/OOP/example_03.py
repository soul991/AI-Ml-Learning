class Student:
    college_name = "ABC College"

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Kabirul",9.2)
print(stu1.name)
print(Student.college_name)