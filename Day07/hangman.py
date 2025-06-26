#Import required modules and assets
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

#Initialise game settings
lives = 6                                               # Total lives a player has
print(logo)                                             # Randomly select a word from the list
chosen_word = random.choice(word_list)
#print(chosen_word)                                       # Debug: Show the chosen word (can be removed to make it harder)

# Create the initial placeholder (e.g., "_____" for a 5-letter word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Set up initial game state
game_over = False
correct_letters = []                                    # Track correctly guessed letters

# Game loop: runs until player wins or loses
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    # Inform the user if they’ve already guessed this letter
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Update the display based on the current guess
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)               # Store correct guess
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # End the game if no lives are left
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check for win condition (no underscores left)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display current hangman ASCII art based on remaining lives
    print(stages[lives])
