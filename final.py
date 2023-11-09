class Game:
     def __init__(self, letters): 
        self.letters = letters 
        self.valid_words = [] 
        
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
        return points
    def __repr__(self):
        """
        can use this magic method to show the players name and score that round
        could evantually implement it to show a high score. **Nolan Bowen**
        """
        return f"Player(name:'{self.name}', score:{self.score})"
