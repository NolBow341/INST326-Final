# INST326-Final Anagrams Word Game
##### created by: Nolan Bowen, Suhas Poturanju, Ethan Holley, Cameron Okolita, Matt Andrasik

#### How to run the program:
1. CTRL + SHIFT + ~ to open a new terminal.
2. write the following: python3 (or python for windows) final.py
3. find words from the scrambled letters and have fun!

# Python Files:

### Final.py
Player class:
__init__ :initializes the objects

__repr__ :formal representation of string

__str__ :informal representation of string

__get_highest_score__: gets the highest score based on game played 

overview of the player. allows the game to set basic requirments like name, score, and words
magic methods are provided to return proper string formations


__Game class__:

how the game operates: inherits the Player class.

methods include:

__init__ :initializes the objects

__leadership_board__: shows the rank of the player based on the round they play

__load_valid_words__: loads the words from a textfile in order to get points

__calculate points__: gives points based on players input and word length

__is_entry_valid__: assesses weather word typed is valid or not

__print_results__: detailed breakdon of players words found and points given

__play_game__: how the game is displayed when playing. allows user to input responses 

__lucky_points__: chooses number from two tuples and gives bonus points if they matched 

### letter_scramble.txt
a textfile of scrambled letter combonations, these letter combonations will be chosen at random when the code is run



### valid_words.txt
list of all the valid words that can be found based on the letter scrambled combonation


# Attribution
__Nolan Bowen__:

Method/Function: load_valid_words and calculate_points.

Techniques demonstrated: With and Conditonal Expression

__Matt Andrasik__:

Method/function: Leadership_board and is_entry_valid

Techniques demonstrated: Lambda expression and sequence unpacking



__Cameron Okolita__:

Method/Function: play_game and __init__ from Game class.

Techniques demonstrated: super() and optional parameters


__Ethan Holley__: 

Method/Function: main() and Player/Game class, lucky_points

Techniques demonstrated: Argument Parser and set operations or forzensets


__Suhas Poturanju__:

Method/Function: __repr__,__str__print,_results

Techniques demonstrated: magic methods and f-strings







