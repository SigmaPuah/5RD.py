# Date: 11/7/24
# author: <ekulkin2809002@woonsocketschools.com>
# author:
# author:
# project: 5RD

import random
from copyreg import constructor

from CodeTests import bridgeChoice

#from gzip import write32u

#time.sleep(2)
#os.system(clear)
bridgeChoice=True
playerStrength = 0
playerDexterity = 0
playerConstitution = 0
playerIntelligence = 0
playerWisdom = 0
playerCharisma = 0
playerHealth = 0
playerSpeed = 0
playerInititive = 0
playerAttack = 0
playerName = input("Salutations! What's your name?: ")
print("Great to meet you", playerName, "Im Dan the demigod. I gift any of those ancestries and classes who ask")
playerClass = input("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Classes are: Alchemist, Adventurer, Fighter, and a Sorcerer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Alchemists- are very skilled in potions.             2) Adventurers- are very outdoorsy with a "Spare Axe"
They can make a plethora of potions.                    and a "Torch" in which they can light out of thin air.
They carry a "Potion Maker" and "Crafting Box".         They allow +1 intelligence.
With +1 dexterity.

3) Fighters- are pure attacking phenoms.                4) Sorcerers- use many different spells to conjure up
They use "Brass Knuckles" along with                    all types of attacks. They use a "Magic Wand" to
"Noradrenaline Drink" to help fuel their punches.       help focus a set amount of power into one place
+1 strength                                             (the wand.) +1 wisdom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now what Class would you like? Please pick a number 1-4: """)
if playerClass == "1":
    print("Alchemist it is!")
    playerDexterity+=1
elif playerClass == "2":
    print("So an adventurer?")
    playerIntelligence+=1
elif playerClass == "3":
    print("A Fighting class? Smart choice.")
    playerStrength+=1
elif playerClass == "4":
    print("That will be a Sorcerer.")
    playerWisdom+=1
else:
    print("Thats not a real class. Please restart.")
print("Amazing. Lets set up your attributes.")
playerAncestry = input("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Ancestries include: Elves, Goblins, Dwarves, Halflings, and Humans.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Elves- are very smart and                            2) Goblins- are very similar to the Dwarves. 
intelligent creatures. With +2 intelligence,            They are the smelly slimey version of chihuahuas.
                                                        +1 constitution. and +1 strength

3) Halflings- are small humans                          4) Wizards- are entirely long range fighters.  
with better battle IQ. +2 dexterity                     +2 wisdom                 

5) Humans- are simply the baseline of all races.
+1 all attributes.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now what Ancestry would you like? Please pick a number from 1-5: """)
if playerAncestry == "1":
    print("Elf it is!")
    playerIntelligence+=2
elif playerAncestry == "2":
    print("So a Goblin?")
    playerConstitution+=1
    playerStrength+=1
elif playerAncestry == "3":
    print("A Halfling ancestry? Okay.")
    playerDexterity+=2
elif playerAncestry == "4":
    print("That will be a Wizard.")
    playerWisdom+=2
elif playerAncestry == "5":
    print("So a Human? smart choice!")
else:
    print("Thats not a real ancestry. Please restart.")
print("Amazing. Lets set up your attributes.")
if playerAncestry == "1":
    print('''
        As a human, you get two free Boosts
        You can boost your [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma
    ''')
    playerSpeed = 25
    playerHealth = 8
    isChoosing = True
    while isChoosing is True:
        playerBoost1 = input("Your first boost is to : ")
        playerBoost2 = input("Your second boost is to : ")
        if playerBoost1 == playerBoost2:
            print("You can't boost the same ability twice")
        else:
            if playerBoost1 == "S" or playerBoost2 == "S":
                playerStrength += 1
            elif playerBoost1 == "D" or playerBoost2 == "D":
                playerDexterity += 1
            elif playerBoost1 == "C" or playerBoost2 == "C":
                playerConstitution += 1
            elif playerBoost1 == "I" or playerBoost2 == "I":
                playerIntelligence += 1
            elif playerBoost1 == "W" or playerBoost2 == "W":
                playerWisdom += 1
            elif playerBoost1 == "Ch" or playerBoost2 == "Ch":
                playerCharisma += 1
            isChoosing = False

elif playerAncestry == "2":
    print('''
        As a dwarf, you take a penalty to Charisma.
        You can boost your Constitution or your Strength and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 20 feet per round and you start with 10 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [C]onstitution or your [S]trength? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerCharisma += -1
    if playerBoost1 == "S" or playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost1 == "C" or playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

elif playerAncestry == "2":
    print('''
        As an elf, you take a penalty to Strength.
        You can boost your Dexterity or your Intelligence and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 30 feet per round and you start with 6 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10
elif playerAncestry == "4":
    print('''
            As an Wizard, you take a penalty to Strength.
            You can boost your Dexterity or your Intelligence and you get one free boost.
            [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

            Your Speed is 30 feet per round and you start with 6 Health.
        ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 10
    playerHealth = 20
elif playerAncestry == "5":
    print('''
        As an Wizard, you take a penalty to Strength.
        You can boost your Dexterity or your Intelligence and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 30 feet per round and you start with 6 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 10
    playerHealth = 20
