import random
"""
Snake=1
water=0
gun=-1
"""
computer=random.choice([1,0,-1])
n=input("Choose what you will: ")
Yourdict= {"S": 1,"W": 0,"G": -1}
reversedict= {1:"Sanke",-1:"Gun",0:"Water"}

you=Yourdict[n]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer==you):
    print("It's a Draw")
else:
    if(computer==-1 and you==0):
        print("You Win")
    elif(computer==-1 and you==1):
        print("You lose")
    elif(computer==1 and you==-1):
        print("You Win")
    elif(computer==1 and you==0):
        print("You lose")
    elif(computer==0 and you==1):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You lose")
    else:
        print("Something went wrong")
