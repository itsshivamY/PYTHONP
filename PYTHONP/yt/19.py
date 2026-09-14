a=int(input("Enter any number"))
rev=0
a2=a
while a>0:
    b=a%10
    rev=rev*10+b
    a=a//10
print(rev)
if rev==a2:
    print("palindrome")
else:
    print("Not Palindrome")