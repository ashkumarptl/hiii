import random

player=int(input("Enter your number"))
#player=int(player)
com=random.randint(1,5)
if (player==com):
    print("you win")
else:
    print("you lose")
print("computer choise is",com)
print("your choise is",player)