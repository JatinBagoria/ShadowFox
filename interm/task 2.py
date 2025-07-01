import random

# List of words
words = ['python', 'shadowfox', 'internship', 'hangman', 'developer', 'laptop', 'keyboard']
chosen_word = random.choice(words)

# Game setup
guessed_letters = []
attempts_left = 6
display_word = ["_" for _ in chosen_word]

print("\n🎮 Welcome to Hangman!")
print("Word to guess:", " ".join(display_word))

while attempts_left > 0 and "_" in display_word:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[i] = guess
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print("❌ Wrong guess. Attempts left:", attempts_left)

    print("Word:", " ".join(display_word))

# End result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game over! The word was:", chosen_word)

# Play again
play_again = input("\nDo you want to play again? (y/n): ").lower()
if play_again == 'y':
    exec(open(__file__).read())  # restart the script
else:
    print("Thanks for playing Hangman! 👋")
