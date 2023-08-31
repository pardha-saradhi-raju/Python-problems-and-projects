a=int(input())
p=1
for i in range(1,a+1):
    for j in range(i):
        print(p ,end=" ")
    for j in range(a-i):
        print(" ", end=" ")
    p=p+1
    print()