#to check penagram(same letters) or not#
import string
a=input()
a=a.lower()
s1=string.ascii_uppercase
print(s1)
if set(a)==set(s1):
	print("penagram")
else:
	print("not")