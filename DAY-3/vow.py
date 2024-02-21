#write a python program to print the smallest vowel repeating odd number of times 
def smvov(word):
    count=0
    for i in word:
        if i in "aeiouAEIOU":
            if word.count(i)%2!=0:
                s.append(word.count(i))
                print(min(s))
word=input()
s=""
print(smvov(word))

