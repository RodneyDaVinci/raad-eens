import random

print("Welkom to guess the number")
score = 0
for x in range(20):
    if x != 0 and x != 19:
        anotherTime = input("Want to guess again? (Y/N) ").lower()
        if anotherTime == "n":
            print("Okay, goodbye")
            exit()
    print("Round " + str(x+1))
    roundNumber = random.randint(1,10)
    for y in range(10):
        print("")
        print("Take " + str(y+1))
        guess = int(input("What do you think the number is? If you want to stop type -1 "))
        if guess == -1:
            exit()
        print("You have {} guesses".format(guess))
        if guess == roundNumber:
            print("You've guessed it, +1 score")
            score += 1
            break

        if abs(guess - roundNumber) <= 20:
            print("You are really warm")
        elif abs(guess - roundNumber) <= 50:
            print("You are warm")

        if guess > roundNumber:
            print("Lower")
        if guess < roundNumber:
            print("Higher")

        if y == 9:
            print("You sadly lost, next time better!")
    print("")
    print("Score is " + str(score))