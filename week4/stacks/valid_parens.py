class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        # Helper method to return opening brace
        def getOpen(p):
            if p == ")":
                return "("
            elif p == "]":
                return "["
            elif p == "}":
                return "{"

        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            else:
                try:
                    open = stack.pop()
                    if open != getOpen(p):
                        return False
                except:
                    return False

        return len(stack) == 0
