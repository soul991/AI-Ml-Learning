#Write a program to store seven fruits in a list entered by the user.
liist =[]
i=0

while(i<7):
    name = input("Input the fruit name: ")
    liist.append(name)
    i+=1
print(liist)
print(type(liist))