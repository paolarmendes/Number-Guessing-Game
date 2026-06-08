import random
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nYou have 5 chances to guess the correct number.")
print("\nPlease select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)")
userChoice= int(input("\nEnter your choice: "))
if userChoice == 1:
    print("\nGreat! You have selected the Easy difficulty level. \nLet's start the game!")
    x = random.randrange(1, 100)
    y = 0
    for i in range (1, 11):
        userGuess = int(input("\nEnter your guess: "))
        if userGuess == x:
            print(f"\nCongratulations! You guessed the correct number in {y} attempts.")
        elif userChoice > x:
            print(f"\nIncorrect! The number is less than {userGuess}.")
        else:
            print(f"\nIncorrect! The number is more than {userGuess}.")
        y+=1
    print(f"The number was {x}")

elif userChoice == 2:
    print("\nGreat! You have selected the Medium difficulty level. \nLet's start the game!")
    x = random.randrange(1, 100)
    y = 0
    for i in range (1, 6):
        userGuess = int(input("\nEnter your guess: "))
        if userGuess == x:
            print(f"\nCongratulations! You guessed the correct number in {y} attempts.")
        elif userChoice > x:
            print(f"\nIncorrect! The number is less than {userGuess}.")
        else:
            print(f"\nIncorrect! The number is more than {userGuess}.")
        y+=1
    print(f"The number was {x}")
elif userChoice == 3:
    print("\nGreat! You have selected the Hard difficulty level. \nLet's start the game!")
    x = random.randrange(1, 100)
    y = 0
    for i in range (1, 4):
        userGuess = int(input("\nEnter your guess: "))
        if userGuess == x:
            print(f"\nCongratulations! You guessed the correct number in {y} attempts.")
        elif userGuess > x:
            print(f"\nIncorrect! The number is less than {userGuess}.")
        else:
            print(f"\nIncorrect! The number is more than {userGuess}.")
        y+=1
    print(f"The number was {x}")

