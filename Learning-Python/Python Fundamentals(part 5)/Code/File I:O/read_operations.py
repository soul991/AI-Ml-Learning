#To Open a file and read 
f = open("file.txt", "r") #"file.txt" is for file name if file exists in the same folder or incase of other we need to mention the path
#"r" represents the mode "read". If we wanted the file in write mode then we would have to pass "w" arguement


data1 = f.readline()
print(data1, end = "")

data = f.read()
print(data)
print(type(data))


data2 = f.readline()
print(data2) #This will not print anything cause of the pointer. Through the data1 variable, the whole file already been read so nothing left to read.
#So nothing will also be printed



f.close() #If you open a file to perform operation, then you must need to close the files to avoide unnecessary changes.