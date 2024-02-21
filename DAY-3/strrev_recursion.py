#sstr rev using recursion
def rev(n,r):
    if n==0:
        return r
    else:
        return rev(n//10,r*10+n%10)
    

n=int(input())
x=rev(n,0)
print(x)
