# SUDOKU


## Description:

Sudoku, also known as Su Doku, popular form of number game.

Sudoku consists of a 9 × 9 grid with numbers appearing in some of the squares.

The object of the puzzle is to fill the remaining squares, using all the numbers 1–9 exactly once in each row, column, and the nine 3 × 3 subgrids.

## Rules:

1.Every square has to contain a single number.


2.The numbers from 1 to 9 can be used.


3.Each 3x3 box ,column,row can only contain a number from 1 to 9-No duplications allowed.

## Approach:

1.We used lists to take input from the user. Incase if the user enters the number which is out of range then it prompts to enter the valid number between the range.

2.Next task is to solve the puzzle.We just defined a function in which we just perform the checking operations based on the rules of Sudoku puzzle i.e,row checking and column checking,3x3 grid checking-No Duplicates.

3.Number will be assigned to the cell if all the above conditions are satisfied.

4.We defined a function to print the puzzle,if the input given by the user is not sufficient to solve the puzzle it displays "not possible".
