#sum of given matrix#
n,m=int(input("rows :")),int(input("columns :")) 
l1=[0]*n
#[[1,2,3,],[4,5,6],[7,8,9]]#
for i in range(n):
	print("enter row %d: "%(i+1))
	l1[i]=list(map(int,input().split()))
#print(l1)
s,p=0,1
for i in l1:
	print(i)
	s+=sum(i)
print("sum",s)
#958209#

for i in l1:
	for j in i:
		print(j)
		p*=j
print("product",p)