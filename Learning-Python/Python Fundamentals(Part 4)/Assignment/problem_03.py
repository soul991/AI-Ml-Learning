# Ceate a class with attributes _name, _roll_no, and _marks.
# Provide getter and setters methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).


a = input("Enter the name of the student: ")
if(a==""):
    print("Name can't be empty!")
else:
    b = int(input(f"Enter the roll of {a}: "))
    if(b<1)or(b>100):
        print("Roll number has to be between 1 to 100")
    else:
        c = int(input(f"Enter the marks of {a}: "))
        if(c<0):
            print("Makrs can't be negative!")
        else:
            class Students:
                def __init__(self, name, roll_no, marks):
                    self.__name = name
                    self.__roll_no = roll_no
                    self.__marks = marks
                def get_roll_no(self):
                    return self.__roll_no
                def set_roll_no(self, new_roll):
                    if(new_roll<1)or(new_roll>100):
                        print("Roll should be in between 1 to 100")
                    else:
                        self.__roll_no = new_roll
                        print(f"New roll of {self.__name} is {self.__roll_no}")
                def get_student_name(self):
                    return self.__name
                def set_student_name(self, new_name):
                    if(new_name==""):
                        print("Name can't be blank!")
                    else:
                        self.__name = new_name
                        print(f"The new name of the student is {self.__name}")
                def get_marks(self):
                    return self.__marks
                def set_marks(self, new_marks):
                    if(new_marks<0):
                        print("Marks can't be Negative!")
                    else:
                        self.__marks = new_marks
                        print(f"The new marks of the {self.__name} is {self.__marks}")
student1 = Students(a, b, c)
r = input("Do you want to perform any operation (yes/no)? ").lower()
if(r=="yes"):
    print("What operation do you want to perform:\n" \
    "1. See the name of the student\n" \
    "2. See the roll of the student\n" \
    "3. See the marks of the student")
    x = int(input("Enter the serial no. of your choise: "))
    if(x==1):
        print(f"The name of the student is {student1.get_student_name()}")
        y = input('Do you want to change the name(Type "yes" or "no")?').lower()
        if(y=="yes"):
            z = input("Enter the new name: ").lower()
            student1.set_student_name(z)
    elif(x==2):
        print(f"The roll no of {student1.get_student_name()} is {student1.get_roll_no()}")
        y = input('Do you want to change the roll(Type "yes" or "no")?').lower()
        if(y=="yes"):
            z = int(input("Enter the new roll number: "))
            student1.set_roll_no(z)
    elif(x==3):
        print(f"The marks of the student {student1.get_student_name()} is {student1.get_marks()}")
        y = input('Do you want to change the marks(Type "yes" or "no")?').lower()
        if(y=="yes"):
            z = int(input("Enter the new marks: "))
            student1.set_marks(z)          
    else:
        print("Invalid choice!")