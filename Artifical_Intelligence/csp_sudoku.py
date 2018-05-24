#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.  

'''
Construct and return sudoku CSP models.
'''

from cspbase import *
import itertools
import math

def sudoku_csp_model_1(initial_sudoku_board):

    '''Return a CSP object representing a sudoku CSP problem along 
       with an array of variables for the problem. That is return

       sudoku_csp, variable_array

       where sudoku_csp is a csp representing sudoku using model_1
       and variable_array is a list of lists

       [ [  ]
         [  ]
         .
         .
         .
         [  ] ]

       such that variable_array[i][j] is the Variable (object) that
       you built to represent the value to be placed in cell i,j of
       the sudokup board (indexed from (0,0) to (8,8))

       
       
       The input board is specified as a list of 9 lists. Each of the
       9 lists represents a row of the board. If a 0 is in the list it
       represents an empty cell. Otherwise if a number between 1--9 is
       in the list then this represents a pre-set board
       position. E.g., the board
    
       -------------------  
       | | |2| |9| | |6| |
       | |4| | | |1| | |8|
       | |7| |4|2| | | |3|
       |5| | | | | |3| | |
       | | |1| |6| |5| | |
       | | |3| | | | | |6|
       |1| | | |5|7| |4| |
       |6| | |9| | | |2| |
       | |2| | |8| |1| | |
       -------------------
       would be represented by the list of lists
       
       [[0,0,2,0,9,0,0,6,0],
       [0,4,0,0,0,1,0,0,8],
       [0,7,0,4,2,0,0,0,3],
       [5,0,0,0,0,0,3,0,0],
       [0,0,1,0,6,0,5,0,0],
       [0,0,3,0,0,0,0,0,6],
       [1,0,0,0,5,7,0,4,0],
       [6,0,0,9,0,0,0,2,0],
       [0,2,0,0,8,0,1,0,0]]
       
       
       This routine returns Model_1 which consists of a variable for
       each cell of the board, with domain equal to {1-9} if the board
       has a 0 at that position, and domain equal {i} if the board has
       a fixed number i at that cell.
       
       Model_1 also contains BINARY CONSTRAINTS OF NOT-EQUAL between
       all relevant variables (e.g., all pairs of variables in the
       same row, etc.), then invoke enforce_gac on those
       constraints. All of the constraints of Model_1 MUST BE binary
       constraints (i.e., constraints whose scope includes two and
       only two variables).
    '''
    
#IMPLEMENT
    csp_model = CSP("model")
    lst_var = []


    for row in range(0,9):
        lst_var.append([])
        for col in range(0,9):
            if initial_sudoku_board[row][col] == 0:
                newVar = Variable((str(row),str(col)), [1,2,3,4,5,6,7,8,9])
                csp_model.add_var(newVar)
                lst_var[row].append(newVar)
            else:
                newVar = Variable((str(row),str(col)), [initial_sudoku_board[row][col]])
                csp_model.add_var(newVar)
                lst_var[row].append(newVar)


    d = [1,2,3,4,5,6,7,8,9]
    a = (itertools.permutations(d,2))
    sat_tuples = []
    #print(a)

    for p in a:
        if p[0] != p[1]:
            sat_tuples.append(p)

    #print(sat_tuples)

    #rows
    for r in range(0,9):
        for p in itertools.permutations(lst_var[r], 2):
            newCon = Constraint(("Row",str(r)),p )
            newCon.add_satisfying_tuples(sat_tuples)
            csp_model.add_constraint(newCon)




    lst_col = []

    for p in zip(*lst_var):
        lst_col.append(p)

    for c in range(0,9):
        for pt in itertools.permutations(lst_col[c],2):
            newCon = Constraint(("Col", str(c)),pt)
            newCon.add_satisfying_tuples(sat_tuples)
            csp_model.add_constraint(newCon)








    for thrr in range(0,3):
        for thic in range(0,3):
            sq_lst = []
            for r in range(0,3):
                for c in range(0,3):
                    sq_lst.append(lst_var[3*thrr+r][3*thic+c])


            for pte in itertools.permutations(sq_lst,2):
                newCon = Constraint("Square", pte)
                newCon.add_satisfying_tuples(sat_tuples)
                csp_model.add_constraint(newCon)







    return (csp_model,lst_var)



##############################

def sudoku_csp_model_2(initial_sudoku_board):
    '''Return a CSP object representing a sudoku CSP problem along 
       with an array of variables for the problem. That is return

       sudoku_csp, variable_array

       where sudoku_csp is a csp representing sudoku using model_1
       and variable_array is a list of lists

       [ [  ]
         [  ]
         .
         .
         .
         [  ] ]

       such that variable_array[i][j] is the Variable (object) that
       you built to represent the value to be placed in cell i,j of
       the sudokup board (indexed from (0,0) to (8,8))

    The input board takes the same input format (a list of 9 lists
    specifying the board as sudoku_csp_model_1.
    
    The variables of model_2 are the same as for model_1: a variable
    for each cell of the board, with domain equal to {1-9} if the
    board has a 0 at that position, and domain equal {i} if the board
    has a fixed number i at that cell.

    However, model_2 has different constraints. In particular, instead
    of binary non-equals constaints model_2 has 27 all-different
    constraints: all-different constraints for the variables in each
    of the 9 rows, 9 columns, and 9 sub-squares. Each of these
    constraints is over 9-variables (some of these variables will have
    a single value in their domain). model_2 should create these
    all-different constraints between the relevant variables, then
    invoke enforce_gac on those constraints.
    '''

#IMPLEMENT
    csp_model = CSP("model2")
    lst_var = []

    for row in range(0,9):
        lst_var.append([])
        for col in range(0,9):
            if initial_sudoku_board[row][col] == 0:
                newVar = Variable((str(row),str(col)), [1,2,3,4,5,6,7,8,9])
                csp_model.add_var(newVar)
                lst_var[row].append(newVar)
            else:
                newVar = Variable((str(row),str(col)), [initial_sudoku_board[row][col]])
                csp_model.add_var(newVar)
                lst_var[row].append(newVar)

    d = [1,2,3,4,5,6,7,8,9]
    a = (itertools.permutations(d,9))
    sat_tuples = []


    for i in range(0,9):
        lst = []
        for j in range(0,9):
            lst.append(lst_var[i][j])
        newCon = Constraint("all",lst)
        newCon.add_satisfying_tuples(a)
        csp_model.add_constraint(newCon)

    #col

    for i in range(0,9):
        lst = []
        for j in range(0,9):
            lst.append(lst_var[j][i])
        newCon = Constraint("all",lst)
        newCon.add_satisfying_tuples(a)
        csp_model.add_constraint(newCon)
    #square
    for thrr in range(0,3):
        for thic in range(0,3):
            sq_lst = []
            for r in range(0,3):
                for c in range(0,3):
                    sq_lst.append(lst_var[3*thrr+r][3*thic+c])

            newCon= Constraint("sq", sq_lst)
            newCon.add_satisfying_tuples(a)
            csp_model.add_constraint(newCon)




    #print(lst_var)
    return (csp_model,lst_var)




    
