a=input()
h=[]
for i in a:
    h.append(i)
c=0
l=["a","e","i","o","u","A","E","I","O","U"]
for i in range(1,len(h)):
    if (h[i-1] in l) and (h[i] not in l):
        c+=1
print(c)
