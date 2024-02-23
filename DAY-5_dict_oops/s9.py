#pp to maintain student marks database 
#using nested dict
d={}
n=int(input("no of students"))
for i in range(n):
	k=input("roll:")
	v={}
	m=int(input("enter subs.no"))
	for j in range(m):
		sub,marks=map(str,input().split())		
		v[sub]=marks
	d[k]=v


print(k,"=",v)



