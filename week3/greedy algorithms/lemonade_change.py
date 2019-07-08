class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif b == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True


                
