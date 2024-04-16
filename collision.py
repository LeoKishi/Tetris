

class Collision:
    def bottom_is_empty(self, array: list[list[int]]) -> bool:
        '''Checks for obstacles under the piece. Returns False if blocked, True otherwise.'''
        positions = self.get_positions(array)
        for pos in positions:
            x, y = pos[0], pos[1]
            if x+1 >= 24 or array[x+1][y][0] == 2:
                return False
        return True


    def right_is_empty(self, array: list[list[int]]) -> bool:
        '''Checks for obstacles to the right of the piece. Returns False if blocked, True otherwise.'''
        positions = self.get_positions(array)
        for pos in positions:
            x, y = pos[0], pos[1]
            if y+1 >= 10 or array[x][y+1][0] == 2:
                return False
        return True


    def left_is_empty(self, array: list[list[int]]) -> bool:
        '''Checks for obstacles to the left of the piece. Returns False if blocked, True otherwise.'''
        positions = self.get_positions(array)
        for pos in positions:
            x, y = pos[0], pos[1]
            if y-1 < 0 or array[x][y-1][0] == 2:
                return False
        return True


    def get_positions(self, array: list[list[int]]) -> list[tuple[int, int]]:
        '''Returns the position of every square that make up the piece.'''
        positions = []
        for x in range(24):
            for y in range(10):
                if array[x][y][0] == 1:
                    positions.append((x,y))
        return positions


    def side_is_blocked(self, piece: list[list[int]], pos: tuple[int, int]) -> bool:
        '''Returns True if rotation puts the piece out of bounds (sides), returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        y = pos[1]
        for i in range(height):
            for j in range(width):
                if not self.in_bounds(y=y+j) and piece[i][j] == 1:
                    return True
        return False
    

    def bottom_is_blocked(self, piece: list[list[int]], pos: tuple[int, int]) -> bool:
        '''Returns True if rotation puts the piece out of bounds (bottom), returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        x = pos[0]
        for i in range(height):
            for j in range(width):
                if not self.in_bounds(x=x+i) and piece[i][j] == 1:
                    return True
        return False
    

    def is_overlapping(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int]) -> bool:
        '''Returns True if rotation causes the piece to overlap with another piece, returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1]
        for i in range(height):
            for j in range(width):
                if array[x+i][y+j][0] == 2 and piece[i][j] == 1:
                    return True
        return False
    

    def try_move_up(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int], step: int = 1) -> bool:
        '''Returns True if the piece can be moved up by the specified amount of steps, returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0] - step, pos[1]
        for i in range(height):
            for j in range(width):
                if not self.in_bounds(x=x+i) and piece[i][j] == 1:
                    return False
                elif  self.in_bounds(x=x+i, y=y+j) and array[x+i][y+j][0] == 2 and piece[i][j] == 1:
                    return False
        return True


    def try_move_right(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int], step: int = 1) -> bool:
        '''Returns True if the piece can be moved right by the specified amount of steps, returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1] + step
        for i in range(height):
            for j in range(width):
                if not self.in_bounds(y=y+j) and piece[i][j] == 1:
                    return False
                elif self.in_bounds(x=x+i, y=y+j) and array[x+i][y+j][0] == 2 and piece[i][j] == 1:
                    return False
        return True


    def try_move_left(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int], step: int = 1) -> bool:
        '''Returns True if the piece can be moved left by the specified amount of steps, returns False otherwise.'''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1] - step
        for i in range(height):
            for j in range(width):
                if not self.in_bounds(y=y+j) and piece[i][j] == 1:
                    return False
                elif self.in_bounds(x=x+i, y=y+j) and array[x+i][y+j][0] == 2 and piece[i][j] == 1:
                    return False
        return True


    def in_bounds(self, x=False, y=False) -> bool:
        '''Checks if x and/or y is inside bounds.'''
        if y is False:
            if x >= 0 and x < 24:
                return True
        elif x is False:
            if y >= 0 and y < 10:
                return True
        else:
            if (x >= 0 and x < 24) and (y >= 0 and y < 10):
                return True





if __name__ == '__main__':




    
    ...