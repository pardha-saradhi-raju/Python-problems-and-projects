a=input()
l=[]
c=" "
for i in range(65,91):
    l.append(chr(i))
for i in range(97,123):
    l.append(chr(i))
for i in a:
    if i in l:
        c+=i
print(c)
