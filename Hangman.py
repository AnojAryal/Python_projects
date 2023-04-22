import random

# List of words to choose from
words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php', 'mysql', 'mongodb']

# Choose a random word from the list
word = random.choice(words)

# Initialize the game state
correct_guesses = set()
incorrect_guesses = set()
max_guesses = 6


# Helper function to display the current state of the game
def display_game_state():
    # Display the word with underscores for unguessed letters
    displayed_word = ''.join([c if c in correct_guesses else '_' for c in word])
    print('Word:', displayed_word)

    # Display the incorrect guesses
    print('Incorrect guesses:', ', '.join(sorted(list(incorrect_guesses))))

    # Display the hangman drawing
    print('  _______')
    print(' |/      |')
    print(' |      {}{}'.format(' ' if 'head' in incorrect_guesses else '', 'O' if 'head' in incorrect_guesses else ''))
    print(' |      {}{}{}'.format('/' if 'left_arm' in incorrect_guesses else '',
                                  '|' if 'torso' in incorrect_guesses else '',
                                  '\\' if 'right_arm' in incorrect_guesses else ''))
    print(' |      {} {}'.format('/' if 'left_leg' in incorrect_guesses else '',
                                 '\\' if 'right_leg' in incorrect_guesses else ''))
    print(' |')
    print(' |')
    print('_|___')


# Main game loop
while len(incorrect_guesses) < max_guesses and set(word) != correct_guesses:
    display_game_state()

    # Get the user's guess
    guess = input('Guess a letter: ').lower()

    # Check if the guess is correct
    if guess in word:
        correct_guesses.add(guess)
    else:
        incorrect_guesses.add(guess)

# Display the final game state
display_game_state()

# Check if the guesser won or lost
if set(word) == correct_guesses:
    print('Congratulations, you guessed the word:', word)
else:
    print('Sorry, you lost. The word was:', word)
