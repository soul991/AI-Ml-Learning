f = open("file2.txt", "a")
f.write("This line is newly created where the the pointer stopped after the last operation!!")
f.write("\nThis a separate line due.")

f.close()

g = open("file2.txt", "r")
data = g.read()
print(data)