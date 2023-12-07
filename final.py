import random
import argparse

class Player:
    """Creates player object. Created by ** Ethan Holley **
        Attributes:
            leadership_board (dict): dictionary for score keeping
            name (str): name of Player
            score (int): score of Player
            words (list): list of words
    """
    def __init__(self,name):
        self.leadership_board = {}
        self.name = name
        self.score = 0
        self.words = []

    def __repr__(self):
        return f"Player(name: '{self.name}', score: {self.score})"
    
class Game(Player):
     
    
    def __init__(self, letters, valid_words_file="valid_words_file.txt"):
        """ 
        Created by Cameron Okolita 
        Techniques: super(). and Optional Parameters 

        """ 
        
        super().__init__("Player 1")
        self.letters = letters
        self.valid_words = self.load_valid_words(valid_words_file)
        
    def load_valid_words(self,valid_words_file):
        """  Loads valid words from a text file
        **Nolan Bowen**

        Args:
            valid_words_file (str): Path to a text file containing valid words
                based on scramble

        Returns:
            list: List of valid words from the text file, if file is not found
                an empty list is returned
        """
        try:
            with open(valid_words_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print( f"Error: File {valid_words_file} not found")
            return []
        
  
    def is_entry_valid(self, entry):
        """Check the word entry to make sure its valid.
        created by ** Matt Andrasik **
        
        Args:
            entry (str): word that the player submits as an entry for points
            
        Returns:
            bool: True if word is valid, False if not.
        """
        entry_letters = list(entry)
        
        for letter in entry_letters:
            if entry_letters.count(letter) > self.letters.count(letter):
                return False
        
        if entry in self.valid_words:
            return True
        
        return False
        
        
    def longest_word(self): 
        """
    Get the longest word from a player from the list of valid words.

    Returns:
        str or None: The longest valid word found or None if no valid words.
    
    created by ** Cameron Okolita**
    """
    
        
        if self.valid_words:
            longest_words = max(self.valid_words, key=lambda x: len(x[0]))
            return longest_words[0]
        else:
            return None  
    
    
    """
    features of our game class that allows the user to play
    the anagram game
    """
    def calculate_points(self,word):
        """ Calculates the points the user gets based on length of word found
        created by **Nolan Bowen**

        Args:
            word (str): word found by user

        Returns:
            str: points based on length of word found as long as
                word length is >= 3
        """
        word_len = len(word)
        points = word_len * 100 if word_len >= 3 else 0
        self.leadership_board[self.name] = points
        return points
    
    def print_results(self, player1, player2):
        """ Prints a detailed breakdown of player 1's and player 2's list of
        words and points each word is worth. Created by ** Suhas Poturaju **
        
        EDIT THIS FOR ONLY 1 PLAYER 
        
        Args:
        
        
        """
        for word in player1.words:
            total1 += calculate_points(word)
        for word in player2.words:
            total2 += calculate_points(word)
            
        print(f"Player 1: {total1} pts")
        for word in player1.words:
            print(f"{word} - {calculate_points(word)}")
        
        print("\n---------------------\n")
        
        print(f"Player 2: {total2} pts")
        for word in player2.words:
            print(f"{word} - {calculate_points(word)}")
            
        print("\n---------------------\n")

        
        if total1 == total2:
            print("IT'S A DRAW!")
        elif total1 > total2:
            print(f"PLAYER 1 WON BY {total1 - total2} PTS!")
        else:
            print(f"PLAYER 2 WON BY {total2 - total1} PTS!")
        
      
      
    def leadership_board(self):
        """ Displays the names and scores of players 

        Returns:
            str: number that player placed, their name, and their score
            
        created by ** Matt Andrasik **
        """
        ordered_board = sorted(self.leadership_board.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for i in range(len(ordered_board)):
            place = i + 1
            name, score = ordered_board[1]
            result += f'{place}. {name} : {score}'
    
    def play_game(self):
        """ Method to play the Anagram Game.
        
        Args:
            letters (str): the letters for the game
            
            this method initiates the Game with the provided letters and enter
            word matches until they decide to quit. each word gives points to
            the player and the game results are returned in the end
        """
        print("Welcome to Anagrams!!")
        
        wordlist_file = "letter_scramble.txt"
        self.letters = random.choice(self.load_valid_words(wordlist_file))
        
        print(f"Unscramble the letters: {self.letters}")
        
        while True:
            user_input = input("Enter a word (or 'quit' to end game: )")
            
            if user_input == 'quit':
                break
            
            if self.is_entry_valid(user_input):
                points = self.calculate_points(user_input)
                self.score += points
                self.words.append(user_input)
                print(f"Valid word! {user_input} is worth {points} PTS.
                      your total score is {self.score}.")
            else:
                print("Invalid word. Try again!")
        print("Game Over. Final score is:")
        self.print_results()
        
def main():
    """
        Create command line interface and instantiate Game class.

        Returns: string representation of Game.

        ** created by Ethan Holley **
    """
    parser = argparse.ArgumentParser(description='Anagram Game')
    parser.add_argument('letters', type=str, help='Letters for the Anagram Game')
    parser.add_argument('-w', '--wordsfile', type=str, default='valid_words.txt', help='Path to the file containing valid words')

    args = parser.parse_args()

    game_instance = Game(args.letters, args.wordsfile)
    game_instance.play_game(args.letters)
    print(str(game_instance))

if __name__ == "__main__":
    game_instance = Game("","")
    game_instance.play_game()
