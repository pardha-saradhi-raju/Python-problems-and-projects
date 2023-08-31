c=0
s=0
e=0
a=0
g=0
while (g<5):
    d=int(input())
    r=int(input())
    p=int(input())
    g=g+1
    if (d+r+p!=180):
        print("Wrong Entry try again")
        c=c+1
    else:
        if (d<90 and r<90 and p<90):
            s=s+1
        elif (d==90 or r==90 or p==90):
            e=e+1
        elif (d>90 or r>90 or p>90):
            a=a+1
print("Acute Angled Triangle:",s)
print("Right Angled Triangle:",e)
print("Obtuse Angled Triangle:",a)
print("Wrong Entries:",c)

