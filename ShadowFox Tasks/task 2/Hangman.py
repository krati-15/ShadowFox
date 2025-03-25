import random

# Hangman visuals
HANGMAN_PICS = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Word list with hints
word_list = {
    "python": "A popular programming language",
    "guitar": "A musical instrument with strings",
    "elephant": "A large animal with a trunk",
    "ocean": "A vast body of saltwater",
    "basketball": "A sport played with a hoop and a ball"
}

# Choose a random word and hint
word, hint = random.choice(list(word_list.items()))
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()  # Letters guessed correctly
wrong_guesses = 0  # Incorrect attempts

# Game loop
while wrong_guesses < len(HANGMAN_PICS) - 1:
    print(HANGMAN_PICS[wrong_guesses])  # Show hangman
    print(f"Hint: {hint}")  # Show hint

    # Display current progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", " ".join(display_word))

    # Get user input
    guess = input("\nGuess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter!\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("🔄 You already guessed that letter!\n")
        continue

    # Process the guess
    if guess in word_letters:
        guessed_letters.add(guess)
        print("✅ Correct!\n")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!\n")

    # Check if the word is fully guessed
    if word_letters.issubset(guessed_letters):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print(HANGMAN_PICS[wrong_guesses])  # Final hangman state
    print("\n💀 Game Over! The word was:", word)
