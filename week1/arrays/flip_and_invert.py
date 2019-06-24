class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped = A[:]

        # reverse each row
        for row in flipped:
            for i in range(0, len(row)/2):
                index_to_swap = (len(row) - 1)- i
                temp = row[i]
                row[i] = row[index_to_swap]
                row[index_to_swap] = temp

        # invert image
        for row in flipped:
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0

        return flipped
