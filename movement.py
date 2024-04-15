


class Move:
    current_shape = None
    current_piece = None
    current_pos = None
    stored_piece = None


    def down(self, array: list[list[int]]):
        '''Move the current piece one step downwards.'''
        if self.bottom_is_empty(array):
            self.erase_old_position(array)
            x, y = self.current_pos[0], self.current_pos[1]
            self.current_pos = (x+1, y)
            self.spawn_piece(array, self.current_piece, self.current_pos, self.current_shape.color)


    def erase_old_position(self, array: list[list[int]]):
        '''
        Removes the current piece from the array.\n
        Used to clear the old position before assigning a new one
        '''
        for x in range(24):
            for y in range(10):
                if array[x][y][0] == 1:
                    array[x][y][0] = 0
                    array[x][y][1] = ''


    def get_positions(self, array: list[list[int]]) -> list[tuple[int, int]]:
        '''Returns the position of every square that make up the piece.'''
        positions = []
        for x in range(24):
            for y in range(10):
                if array[x][y][0] == 1:
                    positions.append((x,y))
        return positions
    

    def bottom_is_empty(self, array: list[list[int]]) -> bool:
        '''Checks for obstacles under the piece. Returns False if blocked, True otherwise.'''
        positions = self.get_positions(array)
        for pos in positions:
            x, y = pos[0], pos[1]
            if x+1 >= 24 or  array[x+1][y][0] == 2:
                return False
        return True


    def spawn_piece(self, array: list[list[int]], piece: list[list[int]], pos: tuple[int, int], color: str):
        '''
        Creates a new piece on the game grid at the specified position.\n
        Does not check wether the position is empty or not.
        '''
        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1]
        for i in range(height):
            for j in range(width):
                if x+i < 24 and array[x+i][y+j][0] == 0 and piece[i][j] == 1:
                    array[x+i][y+j][0] = 1
                    array[x+i][y+j][1] = color




if __name__ == '__main__':




    ...