import os, re, random, images, words, wordseasy

while True:
    lives = 7
    missedLetters = []
    gameWon = False


    def check_letter(letter, word):
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
        os.system('clear')
        print(images.hangman[7 - lives])
        print(' '.join([str(e) for e in reveal]))
        print('\nYou have', lives, 'lives.')
        print('Missed letters/words:', ' '.join([str(x) for x in missedLetters]))


    diff = ''
    while not (diff == 'easy' or diff == 'hard'):
        diff = input('What difficulty? [easy/hard] ')  # HARD not working!
        diff = diff.lower()

        if diff == 'hard':
            word = random.choice(words.hangman_words)
            word = word.upper()
        elif diff == 'easy':
            word = random.choice(wordseasy.hangman_words_easy)
            word = word.upper()
        else:
            print('Invalid answer. Try again.')

    reveal = list(len(word) * '_')

    while gameWon == False and lives > 0:
        status()
        guess = input('Guess a letter or an entire word: ')
        guess = re.sub(r'[^A-Za-z]', '', guess)
        guess = guess.upper()

        if guess == word:
            gameWon = True
            reveal = word
        elif len(guess) == 1 and guess in word:
            gameWon = check_letter(guess, word)
        elif guess in word:
            gamewon = check_letter(guess,word)
        else:
            lives -= 1
            missedLetters.append(guess)
        status()

    if gameWon:
        disdiff = diff.lower()
        print('Well done! You are a winner! You ended with',lives,'lives on',disdiff,'difficulty!')
    else:
        print('Oh no! You failed! The word was: ' + word + '.')
        if not lives == 0:
            print('You ended with',lives,'lives.')
        else:
            print('You ended with no lives.')
        os.system('clear')
