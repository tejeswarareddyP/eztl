A,B,C,D=map(int,input().split(" "))
if (A-(A*C/100 ))>(B-(B*D/100)):
 print("Second")
elif (A-(A*C/100))<(B-(B*D/100)):
 print("First")
else:
 print("Any")
