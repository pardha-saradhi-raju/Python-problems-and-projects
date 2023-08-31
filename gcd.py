def gcd(a, b):
    if (a > b):
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if ((a % i == 0) and (b % i == 0)):
            c = i
    return c
a = int(input())
b = int(input())
print(gcd(a, b))