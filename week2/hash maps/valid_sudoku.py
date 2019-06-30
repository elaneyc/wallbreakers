class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {} }
        cols = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {} }
        squares = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {} }

        # Always be 9 rows and columns
        ROWS = 9
        COLS = 9
        for i in range(ROWS):
            for j in range(COLS):
                val = board[i][j]
                if val == '.':
                    continue

                r = (i+1) / 3.0
                c = (j+1) / 3.0

                # Determine which square the space is in
                if r <= 1:
                    if c <= 1:
                        square = 1
                    elif c <= 2:
                        square = 2
                    else:
                        square = 3
                elif r <= 2:
                    if c <= 1:
                        square = 4
                    elif c <= 2:
                        square = 5
                    else:
                        square = 6
                else:
                    if c <= 1:
                        square = 7
                    elif c <= 2:
                        square = 8
                    else:
                        square = 9

                # Check if the number has already appeared
                # in the row, column, or square
                if val in rows[i+1] or val in cols[j+1] or val in squares[square]:
                    return False
                else:
                    rows[i+1][val] = 0
                    cols[j+1][val] = 0
                    squares[square][val] = 0

        return True
        
