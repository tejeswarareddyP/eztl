n=int(input())
r=0
while n>0:
    d=n%10
    r=r+d**3
    n//=10
    
if r==n:
 print("true")
else:
 print("false")
    
