#p to print armstrong nos in given range#

def armstrong(n,m):
    for i in range(n,m+1):
        r=0
        x=i
        while i>0:
             d=i%10
             r+=d**3
             i//=10
        if r==x:
          print(x)
n,m=map(int,input().split(" "))
armstrong(n,m)         
