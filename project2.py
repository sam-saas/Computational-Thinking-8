print("you crash-land in a forest on your way to nationals.")
thing1 = input("do you: A. try to save yourself or B. try to save the other passengers on the plane, aka your teammates.")
if thing1 == "A" or thing1 == "a":
    print("you make it out scot-free, but none of your teammates are lucky enough to join you.")
    TC = "no"
    health = "100"
    thing2 = input("now that you're out of the burning plane, do you: A. go back in for materials B. survey the wilderness or C. check for what you might already have")
    if thing2 == "A" and TC == "yes" or thing2 == "a" and TC == "yes":
        print("the team captain offers to go in for you. She finds a few protein bars, seven bottles of water, and a piece of paper that seems to be a map of between your point of departure and your destination.")
    elif thing2 == "A" and TC == "no" or thing2 == "a" and TC == "no":
        print("you find a couple of protein bars, a few bottles of water, and a piece of paper that seems to be a map of between your point of departure and your destination, but end up scraping your arm on a piece of jagged metal.")
        health = "80"
    elif thing2 == "B" or thing2 == "b":
     print("you spot no signs of humanity.")
     print("you find scraps of metal a good size for self-defense and edible mushrooms you recognize from pamphlet on the plane.")

    elif thing2 == "C" and TC == "yes" or thing2 == "c" and TC == "yes":
        print("you check your bag and find a melted protein bar and a warm bottle of water, the team captain checks hers and finds a stick of beef jerky and a sweatshirt.")
    elif thing2 == "c" and TC == "no" or thing2 == "C" and TC == "no":
     print("you check your bag and find a bottle of water and a sweatshirt.")
    else:
        print("uh-oh! you didn't respond correctly and a grizzly bear ate you")
