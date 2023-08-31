and for?")
a=input()
if a.lower()=="central processing unit":print("welcome to my computer quiz!")
playing=input("do you want to play? ")

if playing.lower() !="yes":
    quit()

print("let's play :")
score=0
print("what does cpu st
    print("corrent!")
    score+=1
else:
    print("incorrent!")
print("what does RAM stand for?")
a=input()
if a.lower()=="ramdom access memory":
    print("corrent!")
    score += 1
else:
    print("incorrent!")
print("what does GPU stand for?")
a=input()
if a.lower()=="graphics processing unit":
    print("corrent!")
    score += 1
else:
    print("incorrent!")

print("you got "+ str(score) +" questions corrent!")
print("you got "+ str((score/4)*100) +" %")

