# Write a program to accept marks of 6 students and display them in a sorted
# manner. Find average of the marks
marks_list = []
i=1
while(i<7):
    marks=int(input(f"Enter the marks in subject{i}: "))
    marks_list.append(marks)
    i+=1
marks_list.sort()
print(marks_list)
sum =0
for int in marks_list:
    sum = sum+int
print(sum/6)