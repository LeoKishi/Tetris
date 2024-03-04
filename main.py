import tkinter as tk
import numpy as np
import pmov


root = tk.Tk()
root.resizable(0,0)
root.title('TETRIS')

class Grid:
    def __init__(self):
        self.button = [[0 for width in range(10)] for height in range(24)]
        self.array = np.zeros((24,10),dtype=np.int8)
        for x in range(24):
            for y in range(10):
                self.button[x][y] = tk.Frame(grid_frame,height=30, width=30, borderwidth=1,bg='#1a1a1a' ,relief=tk.RIDGE)
                self.button[x][y].grid(row=x, column=y)
        # 4x10 space to spawn pieces above screen
        for x in range(4):
            for y in range(10):
                self.button[x][y].grid_forget()
        
    def print_array(self):
        print(self.array)



class Control:
    def __init__(self):
        root.bind('<Key>', lambda event: self.move(event.keysym))

    def move(self, key):
        match key:
            case 'Up':
                move.rotate()
            case 'Down':
                move.step('Down' , mod_x=1) # moves piece 1 step downwards
            case 'Right':
                move.step('Lateral', mod_y=1) # moves piece 1 step to the right
            case 'Left':
                move.step('Lateral', mod_y=-1) # moves piece 1 step to the left
        #grid.print_array()



# frame creation
main_window = tk.Frame(root, height=600, width=400, bg='#2d2a30')
grid_frame = tk.Frame(main_window, borderwidth=3, relief=tk.SUNKEN)
side_frame = tk.Frame(main_window, height=600, width=200, bg='#1a1a1a')

# frame packing
main_window.pack()
grid_frame.pack(side=tk.LEFT, padx=(20,20), pady=(20,20))
side_frame.pack(side=tk.RIGHT, padx=(0,20))

# class instantiation
grid = Grid()
control = Control()

move = pmov.Move(grid)

# misc
move.spawn_next()







root.mainloop()