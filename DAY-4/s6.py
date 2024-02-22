#sum of elements of last column of matrix#
n,m=int(input("rows :")),int(input("columns :")) 
l1=[0]*n
#[[1,2,3,],[4,5,6],[7,8,9]]#
for i in range(n):
	print("enter row %d: "%(i+1))
	l1[i]=list(map(int,input().split()))
print(l1)
sum=0
for i in l1:
	sum+=i[-1]
print(sum)