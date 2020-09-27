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

lijstA = ["tekst", 11 , True , "#", 4.22, "meer tekst"]
lijstB = ["dit", "is", "een", "lijst", "van", "tekst"]
print(lijstA)
print(lijstA[1])

lijstA[1] = 23
print(lijstA)

print("-----------------------------------------------------------")

for waarde in lijstA :
    print("Dit is waarde: ", waarde)
else :
    print("klaar met de for loop")
