class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        score = 0
        stack = []

        for p in S:
            if p == "(":
                stack.append(p)
            else:
                temp = stack.pop()
                temp_score = 0
                if temp != "(":
                    while temp != "(":
                        temp_score += 2*temp
                        temp = stack.pop()
                if temp_score != 0:
                    stack.append(temp_score)

                elif temp == "(":
                    stack.append(1)

        if len(stack) != 0:
            score = sum(stack)

        return score
                    
