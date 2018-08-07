# Hangman game
#This problem will implement a function, an interactive Hangman game between a player and the computer.
#Before we get to this function, we'll first implement a few helper functions to get you going.
#For this problem, you will need the code files ps3_hangman.py and words.txt.

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char  not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ''
    space = "_ "
    for char in secretWord:
        if char in lettersGuessed:
            guess += char
        else:
            guess += space
    return guess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avaliableLetters = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if char not in lettersGuessed:
            avaliableLetters += char
    return avaliableLetters
   
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    answer = False
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    print('-------------')
    while guesses != 0 and  not answer:
        print('You have', guesses, 'guesses left.')
        print('Available letters: ',getAvailableLetters(lettersGuessed))
        guess_letter = input(str('Please guess a letter: '))
        if guess_letter in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess_letter)
            if guess_letter in secretWord:
                print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            answer = True
    if answer:
        print('Congratulations, you won!')
    else:
        print("Sorry, you ran out of guesses. The word was else.")
            

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
