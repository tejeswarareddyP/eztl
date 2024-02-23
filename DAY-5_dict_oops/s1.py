#write a pp to take dict as input and print keys and values of a dict#
n=int(input("enter number of elements"))
d={}
for i in range(n):
	key=input(f"input key-{i}:")
	value=input(f"value for -{key}:")
	d[key]=value

for i in d:
	print("key:",i," value:",d[i])
	#print(f"key:{i} value:{d[i]}")
	#print("key:{} value:{}".format(i,d[i]))

"""for i in d.keys():
	print("keys",i)

for i in d.values():
	print("values",i)
"""