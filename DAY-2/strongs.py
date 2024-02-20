#strong range#
def strong(n,m):
    for i in range(n,m+1):
        s=0
        x=i
        while i>0:
              d=i%10  
              r=1     
              for j in range(1,d+1):
                  r*=j
              i//=10
              s+=r
        if s==x:
         print(x)
n,m=int(input()),int(input())
strong(n,m)
        
