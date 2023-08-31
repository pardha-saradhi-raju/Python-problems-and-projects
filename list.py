l=[1,2,3,4,5]
c=[]
d=[]
for i in range(0, len(l), 2):
    c.append(l[i])
for j in range(1, len(l), 2):
    d.append(l[j])
print(c+d)