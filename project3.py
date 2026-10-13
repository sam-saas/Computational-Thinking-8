right = 0
wrong = 0
QA = 0

print("Welcome to my quiz! I'll ask you five questions, if you get three wrong you fail!")
input()
q1 = input("\nWhat's my favorite movie? \nA: How To Train Your Dragon \nB: Ginger Snaps \nC: Black Widow\n")
if q1 == "A" or q1 == "a":
    print("\nWRONG!")
    wrong += 1
elif q1 == "B" or q1 == "b":
    print("\nCorrect!")
    right += 1
elif q1 == "C" or q1 == "c":
    print("\nWrong, but it is one of my favorites!")
    wrong += 1
QA += 1
q2 = input("\nWhat's my Starbucks order? \nA: iced brown sugar oatmilk shaken espresso \nB: iced brown sugar oatmilk shaken espresso with pumpkin spice \nC: Mocha frappuccino with the whipped cream mixed in\n")
if q2 == "A" or q2 == "a" or q2 == "C" or q2 == "c":
    print("\nWRONG!")
    wrong += 1
elif q2 == "B" or q2 == "b":
    print("\nCorrect!")
    right += 1
QA += 1
q3 = input("\nWhat am I excited for next tri? \nA: Going to Italy \nB: My stepsister's wedding \nC: Being in the musical\n")
if q3 == "A" or q3 == "a" or q3 == "B" or q3 == "b":
    print("\nWRONG!")
    wrong += 1
elif q3 == "C" or "c":
    print("\nCorrect!")
    right += 1
QA +=1
if wrong == 3:
    print("\nWow, you managed to get the first three wrong already. FAILLLL!!!")
    print(f"\nQuestions answered right: {right} \nQuestions answered wrong: {wrong} \nTotal questions answered: {QA}")
else:
    q4 = input("\nWhat pet do I want? \nA: Western Hognose Snake \nB: Tanuki, aka raccoon dog \nC: Tortoiseshell Maine Coon cat\n")
    if q4 == "B" or q4 == "b" or q4 == "C" or q4 == "c":
        print("\nWRONG!")
        wrong += 1
    elif q4 == "A" or q4 == "a":
        print("\nCorrect!")
    right += 1
    QA +=1
    if wrong == 3:
        print("\nYou got 3 wrong, you fail!")
        print(f"\nQuestions answered right: {right} \nQuestions answered wrong: {wrong} \nTotal questions answered: {QA}")
    else:
        q5 = input("\nWhat's my favorite color? \nA: Black \nB: Navy \nC: Green\n")
        if q5 == "A" or q5 == "a":
            print ("\nWRONG!")
            wrong +=1
        elif q5 == "B" or q5 == "b":
            print("\nWRONG!!")
            print("\nNavy is my LEAST FAVORITE color!!!!!")
            wrong +=1
        elif q5 == "C" or q5 == "c":
            print("\nCorrect!")
            right += 1
        if wrong == 3 and QA == 5:
            print("\nYou got 3 wrong! you FAIL!")
            print("So close...")
            print(f"\nQuestions answered right: {right} \nQuestions answered wrong: {wrong} \nTotal questions answered: {QA}")
        else:
            print("\nYOU WIN!!!")
            print(f"\nYou got {right}/5 right!")
            if right == 5:
                print("Great job! You aced it!")
            else:
                print("Good job!")