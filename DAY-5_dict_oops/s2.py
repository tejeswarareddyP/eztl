#phone book
d={}
n=int(input("enter range"))
for i in range(n):
	key,value=map(str,input().split())
	d[key]=value

for i in d:
	k=input()
	if k in d.keys():
		print(f"{d[i]}")
	elif k in d.values():
		print(f"{i}")				
	else:
		print("not found")
		
	 

#for i in d:
#	print(f"{i}")
