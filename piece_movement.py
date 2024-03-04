import numpy as np
import tkinter as tk

class Move:
    # redraw piece
    def redraw(self, grid, coords, mod_x=0, mod_y=0, erase_only=False, draw_only=False):
        # erase
        if not draw_only:
            for pos in coords:
                x, y = pos[0], pos[1]
                grid.array[x][y] = 0
                grid.button[x][y]['bg'] = '#1a1a1a'
                grid.button[x][y]['relief'] = tk.RIDGE
                grid.button[x][y]['borderwidth'] = 1
        if erase_only:
            return
        # draw
        for pos in coords:
            x, y = pos[0], pos[1]
            grid.array[x+(mod_x)][y+(mod_y)] = 1
            grid.button[x+(mod_x)][y+(mod_y)]['bg'] = 'red'
            grid.button[x+(mod_x)][y+(mod_y)]['relief'] = tk.RAISED
            grid.button[x+(mod_x)][y+(mod_y)]['borderwidth'] = 6

        # top-left position of current piece bounding square
        piece.current_pos[0] += mod_x
        piece.current_pos[1] += mod_y

    # move piece 1 square
    def step(self, grid, direction ,mod_x=0, mod_y=0):
        coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
        # down step
        if direction == 'Down':
            self.redraw(grid, coords, mod_x=mod_x)
            for x,y in coords:
                # if piece is next to floor
                if x == 22:
                    for pos in coords:
                        x, y = pos[0], pos[1]
                        grid.array[x+(mod_x)][y] = 2 # turn falling piece into static piece
                    self.replace(grid, [5,4], piece.t_shape_0) # SPAWN NEXT SHAPE
        # side step
        elif direction == 'Lateral':
            for x,y in coords:
                # if piece is next to border and the next move is against border: do nothing
                if ((y == 9) and (mod_y == 1)) or ((y == 0) and (mod_y == -1)):
                    return
            self.redraw(grid, coords, mod_y=mod_y)

    orientation = 1 #  0,1,2,3  =  0°,90°,180°,270°

    # select piece orientation and place in grid
    def rotate(self, grid, current_piece):
        coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
        self.redraw(grid, coords, erase_only=True) # erase piece
        shape = current_piece[self.orientation] # select piece orientation
        self.replace(grid, piece.current_pos, shape) # place piece in grid
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1

    # place piece in grid
    def replace(self, grid, pos, shape):
        piece.current_pos = pos
        x, y = pos[0], pos[1]
        coords = []
        for row in range(3):
            for col in range(3):
                if shape[row][col] == grid.array[x+row][y+col] == 2:
                    return
                else:
                    coords.append((x+row, y+col)) if shape[row][col] == 1 else None
        self.redraw(grid, coords, draw_only=True)

class Piece:
    current_pos = []

    s_shape_0 = [[0,1,1],
               [1,1,0],
               [0,0,0]]

    s_shape_90 = [[0,1,0],
                  [0,1,1],
                  [0,0,1]]

    s_shape_180 = [[0,1,1],
                   [1,1,0],
                   [0,0,0]]
    
    s_shape_270 = [[0,1,0],
                   [0,1,1],
                   [0,0,1]]

    s_rotation = [s_shape_0, s_shape_90, s_shape_180, s_shape_270]
    
    t_shape_0 = [[0,0,0],
               [1,1,1],
               [0,1,0]]

    t_shape_90 = [[0,1,0],
                  [1,1,0],
                  [0,1,0]]

    t_shape_180 = [[0,1,0],
                   [1,1,1],
                   [0,0,0]]
    
    t_shape_270 = [[0,1,0],
                   [0,1,1],
                   [0,1,0]]
    
    t_rotation = [t_shape_0, t_shape_90, t_shape_180, t_shape_270]


move = Move()
piece = Piece()