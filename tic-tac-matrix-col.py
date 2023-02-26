def assert_equal(actual, expected):
	    if actual == expected:
	        print("OK")
	    else:
	        print(f"Error! {repr(actual)} != {repr(expected)}")

  
    
def column_winner(board):
   
    for col in range(len(board[0])):
        all_equal = True
        letter =  board[0][col]
        for row in board:
            if row[col] == " " or row[col] != letter:
                all_equal = False
                break
        if all_equal:
            return True
    return False
    
        
assert_equal(
    column_winner(
        [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['O', 'X', ' ']
        ]
    ),
    False
)
assert_equal(
    column_winner(
        [
            ['X', 'O', ' ', 'X'],
            [' ', 'O', 'X', 'O'],
            ['O', 'O', 'X', 'X'],
            ['O', 'O', 'X', ' ']
        ]
    ),
    True
)