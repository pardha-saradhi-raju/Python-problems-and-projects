a=input()
b=input()
if(len(a)==len(b) and sorted(a)==sorted(b)):
    print("The given string is Anagram")
else:
    print("The given string is not Anagram")