a = int(input("enter the pin number:"))
if a == 1234 or a == 5678:
    b = input("give 'D' for deposit and 'W' for withdraw (D/W):")
    if (b == 'D'):
        c = int(input("enter number of 100:"))
        d = int(input("enter number of 500:"))
        e = int(input("enter number of 2000:"))
        print("recepit:")
        print("total amount deposited:", (c * 100 + d * 500 + e * 2000))
        print("balance amount:", (10000 + (c * 100 + d * 500 + e * 2000)))
    else:
        f = int(input("enter number of 100 to withdraw:"))
        if (1<f>10):
            g=(10000-(f*100))
            print("balance amount:",g)
        else:
            print("insufficient balance")
else:
    print("Invalid pin number")

