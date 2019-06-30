class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        map_s, map_t = {}, {}
        code_s, code_t = '', ''
        '''
        def check(s, t):
            mapping = {}
            for i in range(len(s)):
                try:
                    if t[i] != mapping[s[i]]:
                        return False
                except KeyError:
                    mapping[s[i]] = t[i]
            return True
        return check(s, t) and check(t, s)
