a=123
prod=1
while a>0:
    b=a%10
    prod=prod*b
    a=a//10
print(prod)