elif thing1 == "B" or thing1 == "b":
    print("you sustained some injuries pulling the team captain out of the plane, but she's grateful and decides that your odds are better if she sticks with you.")
    TC = "yes"
    health = "80"
    thing2 = input("now that you're out of the burning plane, do you: A. go back in for materials B. survey the wilderness or C. check for what you might already have")
    if thing2 == "A" and TC == "yes" or thing2 == "a" and TC == "yes":
        print("the team captain offers to go in for you. She finds a few protein bars, seven bottles of water, and a piece of paper that seems to be a map of between your point of departure and your destination.")
    elif thing2 == "A" and TC == "no" or thing2 == "a" and TC == "no":
        print("you find a couple of protein bars, a few bottles of water, and a piece of paper that seems to be a map of between your point of departure and your destination, but end up scraping your arm on a piece of jagged metal.")
        health = "80"
    elif thing2 == "B" or thing2 == "b":
     print("you spot no signs of humanity.")
     print("you find scraps of metal a good size for self-defense and edible mushrooms you recognize from pamphlet on the plane.")
     input()
     print("Walking further, you find a stream. You remember the old survival tip that flowing water is safer, and that you can follow rivers and streams when lost.")
     thing6 = input("Do you A. drink the water or B. follow it to safety?")
     if thing6 == "a" or "A":
        print("You bend down to sip the water. It's cold and has a mineral-y taste to it, but you're too thirsty to care.")
        input()
        if  TC == "no":
           print("For the next few days, you survive off of mushrooms and return to the stream to drink. Things are looking hopeful, or at least as hopeful as it can get when you're the sole survivor of a plane crash that all of your friends were on.")
        if TC == "yes":
           print("For the next few days, you survive off of mushrooms and return to the stream to drink. Things are looking hopeful, or at least as hopeful as it can get when you're one of two survivors of a plane crash that all of your friends were on.")
        input()
        print("But after another day or two, you start getting stomachaches. You're dehydrated, exhausted, and scared.")
        input()
        if TC == "yes":
            print("The next day, both you and TC wake up with fevers.")
        elif TC == "no":
           print("The next day, you wake up with a fever.")
        input()
        print("FIN.")
        print("")
        print("cause of death:")
        print("SICKNESS FROM DRINKING CONTAMINATED WATER")
     if thing6 == "b" or "B":
        print("You follow the stream for a while, walking along its edge.")
        input()
        print("All of a sudden, your foot catches on a pebble.")
        input()
        print("The water rushes over you as you fall in. It's deeper than you thought, and it's near impossible to get out.")
        input()
        print("FIN.")
        print("Cause of death:")
        print("DROWNING.")

    elif thing2 == "C" and TC == "yes" or thing2 == "c" and TC == "yes":
        print("you check your bag and find a melted protein bar and a warm bottle of water, the team captain checks hers and finds a stick of beef jerky and a sweatshirt.")
    elif thing2 == "c" and TC == "no" or thing2 == "C" and TC == "no":
     print("you check your bag and find a bottle of water and a sweatshirt.")
     input()
    else:
        print("uh-oh! you didn't respond correctly and a grizzly bear ate you")
        health = "0"
        input()
        print("FIN.")
        print("")
        print("Cause of death:")
        print("GRIZZLY BEAR")
    print("The plane has stopped smoking, but it seems like everything inside has burnt to ash.")
    if thing2 == "a" or "A":
       thing3 = input("Would you like to A. check the map or B. use it to start a fire. ")
       if thing3 == "A" or "a":
        print("You find where you are from the shapes of the mountains nearby, and spot a town that looks to be only a small trek ")
        thing4 = input("Do you A. Wait for rescue, or B. Try to find, then hike to the town.")
        print()
        if thing4 == "A" or thing4 == "a":
             print("You wait for rescue in the cold, keeping your eyes on the sky. ")
             input()
             print("As dawn comes, the stars dim, as does your hopes.")
             input()
             print("You keep waiting throughout the day, barely moving. When nighttime comes, the temperature has dropped so low that you feel like your blood has frozen.")
             input()
             print("You didn't make it through the cold winter night.")
             input()
             print("FIN.")
             print("")
             print("Cause of death:")
             print("HYPOTHERMIA")
        else:
            print 
            print("You gather all your belongings and begin hiking towards the town, map in hand.")
            input()
            print("A heavy wind comes in and tugs furiously at the map!")
            print("")
            print("The top of the map has been torn off, you're now traveling based on instinct alone.")
            thing5 = input("You come across a branching path. Do you A. go on the left side of the path or B. the right side?")
            if thing5 == "A" or "a":
               print("You turn left and keep walking.")
               print("After what seems like an eternity, you hear the sounds of civilization!")
               print("")
               print("You immediately talk to the first person you find, explaining your situation.")
               input()
               if TC == "yes":
                  print("Apparently, there's already a protocol for this. A helicopter will arrive to take you tomorrow, and the stranger has offered to let you and TC stay in their guest bedroom for the night.")
                  input()
                  print("You fill your growling stomachs with warm food, and you and TC get all your mild injuries patched up.")
                  input()
                  print("TC falls asleep first, while you lie in bed, eagerly awaiting tomorrow's events.")
                  input()
                  print("FIN.")
                  
               else:
                  print("Apparently, there's already a protocol for this. A helicopter will arrive to take you tomorrow, and the stranger has offered to let you stay in their guest bedroom for the night.")
                  input()
                  print("You fill your growling stomach with warm food, and you get all your mild injuries patched up.")
                  input()
                  print("You finally fall asleep, awaiting tomorrow's events.")
                  input()
                  print("FIN.")
       if thing4 == "b" or "B":
          print("The warmth brings you some comfort, but you begin to shiver again when you realize you burnt your only hope for survival.")
          input()
          print("FIN.")
          print("Cause of death:")
          print("UNKNOWN. anything could happen in the forest.")
    if thing2 == "C" or "c":
       input()
       print("you ration your water, but you still run out in a few days. You search for anything flammable, but it's all damp from a recent rain.")
       input()
       print("you're wandering the area, searching for mushrooms for food, when you spot a beehive.")
       input()
       print("out of desperation, you try to grab a piece of honeycomb.")
       input()
       print("you got stung by so many bees that you died.")
       input()
       print("FIN.")
       print("Cause of death:")
       print("ANAPHYLAXIS FROM REACTION TO BEE VENOM")
       

else:
    print("uh-oh! you didn't respond correctly in time and you didn't make it out the plane.")
    health = "0"
    input()
    print("FIN.")
    print("Cause of death:")
    print("FIRE")
