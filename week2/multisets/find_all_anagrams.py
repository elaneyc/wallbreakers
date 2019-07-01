from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        indices = []

        if len(s) < len(p):
            return indices

        sChars = Counter(s[0:len(p)])
        pChars = Counter(p)

        if sChars == pChars:
            indices.append(0)

        for i in range(len(p), len(s)):
            if s[i] in sChars:
                sChars[s[i]] += 1
            else:
                sChars[s[i]] = 1

            sChars[s[i - len(p)]] -= 1
            if sChars[s[i - len(p)]] == 0:
                del sChars[s[i - len(p)]]

            # Check if current substring of s is an anagram of p
            if sChars == pChars:
                indices.append(i - (len(p)-1))

        return indices
        
