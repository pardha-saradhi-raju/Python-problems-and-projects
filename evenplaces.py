a=input()
b=len(a)
e=0
f=0
for i in range(1,b+1):
    if (i%2==0):
        j=a[i-1]
        j=int(j)
        e+=j
    else:
        k=a[i-1]
        k=int(k)
        f+=k
print(e-f)