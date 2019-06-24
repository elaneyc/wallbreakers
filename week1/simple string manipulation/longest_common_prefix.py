class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        longest_possible = min(strs)

        for i in range(len(longest_possible)):
            for word in strs:
                if word[i] != longest_possible[i]:
                    return longest_possible[:i]
        return longest_possible
                    
