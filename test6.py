
# Guessing Game Challenge

# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!


from random import randint

choice = randint(1,100)

guesses = [0]

while True:

    guess = int(input('Please guess a correct number:'))

    if guess <1 or guess >100:
        print('Out of Bounds')
        continue

    if guess == choice :
        
        print('correct')

        break
    
    guesses.append(guess)

    if guesses[-2]:

        if abs(guess-choice) < abs(choice-guesses[-2]):
            print('Warm')
        else:
            print('cold')
    else:

        if abs(guess-choice)<=10:
            print('Warm')
        else:
            print('cold')







