a=input()
z=" "
g=" "
y=" "
u=''
for i in a:
    if(i.isalpha()):
        z+=i
    elif(i not in "0123456789"):
        g+=i
for i in z:
    if i not in u:
        u=u+i
print(g+u)


