a=["14","7"]
for i in a:
    s=0
    c=1
    z=0
    for j in i:
        j=int(j)
        s=s+j
    for k in i:
        k=int(k)
        c=c*k
    if (c!=0):
        if (int(i)%s==0) or (int(i)%c==0):
            z+=1
print(z)