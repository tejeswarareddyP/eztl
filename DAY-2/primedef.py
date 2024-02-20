#prime numbers in range#
def prime(n,m):
    for i in range(n,m+1):
        count=0
        for j in range(1,i+1):
         if i%j==0:
            count+=1
        if count==2:
         print(j)
n,m=map(int,input().split(" "))
prime(n,m)
