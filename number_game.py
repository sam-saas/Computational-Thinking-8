import random

hidden_number = random.randint(1, 30)

#print (hidden_number)

stupidvariable = "no"

guess = int(input("guess a number between 1 and 30!"))
if guess == hidden_number:
    print("Good job, that's correct!")
    quit()
elif 10 > hidden_number:
    print("Wrong! Hint: It's less than 10")
elif 20 < hidden_number:
    print("Wrong! Hint: It's more than 20")
else:
    print("Wrong! Hint: It's in the 20s")
for i in range (8):
    guess = int(input("guess a number between 1 and 30!"))
    if guess == hidden_number:
        print("Good job, that's correct!")
        quit()
    else:
        print("Nope!")
guess = int(input("Last guess! \nGuess a number between 1 and 30!"))
if guess == hidden_number:
    print("Good job, that's correct!")
    quit()
else:
    print("Nope! You lose!")
    print(f"The answer was: \n {hidden_number}")