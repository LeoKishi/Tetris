import tkinter as tk
import numpy as np

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
                
        for x in range(4):
            for y in range(10):
                self.button[x][y].grid_forget()
        
    def print_array(self):
        print(self.array)

class Control:
    def spawn_piece(self, piece):
        for coord in piece:
            x, y = coord[0], coord[1]
            grid.array[x][y] = 1
            grid.button[x][y]['bg'] = 'red'

    def step(self):
        coords =  np.transpose(np.nonzero(grid.array == 1)) # piece position
        # erase piece
        for coord in coords:
            x, y = coord[0], coord[1]
            grid.array[x][y] = 0
            grid.button[x][y]['bg'] = 'SystemButtonFace'
        # redraw piece
        for coord in coords:
            x, y = coord[0], coord[1]
            grid.array[x+1][y] = 1
            grid.button[x+1][y]['bg'] = 'red'


class Piece:
     square = [[0,4],[0,5],[1,4],[1,5]]




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
grid.print_array()
control.spawn_piece(Piece.square)



# event binding
root.bind('<Button-1>', lambda event:control.step())






root.mainloop()