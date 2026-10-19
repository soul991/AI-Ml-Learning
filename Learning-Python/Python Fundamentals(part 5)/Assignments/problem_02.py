# Create a program that:
# 1. Opens a file in append mode"log.txt"
# 2.Adds a new log entry (like "Program run successfully")
# 3.Opens the file in read mode and prints all logs

f = open("log.txt", "a")
f.write("Program ran successfully\n")
f.close()

g = open("log.txt", "r")
data = g.read()
print(data)