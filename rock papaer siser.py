import random
RoPeSe=["r","p","s"]
com=random.choice(RoPeSe)
user=input("enter rock paper scissor")
times=0
print(com)
print(user)
while True:
    if com=="s" and user == "s":
        print("draw awwwwww!")
        times=times+1
        pass
    elif com=="s" and user == "r":
        print("com select scisser you select rock so you win")
        times=times+1
        pass
    elif com=="s" and user=="p":
        print("com select scisser you select paper so com win")
        times=times+1
        pass
    else:
        print("1if condtion")
        if com=="r" and user=="s":
            print("com select rock you select scissor com you win")
            times=times+1
            pass
        elif com=="r" and user=="p":
            print("com select rock you select paper so you win")
            times=times+1
            pass
        elif com=="r" and user=="r":     
            print("com select rock you select rock draw awwwwww")
            times=times+1
            pass
        else:
            print("2if condtion")
            pass
            if com=="p" and user=="p":
                print("com select paper you select paper so draww awwww")
                times=times+1
                pass
            elif com=="p" and user=="r":
                print("com select paper you select rock so com win")
                times=times+1
                pass
            elif com=="p" and user=="s":
                print("com select paper you select paper so you win")
                times=times+1
                pass
            else:
                print("soorry i dont understant")
                pass

    if times>0:
        break
