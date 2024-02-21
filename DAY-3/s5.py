l,n=map(str,input().split())
s=''
no=input()
for i in range(len(no)):
    if int(no[i])<=int(n):
     print(no[:i]+n+no[i:])
     break
else:
    print(no+d)   
    
