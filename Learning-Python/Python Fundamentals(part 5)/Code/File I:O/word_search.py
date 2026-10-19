data = True
line = 1
word = input("Enter the word you want to look for in th file:")

with open("word_search.txt", "r") as f:
    # print(f.read())
    while data:
        data = f.readline()
        if word in data:
            print(f"Yes! The word exists in the file. And, it's in the line {line}.")
            break
        line +=1
    else:
        print("No! The word does not exist in the file.")