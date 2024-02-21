def teja(n):
    if n<1:
       return 1
    else:
        teja(n-1)
        print(n)
        

n=int(input())
teja(n)
