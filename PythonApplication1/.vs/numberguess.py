import random
player=int(input("Enter number"))
com=random.randint(1,21)
guessestime=0
while (True):
     if player==com:
          print(f"congratulaion your guess is right in {guessestime} times")
          break
     elif player>com:
          print("you gusses high number")
          player=int(input("enter number again:"))
          guessestime =guessestime+1
     elif player<com:
          print("you gusses low number")
          player=int(input("enter number again:"))
          guessestime=guessestime+1
     else:
          print("choose right choise")
          break
print(f'compuer choice is {player},your choice is {com}')