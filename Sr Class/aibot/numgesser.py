import random

# Step 1: Computer selects a random number from 1 to 10
secret_number = random.randint(1, 10)

# Step 2: Keep asking the user to guess until correct
while True:
    # Step 3: Get user input and convert to int
    guess = int(input("Guess a number between 1 and 10: "))

    # Step 4: Use if...else to check guess
    if guess == secret_number:
        print("🎉 You guessed it!")
        break
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again")

     