#prime#
n=int(input("enter number"))
c=0
for i in range(1,n):
    if n%i==0:
        c+=1
if c==1:
        print("prime")
else:
        print("not prime")
    
        
