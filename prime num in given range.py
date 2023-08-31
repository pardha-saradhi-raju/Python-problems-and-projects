a=int(input("Enter a:"))
b=int(input("Enter b:"))
for i in range(a,b+1):
    c=0
    for k in range(1, i+1):
        if (i%k)==0:
            c=c+1
    if (c==2):
        print(i)

