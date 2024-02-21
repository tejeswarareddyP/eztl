#sstr rev using recursion
"""def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10 + n%10)"""
def rev(n,r):
    if n==0:
        return r
    else:
        return rev(n//10,r*10+n%10)
    

number = int(input("Enter number: "))

# Function call
reversed_number = rev(number,0)

# Display output
print("Reverse of %d is %d" %(number, reversed_number))
