n=int(input())
x=int(input())
for n in range(x,n):

 for i in range(2,n):
    if n%i==0:
        break
 else:
     print(n,"prime")
