#
"""
s=input()
count=0
for i in range(len(s)):
	for j in s[i]:
		count+=1
	if count>1:
		print(i)
		break
else:
		print(".")
"""

s=input()
for j in s:
	if s.count(j)>1:
		print(j)
		break
else:
	print(".")