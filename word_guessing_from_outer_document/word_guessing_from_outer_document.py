"""
1. THE TASK

Guessing a word from the list.

-Write a python program that may contain a couple of functions (number of functions in your program depends on you, there are no spesific limitations).
-Create a text file which will contain words from which the python program will choose randomly.
-The code allows user to guess the letters of the word which is randomly chosen from a given words_list.
-The words_list will be located in the same folder of your python program and you need to import the list to your python code by defining a function.
A sample output is given in the following lines of comments:

*---------------------------------------------
The word contains 9 letters.
Please enter one letter or a 9-letter word. A
Yes! The word contains 2 "A"s!
***A***A*
*---------------------------------------------

TO WRITE:
1) FUNCTION WHICH WILL COUNT THE LETTER COUNT IN THE WORD
2) ONE LETTER OR WORD INPUT ASKER
3) YES CONTAINS / NO DOESN'T CONTAIN OUTPUT
4) "HOW MANY TRIES APPLIED" COUNTER

"""

#---------------------------------------------------------------
#      IMPORTING MODULES AND ASSIGNING FUNDAMENTAL VARIABLES
#---------------------------------------------------------------

#importing the random module
import random

#opening the document 'words_list.txt' and assigning it as variable f. We make python read the lines of the file f and assign it as the variable 'content'
with open('words_list.txt') as f:
    content = f.readlines()

#CREATED A LIST FROM THE LINES OF OUR WORD FILE - THAT LIST IS CALLED "CONTENT"
#remove whitespaces from characters characters like `\n` at the end of each line
content = [lines.strip() for lines in content]


#WE CHOSE A RANDOM ELEMENT OF THE LIST AND ASSIGNED THAT ELEMENT INTO THE VARIABLE "CHOSEN"
chosen = random.choice(content)


#WE CONVERTED THE CHOSEN STRING ELEMENT INTO A LIST
chosenList = list(chosen)

#WE WRITE THE ACTIVE STATUS OF THE NAME TO BE GUESSED AS ************

activeStatus = list(("*" * len(chosen)))

#WRITING OUT HOW MANY LETTERS THE WORD CONTAINS
print("The word contains {} letters.".format(len(chosen)))


#-----------------------------------------
#           WRITING THE FUNCTIONS
#-----------------------------------------


#INPUT A CHARACTER
def guess_input():

    global guess
    guess = input("Please enter one letter or a {}-letter word:".format(len(chosen)))
    guess = guess.upper()
    print(guess.upper())


#WRITING THE ITERATION FUNCTIONALITY OF THE SELECTED LIST ITEM FOR INPUTTED LETTER
def after_guess_func():
    letter_count = int(chosenList.count(guess))
    if letter_count > 1:
        print("Yes! The word contains the {} '{}'s.".format(letter_count, guess))
    elif letter_count == 1:
        print("Yes! The word contains the letter {}".format(guess))
    else:
        print("Sorry. There are no letters '{}' in this word.".format(guess))



#UPDATING THE ACTIVE STATUS OF THE CHOSEN WORD AFTER A LETTER IS GUESSED
def guess_iteration():
    for i in range(len(chosenList)):
        if chosenList[i] == guess:
            activeStatus[i] = chosenList[i]

    print(''.join(activeStatus))

