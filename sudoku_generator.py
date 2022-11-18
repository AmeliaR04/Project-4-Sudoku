def SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        #Constructor for the SudokuGenerator class.
        #For the purposes of this project, row_length is always 9.
        #removed_cells could vary depending on the difficulty level chosen (see “UI Requirements”).

    def valid_in_row(self, row, num):
        #Returns a Boolean value.
        #Determines if num is contained in the given row of the board.

    def valid_in_col(self, col, num):
        #Returns a Boolean value.
        # if num is contained in the given column of the board.

    def valid_in_box(self, row_start, col_start, num):
        #Returns a Boolean value.
        #Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)

    def is_valid(self, row, col, num):
        #Returns if it is valid to enter num at (row, col) in the board.
        #This is done by checking the appropriate row, column, and box.

    def fill_box(self, row_start, col_start):
        #Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
        #Uses unused_in_box to ensure no value occurs in the box more than once.

    def fill_diagonal(self):
        #Fills the three boxes along the main diagonal of the board.
        #This is the first major step in generating a Sudoku.
        #See the Step 1 picture in Sudoku Generation for further explanation.

    def fill_remaining(self, row, col):
        #This method is provided for students.
        #It is the second major step in generating a Sudoku.
        #This will return a completely filled board (the Sudoku solution).

    def fill_values(self):
        #This method is provided for students.
        #It constructs a solution by calling fill_diagonal and fill_remaining.

    def remove_cells(self):
        #This method removes the appropriate number of cells from the board.
        #It does so by randomly generating (row, col) coordinates of the board and setting the value to 0.
        #Note: Be careful not to remove the same cell multiple times. A cell can only be removed once.
        #This method should be called after generating the Sudoku solution.

    def generate_sudoku(size, removed):
        #Note: This is a function outside of the SudokuGenerator class.
        #This function should also be implemented in sudoku_generator.py as it interacts with the class.
        #Given size and removed, this function generates and returns a size-by-size sudoku board.
        #The board has cleared removed number of cells.
        #This function should just call the constructor and appropriate methods from the SudokuGenerator class.



