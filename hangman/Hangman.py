from wordgenerator import wordgenerator
from tablegenerator import tablegenerator
from rules import rules
from replace import replace
from check import check
from vowelcheck import vowelcheck
from remover import remover
from scorecalc import scorecalc

SecretWord,nwords = wordgenerator()
table,length = tablegenerator(SecretWord)
print(f"Loading word list from file...\n{nwords} words loaded.\nWelcome to the game Hangman!")
i = input("Do you wish to know the rules of the game? Press 'Y' for yes and 'N' for no.").upper()
if i == "Y":
    rules()
input("Press enter when ready...")
print("Let's Play!\nI am thinking of a word that is {} letters long.".format(length))

guesses = 6
warnings = 3
aval = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("You have {} warnings left".format(warnings))

while True:
    
    print("-------------")
    print("You have {} guesses left".format(guesses))
    print("Available letters: ",*aval)
    guess = input("Please guess a letter: ").lower()
    
    if guess in SecretWord and guess in aval:
        replace(SecretWord,guess,table)
        print("Good Guess: ",*table)
        remover(guess,aval)
    elif guess not in aval and check(guess):
        warnings -= 1
        print("Oops! You've already guessed that letter.")
        print("You have",warnings,"warnings left: ",*table)
    elif guess not in SecretWord and check(guess):
        print("Oops! That letter is not in my word: ",*table)
        remover(guess,aval)
        if vowelcheck(guess):
            guesses -= 2
        else: guesses -= 1
    else:
        print("Please enter valid character")
        warnings -= 1
        if warnings>0 :
            print("You have",warnings,"warnings left: ",*table)
        
    if warnings <= 0:
        print("You have no warnings left so you lose one guess: ",*table)
        guesses -= 1
        warnings = 3
        
    if guesses <= 0:
        print("-----------\nSorry, you ran out of guesses.")
        print("The word was",SecretWord)
        break
    
    if "_" not in table:
        print("------------\nCongratulations, you won!")
        score = scorecalc(guesses,table)
        print("Your total score for this game is:",score)
        break
