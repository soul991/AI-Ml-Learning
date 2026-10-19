class Employee:
#     pass
# emp_1 = Employee()
# emp_2 = Employee()


# print(emp_1)
# print(emp_2)

# emp_1.first = 'Istak'
# emp_1.last = 'Ahamed'
# emp_1.email = 'istak.ahamed@email.com'
# emp_1.salary = 69000

# emp_2.first = 'Mustak'
# emp_2.last = 'Ahamed'
# emp_2.email = 'mustak.ahamed@email.com'
# emp_2.salary = 67000

# print(emp_2.email)
# print(emp_1.last)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() +'@email.com'
        self.pay = pay
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
emp_1 = Employee('Istak', 'Ahamed', 60000)
emp_2 = Employee('Mustak', 'Ahamed', 50000)

print(emp_1)
print(emp_2)

print(f"{emp_1.first} {emp_1.last}")
print(emp_2.email)
print(emp_2.first)
print(emp_2.fullname())