a=int(input("Enter a:"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum>a):
    print("Abudant number")
else:
    print("not a Abudant number")