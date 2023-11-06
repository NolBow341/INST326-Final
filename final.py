class Game:
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
        if word_len >= self.word:
            return(word_len - 2) * 100
        else:
            return 0