from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Create character counts for s
        sCount = Counter(s)

        # Create dictionary to track character counts in t
        tCount = {}

        # There are two cases for the different character in t:
        # 1. it already appears in s, in which case the count will be 1 more than s
        # 2. it does not appear in s

        # Check these conditions:
        for i in range(len(t)):
            if t[i] in tCount:
                tCount[t[i]] += 1
            else:
                tCount[t[i]] = 1

            # Check case 2
            if t[i] not in sCount:
                return t[i]

            # Check case 1
            if sCount[t[i]] < tCount[t[i]]:
                    return t[i]


            
