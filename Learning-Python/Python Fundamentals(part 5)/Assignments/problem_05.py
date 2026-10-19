# Write a program that tries to open in read mode. If the file does not exist, 
# catch the exception and print "File not found!".

import os
f = open("data.txt", "x")
f.write("Hey, you can fuck off!!")
f.close()
g = open("data.txt","r")
data = g.read()
print(data)
g.close()
os.remove("data.txt")
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File doesn't exist!")
else:
    print(f.read())