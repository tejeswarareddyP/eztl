#count of vowels and list of vowels of a each sentence#
def vow(words):	
	for word in words:
		num_vowels=0
		s1=''
		print(word)		
		for i in word:		
				if i.lower() in "aeiou":					
					num_vowels+=1
					s1+=i
		print(list(set(s1)))
		print("vowels count",num_vowels) 

words=input().split()
vow(words)