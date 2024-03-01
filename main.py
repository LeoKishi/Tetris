import tkinter as tk
import numpy as np
import piece_movement, tetrimino


root = tk.Tk()
root.resizable(0,0)
root.title('TETRIS')

class Grid:
    def __init__(self):
        self.button = [[0 for width in range(10)] for height in range(24)]
        self.array = np.zeros((24,10),dtype=np.int8)
        for x in range(24):
            for y in range(10):
                self.button[x][y] = tk.Frame(grid_frame,height=30, width=30, borderwidth=1, relief=tk.RIDGE)
                self.button[x][y].grid(row=x, column=y)
        # 4x10 space to spawn pieces above screen
        for x in range(4):
            for y in range(10):
                self.button[x][y].grid_forget()
        
    def print_array(self):
        print(self.array)

class Control:
    def __init__(self):
        root.bind('<Key>', lambda event: self.move(event.keysym, None))

    holding = None

    def spawn_piece(self, piece):
        self.holding = piece
        for coord in piece:
            x, y = coord[0], coord[1]
            grid.array[x][y] = 1
            grid.button[x][y]['bg'] = 'red'

    def move(self, key, current_piece):
        match key:
            case 'Down':
                piece_movement.down(grid) # moves piece 1 step downwards
            case 'Up':
                piece_movement.rotate(grid, current_piece)
            case 'Right':
                piece_movement.lateral(grid, mod_y=1) # moves piece 1 step to the right
            case 'Left':
                piece_movement.lateral(grid, mod_y=-1) # moves piece 1 step to the left

class Piece:  
    t_shape = [[0,5],[0,4],[0,6],[1,5]]
    j_shape = [[0,5],[1,5],[2,5],[2,4]]
    l_shape = [[0,4],[1,4],[2,4],[2,5]]
    i_shape = [[0,3],[0,4],[0,5],[0,6]]
    o_shape = [[0,4],[0,5],[1,4],[1,5]]
    s_shape = [[0,5],[0,6],[1,5],[1,4]]
    z_shape = [[0,4],[0,5],[1,5],[1,6]]





# frame creation
main_window = tk.Frame(root, height=600, width=400, bg='pink')
grid_frame = tk.Frame(main_window, borderwidth=3, relief=tk.SUNKEN)
side_frame = tk.Frame(main_window, height=600, width=200)

# frame packing
main_window.pack()
grid_frame.pack(side=tk.LEFT, padx=(20,20), pady=(20,20))
side_frame.pack(side=tk.RIGHT, padx=(0,20))

# class instantiation
grid = Grid()
control = Control()



# misc
control.spawn_piece(Piece.t_shape)
grid.print_array()








root.mainloop()