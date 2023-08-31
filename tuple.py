def convert(l):
    return tuple(l)
t=(10,20,30,40)
l=list(t)
l.remove(30)
print(convert(l))