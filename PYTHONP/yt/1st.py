a=1234235
count=0
while a>0:
    b=a%10
    if b%2==0:
        print(b)
        count=count+1
    a=a//10
print(count)