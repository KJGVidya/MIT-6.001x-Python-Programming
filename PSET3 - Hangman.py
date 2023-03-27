# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random

WORDLIST_FILENAME = "C:/Users/jvidy/OneDrive/Documents/Learnings/Python/Edx/MIT 6.001 Python/words.txt"

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
    #return set(secretWord).intersection(lettersGuessed)==set(secretWord)
    return all([1 if i in lettersGuessed else 0 for i in secretWord])



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return " ".join([i if i in lettersGuessed else "_" for i in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return "".join(["" if i in lettersGuessed else i for i in string.ascii_lowercase])
    

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
    
    
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ", len(secretWord), "letters long.")
    print("-------------")
    guess=8#guessCount(secretWord,letter)
    availableLetters=getAvailableLetters("")
    letters=""
    while guess>0:
       
        print("You have",guess,"guesses left.")
        print("Available letters: ",availableLetters, end="\n")
        letter=input("Please guess a letter: ").lower()
        if letter in secretWord and  letter in availableLetters: 
            letters+=letter
            print("Good guess:", getGuessedWord(secretWord, letters))
            print("-------------")
            #print("letters",letters)
            if isWordGuessed(secretWord, letters):
                print("Congratulations, you won!")
                break
        elif letter not in secretWord and letter  in availableLetters:
            print("Oops! That letter is not in my word:",getGuessedWord(secretWord, letters))
            print("-------------")
            letters+=letter
            guess-=1
        else:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, letters))
            print("-------------")
        
                        
        availableLetters=getAvailableLetters(letters)   
    

    print("Sorry, you ran out of guesses. The word was",secretWord,".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist)
hangman(secretWord)


