from collision import Collision
import piece


collision = Collision()


class Move:
    current_shape = None
    current_piece = None
    angle = None
    current_pos = None
    stored_piece = None


    def rotate(self, array: list[list[int]]):
        '''Rotates the piece in place'''
        self.clear_old_position(array)

        # rotate the piece
        if self.angle == 3:
            self.angle = 0
        else:
            self.angle += 1
        rotated_piece = self.current_piece[self.angle]

        # check if piece is out of bounds (left/right)
        if collision.side_is_blocked(rotated_piece, self.current_pos):
            # try side wall kick
            if new_pos := self.side_bounds_wall_kick(array, rotated_piece):
                self.current_pos = new_pos
            else:
                return 
        
        # check if piece is out of bounds (bottom)
        elif collision.bottom_is_blocked(rotated_piece, self.current_pos):
            # try bottom wall kick
            if new_pos := self.bottom_bounds_wall_kick(array, rotated_piece):
                self.current_pos = new_pos
            else:
                return 
            
        # check if piece is overlapping with another piece
        elif collision.is_overlapping(array, rotated_piece, self.current_pos):
            # try every wall kick
            if new_pos := self.side_bounds_wall_kick(array, rotated_piece):
                self.current_pos = new_pos
            elif new_pos := self.bottom_bounds_wall_kick(array, rotated_piece):
                self.current_pos = new_pos
            else:
                return 

        # place the rotated piece
        self.spawn_piece(array, rotated_piece, self.current_pos, self.current_shape.color)
        

    def side_bounds_wall_kick(self, array: list[list[int]], piece: list[list[int]]):
        '''
        Returns a valid position to relocate the piece to the right or left of the current position.\n
        Returns False if there are no valid positions.
        '''
        x, y  = self.current_pos[0], self.current_pos[1]
        if collision.try_move_right(array, piece, self.current_pos, step=1):
            return (x, y+1)
        elif collision.try_move_left(array, piece, self.current_pos, step=1):
            return (x, y-1)
        elif collision.try_move_right(array, piece, self.current_pos, step=2):
            return (x, y+2)
        elif collision.try_move_left(array, piece, self.current_pos, step=2):
            return (x, y-2)
        else:
            return False


    def bottom_bounds_wall_kick(self, array: list[list[int]], piece: list[list[int]]):
        '''
        Returns a valid position to relocate the piece above the current position.\n
        Returns False if there are no valid positions.
        '''
        x, y  = self.current_pos[0], self.current_pos[1]
        if collision.try_move_up(array, piece, self.current_pos, step=1):
            return (x-1, y)
        elif collision.try_move_up(array, piece, self.current_pos, step=2):
            return (x-2, y)
        else:
            return False


    def down(self, array: list[list[int]]):
        '''Move the current piece one step downwards.'''
        if collision.bottom_is_empty(array):
            self.clear_old_position(array)
            x, y = self.current_pos[0], self.current_pos[1]
            self.current_pos = (x+1, y)
            self.spawn_piece(array, self.current_piece[self.angle], self.current_pos, self.current_shape.color)


    def right(self, array: list[list[int]]):
        '''Move the current piece one step to the right.'''
        if collision.right_is_empty(array):
            self.clear_old_position(array)
            x, y = self.current_pos[0], self.current_pos[1]
            self.current_pos = (x, y+1)
            self.spawn_piece(array, self.current_piece[self.angle], self.current_pos, self.current_shape.color)


    def left(self, array: list[list[int]]):
        '''Move the current piece one step to the left.'''
        if collision.left_is_empty(array):
            self.clear_old_position(array)
            x, y = self.current_pos[0], self.current_pos[1]
            self.current_pos = (x, y-1)
            self.spawn_piece(array, self.current_piece[self.angle], self.current_pos, self.current_shape.color)


    def drop(self, array: list[list[int]]):
        '''Move the current piece to the bottommost position it can be moved to.'''
        while collision.bottom_is_empty(array):
            self.clear_old_position(array)
            x, y = self.current_pos[0], self.current_pos[1]
            self.current_pos = (x+1, y)
            self.spawn_piece(array, self.current_piece[self.angle], self.current_pos, self.current_shape.color)


    def clear_old_position(self, array: list[list[int]]):
        '''
        Removes the current piece from the array.\n
        Used to clear the old position before assigning a new one.
        '''
        for x in range(24):
            for y in range(10):
                if array[x][y][0] == 1:
                    array[x][y][0] = 0
                    array[x][y][1] = ' '
    

    def spawn_piece(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int], color: str):
        '''Creates a new piece on the game grid at the specified position.'''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1]
        for i in range(height):
            for j in range(width):
                if x+i < 24 and y+j < 10 and array[x+i][y+j][0] == 0 and piece[i][j] == 1:
                    array[x+i][y+j][0] = 1
                    array[x+i][y+j][1] = color


    def freeze_piece(self, array: list[list[int]]):
        '''Turns the falling piece into a static piece (value of 2)'''
        positions = collision.get_positions(array)
        for pos in positions:
            x, y = pos[0], pos[1]
            array[x][y][0] = 2


    def new_piece(self, array: list[list[int]], position: tuple[int, int], shape):
        '''
        Define a new piece to be spawned.\n
        Arguments
            array:
                game grid array from the 'gui' module
            position:
                (x, y) where the piece is gonna be spawned
            shape:
                any shape class from the 'piece' module
        '''
        self.current_shape = shape
        self.angle = 0
        self.current_piece = shape.rotation
        self.current_pos = position

        self.spawn_piece(array, self.current_piece[self.angle], self.current_pos, shape.color)



if __name__ == '__main__':




    ...