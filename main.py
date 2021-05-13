import os
import random
import images
import words

my_secret = os.environ['keyToAccess']
word = random.choice(words.hangman_words)
word = word.upper()
reveal = list(len(word)*'_')
lives = 7
gameWon = False

def check_letter(letter,word):
    global reveal
    for i in range(0, len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False

def status():
    os.system("clear")
    print(images.hangman[7-lives])
    print(' '.join([str(e) for e in reveal]))
    print('\nYou have',lives,'lives.')

while gameWon == False and lives > 0:
    status()
    guess = input('Guess a letter or an entire word: ')
    secretguess = guess
    guess = guess.upper()
    if secretguess == my_secret:
        gameWon = True
    
    if guess == word:
        gameWon = True
        reveal = word
    elif len(guess) == 1 and guess in word:
        gameWon = check_letter(guess,word)
    else:
        lives -= 1
    status()

if gameWon:
    print('Well done! You are a winner! You ended with',lives,'lives!')
else:
    print('Oh no! You failed! The word was:', word)