import numpy as np
import tkinter as tk

def down(grid):
    coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
    # erase piece
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x][y] = 0
        grid.button[x][y]['bg'] = 'SystemButtonFace'
        grid.button[x][y]['relief'] = tk.RIDGE
        grid.button[x][y]['borderwidth'] = 1
    # redraw piece
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x+1][y] = 1
        grid.button[x+1][y]['bg'] = 'red'
        grid.button[x+1][y]['relief'] = tk.RAISED
        grid.button[x+1][y]['borderwidth'] = 6
    for x,y in coords:
        # if piece is next to floor
        if x == 22:
            for pos in coords:
                x, y = pos[0], pos[1]
                grid.array[x+1][y] = 2 # turn falling piece into static piece
    #grid.print_array()
                
def lateral(grid, mod_x=0, mod_y=0):
    coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
    for x,y in coords:
        # if piece is next to border and the next move is against border: do nothing
        if ((y == 9) and (mod_y == 1)) or ((y == 0) and (mod_y == -1)):
            return
    # erase piece
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x][y] = 0
        grid.button[x][y]['bg'] = 'SystemButtonFace'
        grid.button[x][y]['relief'] = tk.RIDGE
        grid.button[x][y]['borderwidth'] = 1
    # redraw piece in new position
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x+(mod_x)][y+(mod_y)] = 1
        grid.button[x+(mod_x)][y+(mod_y)]['bg'] = 'red'
        grid.button[x+(mod_x)][y+(mod_y)]['relief'] = tk.RAISED
        grid.button[x+(mod_x)][y+(mod_y)]['borderwidth'] = 6

def rotate(grid, current_piece):
    coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
