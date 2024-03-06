class Collision:
    def __init__(self, grid, piece):
        self.grid = grid
        self.piece = piece

    bottom_collision = False

    def check_bottom_collision(self):
        collision = False
        x, y = self.piece.current_pos[0]+1, self.piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                # checks for collision with another piece
                try:
                    if (self.piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        collision = True
                        self.bottom_collision = True
                        return True
                # collision with floor (index out of bounds)
                except:
                    collision = True
                    self.bottom_collision = True
                    return True
        if collision == False:
            self.bottom_collision = False
            return False

    right_collision = False
    left_collision = False

    def check_side_collision(self, side):
        collision = False
        x, y = self.piece.current_pos[0], self.piece.current_pos[1]
        if side == 'right':
            y += 1
        else:
            y-= 1
        for row in range(4):
            for col in range(4):
                # checks for collision with another piece
                try:
                    if (self.piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        collision = True
                        if side == 'right':
                            self.right_collision = True
                        else:
                            self.left_collision = True
                except: None
        if collision == False:
            if side == 'right':
                self.right_collision = False
            else:
                self.left_collision = False

    def out_of_bounds(self):
        x, y = self.piece.current_pos[0], self.piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                try: 
                    if self.piece.holding[row][col] == 1:
                        self.grid.array[x+row][y+col]
                except IndexError:
                    return 'right'
                else:
                    if (self.piece.holding[row][col] == 1) and (y+col == -1):
                        return 'left'
        return False

    def blocked(self):
        x, y = self.piece.current_pos[0], self.piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                try:
                    if (self.piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        return col
                except: 
                    return False
                
    def not_occupied(self, col): 
        x, y = self.piece.current_pos[0], self.piece.current_pos[1]
        if col <= 1:
            direction = -1
        elif col >= 2:
            direction = 1
        for row in range(4):
            for col in range(4):
                try: 
                    if (self.piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col+direction] == 2):
                        return None
                except:
                    return None
                else:
                    return False if direction == 1 else True
                
    def rotation_is_valid(self):
        if self.out_of_bounds() is None:
            return True
