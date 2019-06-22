class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []

        for i in range(left, right+1):
            self_divides = False
            for j in str(i):
                if int(j) == 0:
                    self_divides = False
                    break
                if i % int(j) == 0:
                    self_divides = True
                else:
                    self_divides = False
                    break
            if self_divides:
                nums.append(i)

        return nums
        
