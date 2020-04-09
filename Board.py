class Board:
    """ a data type for a Connect Four board with arbitrary dimensions"""

    def __init__(self, height, width):
        """ a constructor for Board objects """

        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for r in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object """
        s = ''

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  # newline at the end of the row

        dashes = self.width + 1 + self.width
        s += "-" * dashes
        s += '\n'

        for index in range(self.width):
            s += ' ' + str(index % 10)

        return s

    def add_checker(self, checker, col):
        """ adds a checker that is either an X or O"""

        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = 0
        while row < self.height:
            if self.slots[row][col] == ' ':
                row += 1
            elif self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                row -=1
                break
        
        if row == self.height:
            row -= 1

        self.slots[row][col] = checker

    def reset(self):
        """ reset the board by setting all slots to space characters"""

        self.slots = [[' '] * self.width for r in range(self.height)]


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """checks if it is valid to place a checker in column col"""

        if col >= self.width or col < 0:
            return False
        elif self.slots[0][col] == 'X' or self.slots[0][col] == 'O':
            return False
        else:
            return True


    def is_full(self):
        """returns True if the called Board object is completely full of
            checkers and False otherwise"""

        for x in range(self.width):
            if self.can_add_to(x) == True:
                return False

        return True

    def remove_checker(self,col):
        """removes the top checker form a column col"""

        row = 0
        while row < self.height:
            if self.slots[row][col] == ' ':
                row += 1
            elif self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break
            
    def is_win_for(self, checker):
        """returns True if there are 4 consecutive slots containing checker
            and False otherwise"""

        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        return False


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ checks for vertical win of specified character"""

        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """checks for down diagonal win of a specified character"""

        for row in range(3, self.height):
            for col in range(3, self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row -1][col -1] == checker and \
                   self.slots[row -2][col -2] == checker and \
                   self.slots[row -3][col -3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """checks for up diagonal win of a specified character"""

        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row -1][col +1] == checker and \
                   self.slots[row -2][col +2] == checker and \
                   self.slots[row -3][col +3] == checker:
                    return True
        return False
                
        
  
