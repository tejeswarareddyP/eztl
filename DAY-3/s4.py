#to make encryption and decryption with a key value using functions#
n1=input("string:")
n2=int(input("key"))
def encr(n1,n2):
    s1=''
    for i in n1:
        x=ord(i)+n2
        s1+=chr(x)
    print(s1)
def decry(n1,n2):
    s1=''
    for i in n1:        
        x=ord(i)-n2
        s1+=chr(x)
    print(s1)
print("enter operation 1 for encry and 2 for decry")
n=int(input())
if n==1:
    encr(n1,n2)
else:
    decry(n1,n2)
"""
1.take string and key to encrypt or decrypt.
2.take if else for given operation give.
3.define funtions encry and decry.
4.declare empty string.
5.for loop for given string to change given string into ascii add/sub key and then change then again change it to string using chr.
x=ord(i)+/-key
chr(x) add to empty string
""" 
