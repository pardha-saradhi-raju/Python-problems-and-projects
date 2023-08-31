a=input()
u=" "
for i in a:
    b=int(ord(i))
    print(b)
    if (64<b>91) or (96<b>123):
        u+=i
print(u)

