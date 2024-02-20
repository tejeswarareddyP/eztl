#strong number#
def strong(n):
    s=0
    x=n#145
    
    while n>0:
        d=n%10 #5,4  
        r=1     
        for i in range(1,d+1):
         r*=i#r=24,6
        n//=10#n=14
        s+=r#s=25
    if s==x:#s!=145
        print("strong")
    else:
        print("not strong")
n=int(input())
strong(n)
        
