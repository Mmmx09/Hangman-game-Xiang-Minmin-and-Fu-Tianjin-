import random

# This function selects a random six-letter word from a list of words
def select_word():
    with open('words.txt') as file:
        # Read all the words and split them by lines
        words = file.read().splitlines()  
        # Keep only words that have + than six letters
    six_letter_words = [word for word in words if len(word) >= 6]  
    # Choose a random word from words list
    return random.choice(six_letter_words)  

# This function shows the word with guessed letters and hides the unguessed ones with underscores
def display_word(word, guessed_letters):
    display = ''
    # boucle for every letter
    for letter in word:  
         # If the letter has been guessed
        if letter in guessed_letters:  
            # Show the letter with space
            display += letter + ' '  
        else:
            # Hide the letter with an underscore and space
            display += ' _ '  
    # Return the word with guessed and hide letters
    return display.strip()  

# This is the main game function where the player guesses the word letter by letter
def play():
    #take a words plus or equal to 6 letters
    word = select_word() 
    # remind the guess letters of the player
    guessed_letters = []  
    #  six chance to be wrong
    remaining_guesses = 6  
    # score starts at zero
    score = 0  

    print("Welcome to Hangman!")
     # Show the word as underscores
    print("Your word is: " + '_ ' * len(word)) 
    # Keep playing until the player runs out of guesses
    while remaining_guesses > 0:  
        print("\nWord: " + display_word(word, guessed_letters))  
        # Ask to guess a letter
        guess = input("Guess a letter: ").upper()  # Ask the player to guess a letter
         # If the player already guessed this letter
        if guess in guessed_letters: 
             # guessed it before
            print("You already guessed that letter.") 
        # If the guessed letter is in the word
        elif guess in word: 
            # tell the player
            print(f"Good guess! {guess} is in the word.")  
             # Add the letter to the list of guessed letters
            guessed_letters.append(guess) 
        else:
            # -1 guess
            remaining_guesses -= 1  
            print(f"Sorry, {guess} is not in the word. You have {remaining_guesses} guesses left.")
            # Add the letter to the list of guessed letters
            guessed_letters.append(guess)  # Add the letter to the list of guessed letters

        # Check if the player has guessed all the letters in the word
        if all(letter in guessed_letters for letter in word):
             # win
            print(f"Congratulations! You guessed the word: {word}") 
             # Add 50 points for winner
            score += 50 
            break
    else:
        # lose
        print(f"Sorry, you ran out of guesses. The word was: {word}")  
         # Take away 30 points for loser
        score -= 30 
    # Show the player's score
    print(f"Your score: {score} points")  

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play()  
    else:
        #end
        print("Thanks for playing Hangman!") 

# Start the game
play_game()