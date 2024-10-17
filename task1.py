import random

def select_random_word():
    words = ["python", "hangman", "programming", "development", "challenge"]
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        current_progress = display_current_progress(word, guessed_letters)
        print(f"Current progress: {current_progress}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
