#                                !!!! THE PERFECT GUESS !!!!       
# We are going to write a program that generates a random number and asks the user to guess it

import random
n = random.randint(1,100)
a = -1
gusses = 1
while(a!= n):
    gusses +=1
a = int(input("Enter your number : "))
if(a>n):
    print("Thoda chota daal : ")

else:
    print("Thoda bada daal : ")


print(f"Congratulations tune sahi number{n} guess kiya hain vo bhi {gusses} main")
