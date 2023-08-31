a=input()
sum=0
for i in a:
    i=int(i)
    f=1
    for j in range(1,i+1):
        f=f*j
    sum+=f
if (sum==int(a)):
    print("strong number")
else:
    print("not a strong number")