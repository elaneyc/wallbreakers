class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False

        s_lets = {}

        # Add all letters in s to dictionary
        for c in s:
            if c not in s_lets:
                s_lets[c] = 1
            else:
                s_lets[c] += 1

        for c in t:
            # If the character was not in s, not an anagram
            if c not in s_lets:
                return False
            else:
                s_lets[c] -= 1
                # If the number of letters not equal, not an anagram
                if s_lets[c] < 0:
                    return False
        return True
