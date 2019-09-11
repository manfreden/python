# en slumpgenerator

import random # laddar in random klassen så vi kan använda den

print("vill du rulla en tärning?") # meddelande till 1

# försök läsa in sides som en int, vid fel sätt sides till 1
try:
    sides = int(input("hur många sidor: "))
except:
    print("Tärningen brhöver 1+ sidor")
    sides =1

run = "y" # vi ger run värdet y som standard

# SÅ LÄNGE run == y kör 
while run.lower() == "y":
    randomNumber = random.randint(1, sides)
    print(randomNumber)

    run = input("vill du rulla en till tärning[y/n]: ")