import numpy as np
import tkinter as tk
import random
from copy import deepcopy

class Move:
    def __init__(self, grid, root):
        self.grid = grid
        self.root = root

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

    def step(self, direction ,mod_x=0, mod_y=0):
        coords =  np.transpose(np.nonzero(self.grid.array == 1)) # falling piece position
        # down step
        if (direction == 'Down') and (self.bottom_collision == False):
            self.erase(coords)
            self.draw(coords, mod_x=mod_x)
        # side step
        elif ((direction == 'Right') and (self.right_collision == False)) or ((direction == 'Left') and (self.left_collision == False)):
            for x,y in coords:
                # if piece is next to border and the next move is against border: do nothing
                if ((y == 9) and (mod_y == 1)) or ((y == 0) and (mod_y == -1)):
                    return
            self.erase(coords)
            self.draw(coords, mod_y=mod_y)

        self.check_side_collision('right')
        self.check_side_collision('left')
        self.check_bottom_collision()

    orientation = 1 #  0,1,2,3  =  0°,90°,180°,270°

    # select piece orientation and place in grid
    def rotate(self):
        coords = np.transpose(np.nonzero(self.grid.array == 1)) # falling piece position
        self.erase(coords)
        piece.holding = piece.hold_rotation[self.orientation] # select piece orientation 
        if self.orientation == 3:
            self.orientation = 0
        else:
            self.orientation += 1
        if self.rotation_is_valid() == True:
            self.replace(piece.current_pos, piece.holding)
            return
        else: self.try_insert(self.out_of_bounds())


    def try_insert(self, direction):
        print('Try insert')
        x, y = piece.current_pos[0],piece.current_pos[1]
        if direction == 'left':
            if piece.current_pos[1] == -2:
                self.replace([x,y+2], piece.holding)
            elif piece.current_pos[1] == -1:
                self.replace([x,y+1], piece.holding)
        elif direction == 'right':
            if (piece.current_pos[1] == 8):
                reach = 2 if piece.holding == ishape.shape_0 else 1
                self.replace([x,y-reach], piece.holding)
            elif piece.current_pos[1] == 7:
                self.replace([x,y-1], piece.holding) 

    # place piece in grid
    def rotation_is_valid(self) -> bool | str:
        if self.blocked():
            return 
        side = self.out_of_bounds()
        if side == None:
            return True

    def out_of_bounds(self):
        x, y = piece.current_pos[0], piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                try: 
                    if piece.holding[row][col] == 1:
                        self.grid.array[x+row][y+col]
                except IndexError:
                    return 'right'
                else:
                    if (piece.holding[row][col] == 1) and (y+col == -1):
                        return 'left'
        return None
                    
    def blocked(self) -> bool :
        x, y = piece.current_pos[0], piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                try:
                    if (piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        print('Blocked by piece')
                        return True
                except: pass

    def replace(self, pos, shape):
        piece.current_pos = pos
        piece.holding = shape
        x, y = pos[0], pos[1]
        coords = []
        for row in range(4):
            for col in range(4):
                if y+col >= 0:
                    try:
                        if shape[row][col] == self.grid.array[x+row][y+col] == 2:
                            return
                        else:
                            coords.append((x+row, y+col)) if shape[row][col] == 1 else None
                    except: None
        self.draw(coords)


    bottom_collision = False

    # arrumar bug do quadrado -> quadrado encostando a parte de baixo + rotação + mexer pro lado = não muda pra peça estática

    def check_bottom_collision(self):
        collision = False
        x, y = piece.current_pos[0]+1, piece.current_pos[1]
        for row in range(4):
            for col in range(4):
                # checks for collision with another piece
                try:
                    if (piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
                        collision = True
                        self.bottom_collision = True
                        self.lock_delay()
                # collision with floor (index out of bounds)
                except:
                    collision = True
                    self.bottom_collision = True
                    self.lock_delay()
        if collision == False:
            self.bottom_collision = False
            self.stop_lock_delay()

    right_collision = False
    left_collision = False

    def check_side_collision(self, side):
        collision = False
        x, y = piece.current_pos[0], piece.current_pos[1]
        if side == 'right':
            y += 1
        else:
            y-= 1
        for row in range(4):
            for col in range(4):
                # checks for collision with another piece
                try:
                    if (piece.holding[row][col] == 1) and (self.grid.array[x+row][y+col] == 2):
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

    def freeze(self):
        coords =  np.transpose(np.nonzero(self.grid.array == 1))
        for pos in coords:
            x, y = pos[0], pos[1]
            self.grid.array[x][y] = 2
        self.bottom_collision = self.left_collision = self.right_collision_collision = False
        self.stop_list = []
        self.spawn_next()
        
    def spawn_next(self):
        random_shape = piece.get_random_shape()
        pos = [5,4]
        self.orientation = 1
        piece.current_pos = pos
        piece.hold_rotation = random_shape.rotation
        piece.holding = piece.hold_rotation[0]
        self.replace(pos, random_shape.shape_0)

    stop_list = []

    def lock_delay(self):
        if len(self.stop_list) == 0:
            self.stop_list.append(self.root.after(1000, self.freeze))

    def stop_lock_delay(self):
        if len(self.stop_list) > 0:
            for item in self.stop_list:
                self.root.after_cancel(item)
                self.stop_list.remove(item)


class Piece:
    def __init__(self, *args):
        self.shape_pool = [*args]
        self.temp_shape_pool = deepcopy(self.shape_pool)

    current_pos = []
    holding = None
    hold_rotation = None

    def get_random_shape(self):
        if len(self.temp_shape_pool) == 0:
            self.temp_shape_pool = deepcopy(self.shape_pool)
        random_shape = random.choice(self.temp_shape_pool)
        self.temp_shape_pool.remove(random_shape)
        return random_shape

class SShape:
    shape_0 = [[0,1,1,0],
               [1,1,0,0],
               [0,0,0,0],
               [0,0,0,0]]

    shape_90 = [[0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,0,0]]

    shape_180 = [[0,0,0,0],
                 [0,1,1,0],
                 [1,1,0,0],
                 [0,0,0,0]]
    
    shape_270 = [[1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,0,0,0]]

    rotation = [shape_0, shape_90, shape_180, shape_270]

class ZShape:
    shape_0 = [[1,1,0,0],
               [0,1,1,0],
               [0,0,0,0],
               [0,0,0,0]]

    shape_90 = [[0,0,1,0],
                [0,1,1,0],
                [0,1,0,0],
                [0,0,0,0]]

    shape_180 = [[0,0,0,0],
                 [1,1,0,0],
                 [0,1,1,0],
                 [0,0,0,0]]
    
    shape_270 = [[0,1,0,0],
                 [1,1,0,0],
                 [1,0,0,0],
                 [0,0,0,0]]

    rotation = [shape_0, shape_90, shape_180, shape_270]

class LShape:
    shape_0 = [[0,0,1,0],
                 [1,1,1,0],
                 [0,0,0,0],
                 [0,0,0,0]]

    shape_90 = [[0,1,0,0],
                  [0,1,0,0],
                  [0,1,1,0],
                  [0,0,0,0]]

    shape_180 = [[0,0,0,0],
                   [1,1,1,0],
                   [1,0,0,0],
                   [0,0,0,0]]
    
    shape_270 = [[1,1,0,0],
                   [0,1,0,0],
                   [0,1,0,0],
                   [0,0,0,0]]

    rotation = [shape_0, shape_90, shape_180, shape_270]

class JShape:
    shape_0 = [[1,0,0,0],
                 [1,1,1,0],
                 [0,0,0,0],
                 [0,0,0,0]]

    shape_90 = [[0,1,1,0],
                  [0,1,0,0],
                  [0,1,0,0],
                  [0,0,0,0]]

    shape_180 = [[0,0,0,0],
                   [1,1,1,0],
                   [0,0,1,0],
                   [0,0,0,0]]
    
    shape_270 = [[0,1,0,0],
                   [0,1,0,0],
                   [1,1,0,0],
                   [0,0,0,0]]

    rotation = [shape_0, shape_90, shape_180, shape_270]

class TShape:
    shape_0 = [[0,0,0,0],
                 [1,1,1,0],
                 [0,1,0,0],
                 [0,0,0,0]]

    shape_90 = [[0,1,0,0],
                  [1,1,0,0],
                  [0,1,0,0],
                  [0,0,0,0]]

    shape_180 = [[0,1,0,0],
                   [1,1,1,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    
    shape_270 = [[0,1,0,0],
                   [0,1,1,0],
                   [0,1,0,0],
                   [0,0,0,0]]
    
    rotation = [shape_0, shape_90, shape_180, shape_270]

class IShape:
    shape_0 = [[0,0,0,0],
                 [1,1,1,1],
                 [0,0,0,0],
                 [0,0,0,0]]

    shape_90 = [[0,0,1,0],
                  [0,0,1,0],
                  [0,0,1,0],
                  [0,0,1,0]]

    shape_180 = [[0,0,0,0],
                   [0,0,0,0],
                   [1,1,1,1],
                   [0,0,0,0]]
    
    shape_270 = [[0,1,0,0],
                   [0,1,0,0],
                   [0,1,0,0],
                   [0,1,0,0]]
    
    rotation = [shape_0, shape_90, shape_180, shape_270]

class OShape:
    shape_0 = [[1,1,0,0],
                 [1,1,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]

    shape_90 = [[1,1,0,0],
                  [1,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]

    shape_180 = [[1,1,0,0],
                   [1,1,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    
    shape_270 = [[1,1,0,0],
                   [1,1,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    
    rotation = [shape_0, shape_90, shape_180, shape_270]

sshape = SShape()
zshape = ZShape()
lshape = LShape()
jshape = JShape()
tshape = TShape()
oshape = OShape()
ishape = IShape()

piece = Piece(sshape, zshape, lshape, jshape, tshape, oshape, ishape)
