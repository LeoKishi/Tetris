import numpy as np
import tkinter as tk

# redraw piece
def redraw(grid, coords, mod_x=0, mod_y=0):
    # erase
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x][y] = 0
        grid.button[x][y]['bg'] = '#1a1a1a'
        grid.button[x][y]['relief'] = tk.FLAT
        grid.button[x][y]['borderwidth'] = 1
    # draw
    for pos in coords:
        x, y = pos[0], pos[1]
        grid.array[x+(mod_x)][y+(mod_y)] = 1
        grid.button[x+(mod_x)][y+(mod_y)]['bg'] = 'red'
        grid.button[x+(mod_x)][y+(mod_y)]['relief'] = tk.RAISED
        grid.button[x+(mod_x)][y+(mod_y)]['borderwidth'] = 6

def step(grid,direction ,mod_x=0, mod_y=0):
    coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
    # down step
    if direction == 'Down':
        redraw(grid, coords, mod_x=mod_x)
        for x,y in coords:
            # if piece is next to floor
            if x == 22:
                for pos in coords:
                    x, y = pos[0], pos[1]
                    grid.array[x+(mod_x)][y] = 2 # turn falling piece into static piece
    # side step
    elif direction == 'Lateral':
        for x,y in coords:
            # if piece is next to border and the next move is against border: do nothing
            if ((y == 9) and (mod_y == 1)) or ((y == 0) and (mod_y == -1)):
                return
        redraw(grid, coords, mod_y=mod_y)

def rotate(grid, current_piece):
    coords =  np.transpose(np.nonzero(grid.array == 1)) # falling piece position
