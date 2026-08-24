# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
dict={}
print(type(dict))
i=1
while(i<7):
    hindi_word=input(f"Enter the no.{i} hindi word: ")
    english_translation = input(f"Enter the english translation of no.{i} {hindi_word}: ")
    dict.update({hindi_word:english_translation})
    i+=1
print(dict)
print(f"Do you want to look up?")
a = input("Enter the option:").lower()
if(a=="yes"):
    input_hindi_word= input("Enter the hindi word you want to look for:")
    if((dict.get(input_hindi_word))!=None):
        print(dict[input_hindi_word])
    else:
        print("No search found!")
elif(a=="no"):
    print("Ok!")