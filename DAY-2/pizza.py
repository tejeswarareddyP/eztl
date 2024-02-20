import math
n,x=map(int,input("enter number of people and pieces they need").split(" "))
r=n*x
print(math.ceil(r/4))
