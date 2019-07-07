class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {}

        for b in bills:
            difference = b - 5

            # Check if there is enough change
            while difference > 0:
                if difference >= 10:
                    if change.get(10, 0) < 1 and change.get(5, 0) < 2:
                        return False
                    else:
                        if change.get(10, 0) > 0:
                            change[10] -= 1
                        else:
                            change[5] -= 2
                        difference -= 10
                elif difference == 5:
                    if change.get(5, 0) < 1:
                        return False
                    else:
                        change[5] -= 1
                        difference -= 5

            # Add the bill to the cashbox
            change[b] = change.get(b, 0) + 1

        return True
