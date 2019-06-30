class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        words = string.split()

        if len(pattern) != len(words):
            return False

        mapping = {}

        for i in range(len(pattern)):
            try:
                # Check the mapping of the character to word matches
                if pattern[i] != mapping[words[i]]:
                    return False
            except KeyError:
                if pattern[i] in mapping.values():
                    return False
                mapping[words[i]] = pattern[i]

        return True
