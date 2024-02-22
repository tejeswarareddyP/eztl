#sum of max and min element using tuple#
n,m=int(input("rows :")),int(input("columns :")) 
l1=[0]*n
#[[1,2,3,],[4,5,6],[7,8,9]]#
for i in range(n):
	print("enter row %d: "%(i+1))
	l1[i]=tuple(map(int,input().split()))
print(tuple(l1))
l2=[]
min,max=10,0
for i in l1:
	print(i)
	for j in i:
		if j>max:
			max=j
		if j<min:
			min=j
print("max:",max,"min:",min,"added",max+min)

	