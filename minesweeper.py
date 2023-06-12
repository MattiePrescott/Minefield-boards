# this function prints out the input board in a 2d array.
def mine_field(board):
    for inner_list in board:
        for board in inner_list:
            print(board, end = " ")
        print()
        
 # this function takes the input from the original board and creates a new board showing how many mines there are in area near the value.      
def location(board):
    n = len(board)
    if(n == 0):
        return
    compass = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    m = len(board[0])
    new_board = [["#" for j in range(m)] for i in range(n)]
    for r in range(n):
        for c in range(m):
            if(board[r][c] == "-"):
                count = 0
                for direction in compass:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if(nr >= 0 and nr < n and nc >=0 and nc < m and board[nr][nc] == "#"):
                        count = count + 1
                new_board[r][c] = count
    return new_board

# original input board.
board = [["#", "-", "#", "-", "#"],
        ["-", "#", "-", "#", "-"],
        ["-", "-", "-", "-", "#"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "#", "-"]]

print("Mine Field input")
# this runs the mine field function.
mine_field(board)
# this runs the location function.
new_board = location(board)

print("Mine locator")
# this prints out the location grid in a 2d array.
for x in new_board: 
    for i in x:  
        print(i, end = " ")  
    print()  