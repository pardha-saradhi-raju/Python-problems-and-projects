a=input()
b=len(a)
sum=0
for i in a:
    i=int(i)
    sum=sum+i**b
if(str(sum)==a):
    print("given number is amstrong")
else:
    print("not a amstrong")
