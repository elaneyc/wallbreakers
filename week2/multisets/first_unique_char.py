from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = -1
        chars = {}
        single = {}

        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 1
                single[s[i]] = i

                # If first is undefined, then this is the first single char
                if first == -1:
                    first = i
            else:
                chars[s[i]] += 1

                if s[i] in single:
                    del single[s[i]]

                if s[first] == s[i]:
                    if len(single) > 0:
                        first = min(single.values())
                    else:
                        first = -1

        return first
