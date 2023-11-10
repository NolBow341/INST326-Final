class Player:
    """Creates player object. 
    created by ** Ethan Holley **
    """
    def __init__(self,name):
        self.leadership_board = {}
        self.name = name
        self.score = 0
class Game(Player):

    def __init__(self, letters): 
        self.letters = letters 
        self.valid_words = [] 
        
  
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
            str: points based on length of word found
        """
        word_len = len(word)
        if word_len > 3:
            points = word_len * 100
        else: 
            points = 0
        self.leadership_ship[self.name] = points
        return points
        
    def leadership_board(self):
        """ Displays the names and scores of players 

        Returns:
            str: number that player placed, their name, and their score
        """
        ordered_board = sorted(self.leadership.item(), key=lambda x: x[1], reverse=True)
        for name, score in ordered_board:
            place += 1
            return f"{place}. {name} : {score}" 
    def __repr__(self):
        """
        can use this magic method to show the players name and score that round
        could evantually implement it to show a high score. **Nolan Bowen**
        """
        return f"Player(name:'{self.name}', score:{self.score})"
