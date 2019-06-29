class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        codes = {}

        # Map morse codes to characters and add to dictionary
        for i in range(len(morse)):
            if morse[i] not in codes:
                codes[chr(ord('a') + i)] = morse[i]

        transformations = set()

        # Find unique transformations
        for word in words:
            trans = ""
            for c in word:
                trans += codes[c]
            transformations.add(trans)

        return len(transformations)
