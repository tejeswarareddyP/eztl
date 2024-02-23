#pp to print average of each student marks
d={}
s=0
n=int(input("no of students"))
for i in range(n):
	k=input("roll:")
	v={}
	m=int(input("enter subs.no"))
	for j in range(m):
		sub,marks=map(str,input().split())		
		v[sub]=marks
		p=int(marks)
		s+=p
	print("average: ",s/m)
	d[k]=v
