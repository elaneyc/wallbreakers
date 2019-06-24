class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if (digits[-1] + 1 < 10):
            digits[-1] += 1
        else:
            carry = False
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] + 1 >= 10:
                    carry = True
                    digits[i] = (digits[i] + 1) % 10
                else:
                    digits[i] += 1
                    break

                if carry and (i == 0):
                    digits.insert(0, 1)


        return digits
                
