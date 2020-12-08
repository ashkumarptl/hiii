import random
player=int(input("Enter number"))
com=random.randint(1,20)

while (True):
     if player==com:
          print("congratulaion your guess is right")
          break
     elif player>com:
          print("you gusses high number")
          player=int(input("enter number again"))
     elif player<com:
          print("you gusses low number")
          player=int(input("enter number again"))
     else:
          print("choose right choise")
          break
print(f'compuer choice is {player},your choice is {com}')