a=int(input())
b=int(input())
for i in range(a,b+1):
    sum=0
    for k in range(1,i):
        if(i%k==0):
            sum=sum+k
    if(sum==i):
            print(i)