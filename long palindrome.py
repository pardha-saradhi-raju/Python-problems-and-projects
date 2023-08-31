def pa(s):
    k=""
    for i in range(0,len(s)):
        for j in range(len(s),i,-1):
            if j-i==1 or j-i==-1:
                continue
            elif (s[i:j]==s[i:j][::-1]):
                k=s[i:j]
                return(k)
a=pa(input())
print(a)