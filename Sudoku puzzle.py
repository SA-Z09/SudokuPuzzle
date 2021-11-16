  # Firstly, finding the next empty row and column on the board  and return -1
    # If no space is left and entire board is filled then return row and column tuple 
 # our range is 0-8 
from pprint import pprint
def find_next_empty(puzzle):

    for r in range(9):  
        for c in range(9): # range(9) is 0, 1, 2, ... 8  
            if puzzle[r][c] == -1:     #returning the value in Rth and Cth coluumn
                return r, c            #If it equals none then return r,c

    return None, None                  # If no more empty spaces 

def is_valid(puzzle, guess, row, col):   #Checking the process 
   
    row_vals = puzzle[row]               #Checking on the row
    if guess in row_vals:
        return False                      #If returned TRUE then all okay, if not then there is a issue.

  
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False                       #If guess is there we return FALSE 

   
    row_start = (row // 3) * 3            #Checking the square
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):         #Checking in three rows
        for c in range(col_start, col_start + 3):     #Checking in three rows
            if puzzle[r][c] == guess:
                return False                          #If false then the value is in the row/column

    return True
#If it's true then placing the guess into row/column 
def solve_sudoku(puzzle):
   
    
    # step 1: Making a guess

    row, col = find_next_empty(puzzle)

    # 1- if there's no empty place left, then we are okay
    if row is None:  # this is true if our function gives us NONE
        return True 
    
    # 2- if it's empty then place numbers between 1-9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # 3- if it's valid then place it there
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        # 4- if not valid or our guess does not solve the puzzle, then we need to try other number and we need to reset
    
        puzzle[row][col] = -1            #Restting the value in row/column

    # 5- if we get nothing in return then we cannot solve the puzzle 
    return False

if __name__ == '__main__':
    sudoku_trial = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(sudoku_trial))
    print(sudoku_trial)
