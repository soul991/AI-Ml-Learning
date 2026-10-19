f = open("file.txt", "w")
write = f.write("The previous content of this file has been overwritten.\nThis is the new contents of this file.\nSo, this is another test file.")
f.close()


g = open("file.txt", "r")
data = g.read()
print(data)