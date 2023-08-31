a=input()
c=0
for i in a:
    if(64<ord(i)>91) or (96<ord(i)>122):
        continue
    elif i in ["1","2","3","4","5","6","7","8","9","0"]:
        continue
    else:
        c+=1
print(c)
