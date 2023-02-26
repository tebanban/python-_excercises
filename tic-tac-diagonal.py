def diagonal_winner(board):
    
   
    all_equal1= True
    all_equal2= True
    top_first = board[0][0]
    top_last = board[0][-1]
    for i in range(len(board)):
          
            if board[i][i ] == " " or board[i][i] != top_first:
                
                all_equal1 = False
            if board[i][-i -1] == " " or board[i][-i -1] != top_last:
                
        
                
                all_equal2 = False
    return all_equal1 or all_equal2
               
               
       
       
   

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O', 'X'],
            [' ', 'O', 'X', ' '],
            ['X', 'X', ' ', 'X'],
            ['X', ' ', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['X', 'X', ' '],
            ['X', ' ', 'O'],
            [' ', 'O', 'O']
        ]
    ),
    False
)