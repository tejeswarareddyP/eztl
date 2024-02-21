



#factorial#

def fact(n):
    if n==1:
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
        print("strong")
    else:
        print("not strong")

x=int(input())
print(strong(x))


