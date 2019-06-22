class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        p1 = 0
        p2 = len(s)-1

        while p1 < p2:
            if isVowel(s[p1]) and isVowel(s[p2]):
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            elif not isVowel(s[p1]):
                p1 += 1
            elif not isVowel(s[p2]):
                p2 -= 1
        return ''.join(s)

def isVowel(c):
    c = c.lower()
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
