# INST326-Final Anagrams Word Game
##### created by: Nolan Bowen, Suhas Poturanju, Ethan Holley, Cameron Okolita, Matt Andrasik

#### How to run the program:
1. CTRL + SHIFT + ~ to open a new terminal.
2. write the following: python3 (or python for windows) final.py
3. find words from the scrambled letters and have fun!

# Python Files:

### Final.py
Player class:
__init__ initializes the objects

__repr__ formal representation of string

__str__ informal representation of string

get_highest_score: gets the highest score based on game played 

overview of the player. allows the game to set basic requirments like name, score, and words
magic methods are provided to return proper string formations


Game class:

how the game operates: inherits the Player class.

methods include:

__init__ initializes the objects

leadership_board: shows the rank of the player based on the round they play

load_valid_words: loads the words from a textfile in order to get points

calculate points: gives points based on players input and word length

is_entry_valid: assesses weather word typed is valid or not

print_results: detailed breakdon of players words found and points given

play_game: how the game is displayed when playing. allows user to input responses 

lucky_points: chooses number from two tuples and gives bonus points if they matched 

#### letter_scramble.txt
a textfile of scrambled letter combonations, these letter combonations will be chosen at random when the code is run



#### valid_words.txt
list of all the valid words that can be found based on the letter scrambled combonation


# Attribution
Nolan Bowen:
Method/Function: load_valid_words and calculate_points.
techniques demonstrated: With and Conditonal Expression

Matt Andrasik:
method/function: Leadership_board and is_entry_valid
techniques demonstrated: Lambda expression and sequence unpacking



Cameron Okolita:
Method/Function: play_game and __init__ from Game class.
techniques demonstrated: super() and optional parameters


Ethan Holley: 
Method/Function: main() and Player/Game class, lucky_points
techniques demonstrated: Argument Parser and set operations or forzensets


Suhas Poturanju:
Method/Function: __repr__,__str__print,_results
techniques demonstrated: magic methods and f-strings







