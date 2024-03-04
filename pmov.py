import numpy as np
import tkinter as tk

class Move:
    def __init__(self, grid):
        self.grid = grid

    def erase(self, coords):
        for pos in coords:
            x, y = pos[0], pos[1]
            self.grid.array[x][y] = 0
            self.grid.button[x][y]['bg'] = '#1a1a1a'
            self.grid.button[x][y]['relief'] = tk.RIDGE
            self.grid.button[x][y]['borderwidth'] = 1

    def draw(self, coords, mod_x=0, mod_y=0):
        for pos in coords:
            x, y = pos[0], pos[1]
            self.grid.array[x+(mod_x)][y+(mod_y)] = 1
            self.grid.button[x+(mod_x)][y+(mod_y)]['bg'] = 'red'
            self.grid.button[x+(mod_x)][y+(mod_y)]['relief'] = tk.RAISED
            self.grid.button[x+(mod_x)][y+(mod_y)]['borderwidth'] = 6
        piece.current_pos[0] += mod_x
        piece.current_pos[1] += mod_y


    # move piece 1 square
    def step(self, direction ,mod_x=0, mod_y=0):
        coords =  np.transpose(np.nonzero(self.grid.array == 1)) # falling piece position
        # down step
        if direction == 'Down':
            self.erase(coords)
            self.draw(coords, mod_x=mod_x)
            self.check_collision() # turn falling piece into static piece
        # side step
        elif direction == 'Lateral':
            for x,y in coords:
                # if piece is next to border and the next move is against border: do nothing
                if ((y == 9) and (mod_y == 1)) or ((y == 0) and (mod_y == -1)):
                    return
            self.erase(coords)
            self.draw(coords, mod_y=mod_y)

        self.check_collision()

    orientation = 1 #  0,1,2,3  =  0°,90°,180°,270°

    # select piece orientation and place in grid
    def rotate(self):
        coords =  np.transpose(np.nonzero(self.grid.array == 1)) # falling piece position
        self.erase(coords)
        piece.holding = piece.hold_rotation[self.orientation] # select piece orientation
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1
        self.replace(piece.current_pos, piece.holding) # place piece in grid

    # place piece in grid
    def replace(self, pos, shape):
        piece.current_pos = pos
        piece.holding = shape
        x, y = pos[0], pos[1]
        coords = []
        for row in range(3):
            for col in range(3):
                if shape[row][col] == self.grid.array[x+row][y+col] == 2:
                    return
                else:
                    coords.append((x+row, y+col)) if shape[row][col] == 1 else None
        self.draw(coords)

    def check_collision(self):
        x, y = piece.current_pos[0]+1, piece.current_pos[1]
        for row in range(3):
            for col in range(3):
                # checks for collision with another piece
                try:
                    if (piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        self.freeze()
                        self.spawn_next()
                # collision with floor (index out of bounds)
                except:
                    self.freeze()
                    self.spawn_next()

    def freeze(self):
        coords =  np.transpose(np.nonzero(self.grid.array == 1))
        for pos in coords:
            x, y = pos[0], pos[1]
            self.grid.array[x][y] = 2
        
    def spawn_next(self):
        pos = [0,4]
        self.replace(pos, TShape.t_shape_0) # SPAWN NEXT SHAPE
        self.orientation = 1
        piece.current_pos = pos
        piece.hold_rotation = TShape.t_rotation
        piece.holding = piece.hold_rotation[0]

class Piece:
    current_pos = []
    holding = None
    hold_rotation = None

class SShape:
    s_shape_0 = [[0,1,1],
               [1,1,0],
               [0,0,0]]

    s_shape_90 = [[0,1,0],
                  [0,1,1],
                  [0,0,1]]

    s_shape_180 = [[0,0,0],
                   [0,1,1],
                   [1,1,0]]
    
    s_shape_270 = [[0,1,0],
                   [0,1,1],
                   [0,0,1]]

    s_rotation = [s_shape_0, s_shape_90, s_shape_180, s_shape_270]

class TShape:
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

piece = Piece()
