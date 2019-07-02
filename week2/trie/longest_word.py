class Solution(object):
    def longestWord(self, words):
        """
         :type words: List[str]
         :rtype: str
        """
        seen = set([""])
        for word in sorted(words, key=len):
            if word[:-1] in seen:
                seen.add(word)
        return max(sorted(seen), key=len)
