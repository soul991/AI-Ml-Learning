#Given a list of Tuples with info(name,subject):
#*list all unique courses 
#*list student enrolled in English
#*create dictionaries(student, set of courses)

info =[
("Alice" , "Math"),
("Bob" , "Science"),
("Charlie" , "Math"),
("Alice" , "Science"),
("Charlie" , "English"),
("Bob" , "English"),
]

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])
print(unique_courses)


for name,courses in info:
    if(courses=="English"):
        print(name)


dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)