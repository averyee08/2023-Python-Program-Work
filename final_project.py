import sys,time,os
import random

message = "Welcome to... \n\
SUPER FUN RANDOMIZED FIGHTER! \n"

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1.2)


typewriter(message)
print("Enter in your player information, and play against a friend to see who would win in a randomized fight! \n\
Choices of weaponry include: bow, sword, diamond shovel, and lasso (more coming soon) \n")   
message2 = "\n Player 1 \n"
def typewriter(message):
    for char in message2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1.2)


typewriter(message)
name = input("Enter player's name: ")
age = int(input("Enter player's age (as an integer): "))
weaponry = input("Enter player's weaponry here: ")
strength = 2
health = 120

class character:
    def __init__(self,name,age,strength,weaponry,health):
        self.name=name
        self.age=age
        self.weaponry=weaponry
        self.strength=strength
        self.health=health
    def printName(self):
        print("Name: " + self.name)
    def printAge(self):
        print("Age: " + str(self.age))
    def printHealth(self):
        if weaponry == "bow":
            self.health += 20
        if weaponry == "lasso":
            self.health += 15
        print("HP: " + str(self.health))
    def printWeaponry(self):
        print("Weaponry: " + self.weaponry)
    def printStrength(self):
        if weaponry == "bow":
            self.strength += 1
        elif weaponry == "sword":
            self.strength += 2
        elif weaponry == "diamond shovel":
            self.strength -= 1
        elif weaponry == "lasso":
            self.strength += 0.5
        else:
            self.strength = strength
        print("Attack strength: " + str(self.strength))
    def attack(self,target):
        self.health-=random.randint(1,7)*target.strength
        target.health-=random.randint(1,7)*self.strength
        print(self.health)
        print(target.health)

p1 = character(name,age,strength,weaponry,health)
p1.printName()
p1.printAge()
p1.printWeaponry()
p1.printStrength()
p1.printHealth()
print("\n")

message3 = "\n Player 2 \n"
def typewriter(message):
    for char in message3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1.2)


typewriter(message)
name2 = input("Enter player's name: ")
age2 = int(input("Enter player's age (as an integer): "))
weaponry2 = input("Enter player's weaponry here: ")
strength2 = 2
health2 = 120

class Rogue(character):
    def __init__(self,name,age,strength,weaponry,health):
        self.name=name2
        self.age=age2
        self.weaponry=weaponry2
        self.strength=strength2
        self.health=health2
    def printName(self):
        print("Name: " + self.name)
    def printAge(self):
        print("Age: " + str(self.age))
    def printHealth(self):
        if weaponry2 == "bow":
            self.health += 20
        if weaponry2 == "lasso":
            self.health += 15
        print("HP: " + str(self.health))
    def printWeaponry(self):
        print("Weaponry: " + self.weaponry)
    def printStrength(self):
        if weaponry2 == "bow":
            self.strength += 1
        elif weaponry2 == "sword":
            self.strength += 2
        elif weaponry2 == "diamond shovel":
            self.strength -= 1
        elif weaponry2 == "lasso":
            self.strength += 0.5
        else:
            self.strength = strength2
        print("Attack strength: " + str(self.strength))
    def attack(self,target):
        self.health-=random.randint(1,5)*target.strength
        target.health-=random.randint(1,5)*self.strength
        print(self.health)
        print(target.health)

p2 = Rogue(name, age, strength, weaponry, health)
p2.printAge()
p2.printWeaponry()
p2.printStrength()
p2.printHealth()
print("\n")

#attack!
message4 = "Fight! \n\n"
def typewriter(message):
    for char in message4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1.2)


typewriter(message)
while p1.health>0 and p2.health>0:
    p1.attack(p2)
if p2.health<=0:
   print("\n" + name + " wins!")
elif p1.health<=0:
   print("\n" + name2 + " wins!")

play_again = input("Play again?: ")

