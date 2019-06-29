import collections

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stones = collections.Counter(S)


        # Iterate through the jewels and accumulate total
        jewels = 0
        for jewel in J:
            if jewel in stones:
                jewels += stones[jewel]

        return jewels
