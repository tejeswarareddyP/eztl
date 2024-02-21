#armstrong no in range using function and string#
def armstrong(n,m):
    for i in range(n,m+1):
        s=str(i)
        sum=0
        for j in s:
            sum+=int(j)**len(s)
        if str(sum)==s:
            print(i)
n,m=map(int,input().split())
armstrong(n,m)
