class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punctuations = "',;.?!"
        for p in punctuations:
            paragraph = paragraph.replace(p, " ")

        # Split paragraph into words
        para_words = paragraph.lower().split()

        # find words
        most_common = ""
        appearances = 0
        words = {}
        for word in para_words:
            if word not in banned:
                words[word] = words.get(word, 0) + 1
                if words[word] > appearances:
                    most_common = word
                    appearances = words[word]

        return most_common

        
