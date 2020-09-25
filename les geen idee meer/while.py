import random

isRunning = True

while ( isRunning ):
    num = random.randrange(5)
    print(num)
    if (num == 4) :
        isRunning = False
        print("right")
    else :
        print("wrong")
