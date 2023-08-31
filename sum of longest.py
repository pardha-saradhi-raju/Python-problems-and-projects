a=input()
l=list(a)
e=""
f=""
b=sorted(l)
c=sorted(l,reverse=True)
for i in b:
    e+=i
for j in c:
    f+=j
e=int(e)
f=int(f)
print(e+f)