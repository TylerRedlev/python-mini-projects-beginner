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

#importing the random module
import random

#opening the document 'words_list.txt' and assigning it as variable f. We make python read the lines of the file f and assign it as the variable 'content'
with open('words_list.txt') as f:
    content = f.readlines()

#remove whitespaces from characters characters like `\n` at the end of each line
content = [lines.strip() for lines in content]

