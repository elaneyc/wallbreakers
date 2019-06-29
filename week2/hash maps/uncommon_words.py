import collections

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # Count words in both sentences
        aWords = collections.Counter(A.split())
        bWords = collections.Counter(B.split())

        uncommon = set()

        # Find words that appear once
        for word in aWords:
            if aWords[word] == 1 and word not in bWords:
                uncommon.add(word)
        for word in bWords:
            if bWords[word] == 1 and word not in aWords:
                uncommon.add(word)

        return uncommon
