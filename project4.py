import random
import time
playerhealth = random.randint(100,150)
monsterhealth = random.randint(90,160)
print("You are a knight traveling across the land, slaying monsters and saving kingdoms")
time.sleep(2)
print("\nYou spot an ogre terrorizing a village!")
time.sleep(1)
#turn loop starts here, repeats lines 11-69
for i in range (17):
    time.sleep(1)
    print(f"\nYou have {playerhealth} health, the monster has {monsterhealth} health.")
    choice = input("\nDo you: \n \n A: Heal yourself \n \n B: Attack the ogre? \n \n")
    if choice == "A" or choice == "a" or choice == "Heal" or choice == "heal":
        print("")
        healamount = random.choice([0,1,2,4,9,10,11,25,35])
        playerhealth += healamount
        time.sleep(1)
        print(f"You healed {healamount} health")
    elif choice == "B" or choice == "b" or choice == "Attack" or choice == "attack":
        print("")
        time.sleep(1)
        bethisdabest = random.randint([1,50])
        if bethisdabest == 50:
            monsterdamage = 100
            print("BethIsDaBest!!!")
        else:
            monsterdamage = random.choice([0,1,2,3,4,7,8,9,10,11,12,13,20])
        monsterhealth -= monsterdamage
        print(f" The monster took {monsterdamage} damage!")
        if monsterhealth <= 0:
            print("Huzzah! You successfully vanquished the ogre! The village is safe!")
            exit()
    attacktype = random.randint(1,3)
    time.sleep(1)
    pregnancy2appliances1 = random.randint([1,50])
    if pregnancy2appliances1 == 50:
        playerdamage = 100
        print("PREGANCY, PREGNANCY, APPLIANCES!!")
    elif attacktype == 1:
        print("\nThe ogre swings its club at you!")
        playerdamage = random.choice([0,1,12,15])
        time.sleep(1)
        if playerdamage == 0:
            print("\nPhew! It missed!")
        elif playerdamage == 1:
            print("\nThe club hits the ground right next to you, missing you by a hair!")
    elif attacktype == 2:
        print("")
        print("\nThe ogre stomps its foot, shaking the ground!")
        playerdamage = random.choice([3,5,7,9])
    elif attacktype == 3:
        print("")
        print("\nThe ogre swings its calloused hand, attempting to grab you!")
        time.sleep(1)
        playerdamage = random.choice([0,1,5,7,8,9])
        if playerdamage == 0:
            print("\nIt misses you entirely!")
        elif playerdamage == 0:
            print("\nIts hand whooshes past you, the wind blowing you slightly off-balance.")
        else:
            print(f"\n It grabs you! You take {playerdamage} damage.")
            time.sleep(1)
            escapechance = random.randint(0,3)
            if escapechance == 3:
                falldamage = random.randint(0,3)
                print(f"\nYou manage to squirm out of the beast's hand! You fall onto the ground, taking {falldamage} extra damage.")
                playerdamage += falldamage
            else:
                grabdamage = random.choice([3,4,7,8])
                print(f"\nThe ogre squeezes you, dealing {grabdamage} damage before letting you go.")
                playerdamage += grabdamage
    time.sleep(1)
    print(f"\n You take a total of {playerdamage} damage.")
    playerhealth -= playerdamage
    if playerhealth <= 0:
        print("\nThe ogre has ended your life. It rampages through the village, destroying buildings and people alike. Perhaps next time, you will find success.")
    #turn loop ends here!
if playerhealth <= 0:
    exit()
elif monsterhealth <= 0:
    exit()
else:
    ending = random.randint(0,3)
    if ending == 0:
        print("\nYou took so long, the ogre collapsed from exhaustion!")
    elif ending == 1:
        print("\nThe ogre grows tired of fighting and runs past you, destroying the village as you chase after it.")
    elif ending == 2:
        print("\nYou take so long that both you and the ogre collapse from exhaustion.")
    else:
        print("\nYou take so long that the ogre grows bored and eats you.")
    exit()