# 1. Opens a file in write mode "names.txt"
# 2.Writes 5 names (one per line) entered by the user
# 3.Then opens the same file in read mode and prints all names

f = open("names.txt", "x")
i = 0
while(i<5):
    a = input("Enter the name:",)
    f.write(a)
    if(i<4):
        f.write("\n")
    i+=1
f.close()
data = open("names.txt", "r")
d = data.read()
print(d)