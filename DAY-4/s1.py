#for sum of even palindrome in a range and also print list of palin#
n,m=int(input()),int(input())
l1=''
while n>0:
	d=n%10
	r=r*10+d
	n//=10
	l1.append(r)

"""





def palindrome(n):
	n=str(n)
	if n==n[::-1]:
		return 1
	else:
		return 0	

n,m=int(input()),int(input())
i=0
l1,l2=[],[]
for i in range(n,m+1):
	flag=palindrome(i)
	if flag==1:
		l1.append(i)
		if i%2==0:
			if flag==1:
				l2.append(i)
print(l1)
print(sum(l2))
"""