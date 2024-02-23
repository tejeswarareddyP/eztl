#map old keys with new keys with same values

n,m=map(int,input().split())
d={}
for i in range(n):
	k,v=map(str,input().split())
	d[k]=v			
for i in range(m):
	k1,v1=map(str,input().split())
	for i in d:
		if d[i] == v1[:-1]:
			print(f"{k1} {v1} #{i}")

print(d)
		
	
		

#print(f"{i} {d1[i]}")print(f"{i} {d2[i]}")for i in d2:for i in d1:
