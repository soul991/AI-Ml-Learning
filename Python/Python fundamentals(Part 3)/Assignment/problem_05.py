# Q5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary:

# 1.A - Add a student
# 2.B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

students_info = {"Alice": 73,
                 "Browny": 91,
                 "Melisa": 85,
                 "Marco": 94}
print("A - Add a student" \
", " "B - Update marks" \
", " "C - Search for a student" \
", " "D - Display all students and marks")
option = input("Enter the option: ")
if(option=="A")or(option=="a"):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks of the student: "))
    students_info.update({name:marks})
    print(students_info)
elif(option=="B")or(option=="b"):
    name = input("Enter the name: ")
    if(students_info.get(name)==None):
        print("No students available with this name")
    else:
        marks1 = int(input("Enter the new marks: "))
        print(students_info)
elif(option=="C")or(option=="c"):
    name = input("Enter the name: ")
    if(students_info.get(name)==None):
        print("No students available with this name")
    else:
        print(students_info[name])
elif(option=="D")or(option=="d"):
    print(students_info)
else:
    print("invalid Option!!")