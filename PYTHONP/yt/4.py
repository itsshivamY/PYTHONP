a=[1,2,3,4,5,6,67,8,4,45,7,45,45,35,36,64,74,74,6]
c=[]
for i in a:
    if a.count(i)>1 and i not in c:
        c.append(i)
print(c)