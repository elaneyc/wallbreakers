import collections

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        unique = {}

        for word in A:
            histogram = {}
            length = len(word)

            # Create dictionary tracking number of characters in odd/even indices
            even = [word[i] for i in range(0, length, 2)]
            odd = [word[i] for i in range(1, length, 2)]

            histogram["even"] = collections.Counter(even)
            histogram["odd"] = collections.Counter(odd)

            # Add to unique
            if histogram not in unique.values():
                unique[word] = histogram

        return len(unique)
