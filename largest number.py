def larger(l):
    b=0
    for i in range(0,len(l)):
        if(l[i]>b):
            b=l[i]
    return b
l=[1,2,3,4,5,6,7,8,9]
print(larger(l))