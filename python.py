puzzle = []
N = 9
print("Enter Numbers")
for i in range(N):
    List1 = []
    for j in range(N):
        value = int(input("Value -- "))
        if (value>N):
            value = int(input("Value -- "))
            List1.append(value)
        else:
            List1.append(value)
    puzzle.append(List1)
 

def printing(puzzle):
    for i in range(N):
        for j in range(N):
            print(puzzle[i][j], end = " ")
        print()
 

def isSafe(puzzle, row, col, num):
   
    
    for x in range(9):
        if puzzle[row][x] == num:
            return False
 
   
    for x in range(9):
        if puzzle[x][col] == num:
            return False
 
   
    startRow = ( row // 3 ) * 3
    startCol = ( col // 3 ) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + startRow][j + startCol] == num:
                return False
    return True
 

def solveSuduko(puzzle, row, col):
   
    
    if (row == N - 1 and col == N):
        return True
       
    
    if col == N:
        row += 1
        col = 0
 
    
    if puzzle[row][col] > 0:
        return solveSuduko(puzzle, row, col + 1)
    for num in range(1, N + 1, 1):
       
        
        if isSafe(puzzle, row, col, num):
           
            
            puzzle[row][col] = num
 
            
            if solveSuduko(puzzle, row, col + 1):
                return True
 
        
        puzzle[row][col] = 0
    return False
 

 
if (solveSuduko(puzzle, 0, 0)):
    print("The solution is :")
    printing(puzzle)
else:
    print("no solution  exists ")