class Solution:
    # O(1) time | O(1) space bc board is a fixed size
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create empty set values for rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                currValue = board[row][col]
                # skip empty cells 
                if currValue == ".":
                    continue 
                # calculate box idx
                box_idx = (row // 3) * 3 + (col // 3)
                # Check for duplicates
                if currValue in rows[row] or currValue in cols[col] or currValue in boxes[box_idx]:
                    return False 
                # add value to sets 
                rows[row].add(currValue)
                cols[col].add(currValue)
                boxes[box_idx].add(currValue)

        # all checks passed
        return True 