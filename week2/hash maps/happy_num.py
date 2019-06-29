class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        num = str(n)
        current_sum = 0

        while current_sum != 1:
            current_sum = 0
            # If num has already been seen, will not be happy bc made full cycle
            if num in seen:
                return False
            else:
                seen.add(num)
                # Add up values
                for i in range(len(num)):
                    current_sum += int(num[i])**2
                num = str(current_sum)

        return True
