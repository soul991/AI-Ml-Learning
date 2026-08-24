# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
liist = []
i=1
while(i<9):
    a = int(input(f"Enter the no.{i} integar: "))
    liist.append(a)
    i+=1
liist1 = set(liist)
for int in liist1:
    print(int)