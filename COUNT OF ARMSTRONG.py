a=int(input())
b=int(input())
f=0
for i in range(a,b+1):
    c=len(str(i))
    sum=0
    t=i
    while t>0:
        digit=t%10
        sum+=digit**c
        t//=10
    if i ==sum:
        f+=1
print(f)
