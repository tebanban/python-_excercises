

def row_winner(board):
    for row in board:
        all_equal= True
        letter = row[0]
        for str in row:
            if str == " " or letter != str:
                all_equal = False
                break
        if all_equal:
            return True
    return False        
        
assert_equal(
    row_winner(
        [
            ['A', 'A', 'B', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)
assert_equal(
    row_winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
    ),
    True
)    
 