import random
'''
1 for snake
-1 for water
0 for gun

'''
computer = random.choice([-1, 1, 0])
youstr = input("enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youdict[youstr]

# By now we have two numbers , you and computer

print(f"You choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer == you):
    print("Its Draw !!!")
else:
    if(computer ==-1 and you == 1):
        print("YOU WIN !")
    elif(computer ==-1 and you == 0):
        print("YOU LOSE !")
    elif(computer == 1 and you == -1):
        print("YOU LOSE !")
    elif(computer == 0 and you == 1):
        print("YOU LOSE !")
    elif(computer == 0 and you == -1):
        print("YOU WIN !")
    elif(computer == 1 and you == 0):
        print("YOU WIN !")
    else:
        print("Somthing went wrong :(")
    
    