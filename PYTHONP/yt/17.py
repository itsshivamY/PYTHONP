a=int(input("Enter any number"))
s=0
p=1
while a>0:
    b=a%10
    s=s+b
    p=p*b
    a=a//10
if s==p:
    print("spy number")
else:
    print("not spy number")