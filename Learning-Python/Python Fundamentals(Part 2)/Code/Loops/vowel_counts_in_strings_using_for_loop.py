word = "artificial intelligence"
#count the number of vowels in the word
count = 0
for ch in word:
    if((ch=='a')or(ch=='e')or(ch=='i')or(ch=='o')or(ch=='u')or(ch=='A')or(ch=='E')or(ch=='I')or(ch=='O')or(ch=='U')):
        count+=1
print("Total vowels present in the word is=", count)