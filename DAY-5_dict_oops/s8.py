#dict prime and compo determiner
d={}
n=int(input())
"""
for i in range(1,n+1):
	k="" 
	for j in range(1,i):
		if i%j==0:
			k="composite"
		elif j==1:
			k="prime"
		else:
			k="prime"
		return k
		d[j]=k
"""
def isprime(m):
	for i in range(2,m):
		if m%i==0:
			return "composite"
		else:
			return "prime"


for i in range(n):
	k=i+1
	v=isprime(i+1)
	d[k]=v
print(d)


