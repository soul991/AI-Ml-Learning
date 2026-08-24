# Write a program that takes salary as input. Using conditional statements, calculate the final tax rate
# based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%
 
salary = int(input("Enter the salary:"))
if(salary<30000):
    print("Calculated tax on the basis of salary is:", (salary*5)/100)
elif((30000>=salary<=70000)):
    print("Calculated tax on the basis of salary is:", (salary*15)/100)
else:
    print("Calculated tax on the basis of salary is:", (salary*25)/100)
