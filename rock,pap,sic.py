import random

user=input("rock,paper,siccors?")
list=["rock","paper","siccors"]
comp=random.randint(0,2)
print(comp)
if (list[comp]=="rock" and user=="siccors") or (list[comp]=="paper" and user=="rock") or (list[comp]=="siccors" and user=="paper"):
    print("ai wins")
elif list[comp]==user:
    print("draw")
else :
    print("you wins")    

