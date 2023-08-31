a= [1,2,2,3,1,4,5,2,1,6,7,1]
f=[]
for i in a:
    f.append(a.count(i))
b=max(f)
for i in a:
    fre= a.count(i)
    if (b==fre):
        print(i)
        break
