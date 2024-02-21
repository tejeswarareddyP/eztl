#strong in range

#factorial#

def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
#strong
def strong(x):
    s=0
    su=str(x)
    
    for i in su:
        s+=fact(int(i))
    if s==x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)
