import collections
import unittest


# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            # If value in current col or row or in the square before
            if (board[r][c] in rows[r] or board[r][c] in cols[c] 
                or board[r][c] in squares[(r//3,c//3)]):
                return False
            
            # update all hash map
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])

    return True


class TestSudokuValidation(unittest.TestCase):
    def test_valid_sudoku(self):
        valid_board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
        self.assertTrue(isValidSudoku(valid_board))

    def test_invalid_row(self):
        invalid_row_board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '3', '.', '7', '9']
        ]
        self.assertFalse(isValidSudoku(invalid_row_board))

    def test_invalid_column(self):
        invalid_column_board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '3']
        ]
        self.assertFalse(isValidSudoku(invalid_column_board))

    def test_invalid_subbox(self):
        invalid_subbox_board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['4', '1', '9', '.', '.', '.', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '2']
        ]
        self.assertFalse(isValidSudoku(invalid_subbox_board))

    def test_empty_board(self):
        empty_board = [['.'] * 9 for _ in range(9)]
        self.assertTrue(isValidSudoku(empty_board))


if __name__ == '__main__':
    unittest.main()