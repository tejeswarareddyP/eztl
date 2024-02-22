#addition of two matrices#
n,m=int(input("rows :")),int(input("columns :")) 
l1,l2=[0]*n,[0]*n
#[[1,2,3,],[4,5,6],[7,8,9]]#
for i in range(n):
	print("enter row %d: "%(i+1))
	l1[i]=list(map(int,input().split()))
for i in range(n):
	print("enter row %d: "%(i+1))
	l2[i]=list(map(int,input().split()))
l3=[0]*m
for i in range(n):
	l3[i]=[0]*m

a,b=0,0
for i in range(m):
	for j in range(m):
		l3[i][j]=l1[i][j]+l2[i][j]
print(l3)