def playAgain():
    if play_again == "yes":
            message5 = "\n Player 1 \n"
            def typewriter(message):
                for char in message5:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)

                    if char != "\n":
                            time.sleep(0.05)
                    else:
                        time.sleep(1.2)

            typewriter(message)

            weaponry3 = input("Enter player's weaponry here: ")
            strength = 2
            health = 120

            class character:
                def __init__(self,name,age,strength,weaponry,health):
                    self.name=name
                    self.age=age
                    self.weaponry=weaponry3
                    self.strength=strength
                    self.health=health
                def printName(self):
                    print("Name: " + self.name)
                def printAge(self):
                    print("Age: " + str(self.age))
                def printHealth(self):
                    if weaponry3 == "bow":
                        self.health += 20
                    if weaponry3 == "lasso":
                        self.health += 15
                    print("HP: " + str(self.health))
                def printWeaponry(self):
                    print("Weaponry: " + self.weaponry)
                def printStrength(self):
                    if weaponry3 == "bow":
                         self.strength += 1
                    elif weaponry3 == "sword":
                        self.strength += 2
                    elif weaponry3 == "diamond shovel":
                        self.strength -= 1
                    elif weaponry3 == "lasso":
                        self.strength += 0.5
                    else:
                        self.strength = strength
                    print("Attack strength: " + str(self.strength))
                def attack(self,target):
                    self.health-=random.randint(1,7)*target.strength
                    target.health-=random.randint(1,7)*self.strength
                    print(self.health)
                    print(target.health)

            p1 = character(name,age,strength,weaponry,health)
            p1.printName()
            p1.printAge()
            p1.printWeaponry()
            p1.printStrength()
            p1.printHealth()
            print("\n")
                
            message6 = "\n Player 2 \n"
                
            def typewriter(message):
                for char in message6:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)

                    if char != "\n":
                        time.sleep(0.05)
                    else:
                        time.sleep(1.2)


            typewriter(message)
            weaponry4 = input("Enter player's weaponry here: ")
            strength2 = 2
            health2 = 120

            class Rogue(character):
                def __init__(self,name,age,strength,weaponry,health):
                    self.name=name2
                    self.age=age2
                    self.weaponry=weaponry4
                    self.strength=strength2
                    self.health=health2
                def printName(self):
                    print("Name: " + self.name)
                def printAge(self):
                    print("Age: " + str(self.age))
                def printHealth(self):
                    if weaponry4 == "bow":
                        self.health += 20
                    if weaponry4 == "lasso":
                        self.health += 15
                    print("HP: " + str(self.health))
                def printWeaponry(self):
                    print("Weaponry: " + self.weaponry)
                def printStrength(self):
                    if weaponry4 == "bow":
                        self.strength += 1
                    elif weaponry4 == "sword":
                        self.strength += 2
                    elif weaponry4 == "diamond shovel":
                        self.strength -= 1
                    elif weaponry4 == "lasso":
                        self.strength += 0.5
                    else:
                        self.strength = strength2
                    print("Attack strength: " + str(self.strength))
                def attack(self,target):
                    self.health-=random.randint(1,5)*target.strength
                    target.health-=random.randint(1,5)*self.strength
                    print(self.health)
                    print(target.health)

            p2 = Rogue(name, age, strength, weaponry, health)
            p2.printAge()
            p2.printWeaponry()
            p2.printStrength()
            p2.printHealth()
            print("\n")

            #attack!
            message7 = "Fight! \n\n"
            def typewriter(message):
                for char in message7:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)

                    if char != "\n":
                        time.sleep(0.05)
                    else:
                        time.sleep(1.2)


            typewriter(message)
            while p1.health>0 and p2.health>0:
                p1.attack(p2)
            if p2.health<=0:
                print("\n" + name + " wins!")
            elif p1.health<=0:
                print("\n" + name2 + " wins!")
           
    else:
        print("Game over!")
        
playAgain()
