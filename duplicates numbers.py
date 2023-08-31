import re
a=input()
l=" "
b=[]
u=''
c=''
f=''
z=" "
q=""
pattern=r'[0-9]'
l = re.sub(pattern,'',a)
print(l)
for i in l:
    if i not in b:
        b.append(i)
    else:
        b.remove(i)
print(b)
for i in b:
    print(b[i][4:5]+b[i][0:3])
k=u.join(b)
print(k)
for i in u:
    if((u[i]>='A'and u[i]<='Z')or(u[i]>='a'and u[i]<='z')):
        f=f+i
for i in f:
    if i not in z:
        z=z+i
print(z)








