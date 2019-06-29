import collections

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        num_unique = len(set(candies))

        if  num_unique >= len(candies)/2:
            return len(candies)/2
        else:
            return num_unique
        
