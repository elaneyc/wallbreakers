class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_dist = 0
        counter = 0
        seen_one = False
        binary = bin(N)

        for i in range(len(binary)):
            if ((binary[i] == '1') and (not seen_one)):
                seen_one = True
            elif ((binary[i] == '0') and (seen_one)):
                counter += 1

            elif ((binary[i] == '1') and (seen_one)):
                counter += 1
                if counter > max_dist:
                    max_dist = counter
                counter = 0

        return max_dist
