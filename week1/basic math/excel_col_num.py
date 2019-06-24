class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        exp = 0
        for c in s[::-1]:
            num += ((ord(c) % 65) + 1) * (26 ** exp)
            exp += 1

        return num
