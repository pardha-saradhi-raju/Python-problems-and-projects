def pangram(s):
   alphabet="abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
         if char not in s.lower():
             return False
   return True
a="i am student"
if(pangram(a) == True):
    print("pangram")
else:
    print("not pangram")