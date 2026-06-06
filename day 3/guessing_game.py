import random
jackpot=random.randint(1,100)
guess=int(input("enter a number"))
count=1
while jackpot!=guess:
    if guess>jackpot:
        print("lower")
    else:
        print("higher")    
    guess=int(input("enter a number"))
    count+=1
print("you got it")
print("you took",count,"attemps")        
