a=input()
def fun(a):
    s=0
    if (int(a)>=9):
        for i in str(a):
            s=s+int(i)
        return fun(s)
    return(a)
g=fun(a)
print(g)


