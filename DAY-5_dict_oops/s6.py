#list difference given number true
n=int(input("lenght of list"))
d=int(input("difference"))
l=list(map(int,input().split(" ")))
for i in l:
	for j in l:
		if i-j==d:	
			flag=1
	
print("false" if flag==0 else "true")