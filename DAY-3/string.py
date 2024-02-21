s1,s2=map(str,input().split(" "))
s3=""
for i in range(len(s2)):
    if i!=s2[i]:
        s3+=i
print(s3)
