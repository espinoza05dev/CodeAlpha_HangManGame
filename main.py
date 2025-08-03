import random

# List of words
words = ["person", "animal", "love", "food", "interest"]

# Choose random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("HANGMAN GAME")
print("Guess the word!")

# Main game loop
while wrong_guesses < max_wrong:
    # Show current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(f"\nWord: {display}")
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

    # Check if won
    if "_" not in display:
        print("YOU WON!")
        break

    # Get guess
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("Already guessed that letter!")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check if correct
    if guess in word:
        print("Good guess!")
    else:
        print("Wrong!")
        wrong_guesses += 1

# Check if lost
if wrong_guesses == max_wrong:
    print(f"GAME OVER! The word was: {word}")