class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)

        s_len = len(s)
        if len(t) < s_len:
            return False


        idx = 0
        matched = 0
        for c in t:
            if idx > s_len or matched == s_len:
                break
            elif c == s[idx]:
                matched += 1
                idx += 1

        return matched == s_len
