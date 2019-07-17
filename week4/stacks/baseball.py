class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum = 0

        for item in ops:
            length = len(stack)
            try:
                pts = int(item)
                stack.append(pts)
                sum += pts
            except ValueError:
                if item == "D":
                    if length > 0:
                        double = 2*stack[-1]
                        stack.append(double)
                        sum += double
                elif item == "C":

                    if length > 0:
                        remove = stack.pop()

                        sum -= remove
                elif item == "+":
                    if length >= 2:
                        temp1 = stack.pop()
                        temp2 = stack.pop()
                        summed = temp1 + temp2
                        sum += summed
                        stack.append(temp2)
                        stack.append(temp1)
                        stack.append(summed)

        return sum


                    
