x=int(input("enter year"))
print("Leap year" if (x%4==0 and x%100!=0) or (x%400==0)   else "non leap")
