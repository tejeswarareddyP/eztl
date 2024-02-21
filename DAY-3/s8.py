#sum of n no.s using recursion#
def teja(n):
    if n<1:
        return 1
    else:
        
        return n+teja(n-1)
        print(n)
n=int(input())
s=teja(n)
print(s)
