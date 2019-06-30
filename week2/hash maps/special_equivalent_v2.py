class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        unique = {}

        for word in A:
            histogram = {"even": {}, "odd": {}}
            
            # Create dictionary tracking number of characters in odd/even indices
            for i in range(len(word)):
                if i % 2 == 0:
                    histogram["even"][word[i]] = (histogram["even"].get(word[i], 0) + 1)
                else:
                    histogram["odd"][word[i]] = (histogram["odd"].get(word[i], 0) + 1)

            # Add to unique
            if histogram not in unique.values():
                unique[word] = histogram

        return len(unique)
