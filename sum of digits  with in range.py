def digits(a):
    sum = 0
    for i in a:
        i = int(i)
        sum = sum + i
    if 0 < sum <= 26:
        return sum
    else:
        return digits(str(sum))
a=input()
print(chr(digits(a)+64))
