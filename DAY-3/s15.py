#odd composite#
def composite(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return 1
    else:
        return 0
n,m=map(int,input().split())

l=[]
for i in range(n,m+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)
#1,2,3,4,5,6,7,8,9
#1,3,5,7,9

