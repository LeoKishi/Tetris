import tkinter as tk


class Display:
    def __init__(self):
        '''
        Initialize the game window.
        '''

        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.title('TETRIS')

        self.create_frames()
        self.create_labels()
        self.load_images()
        self.pack_widgets()



        
        # populating 'grid_frame' with small square frames in a grid
        self.square = [[None for width in range(10)] for height in range(22)]
        for x in range(22):
            for y in range(10):
                self.square[x][y] = tk.Frame(self.grid_frame,
                                             height=30,
                                             width=30,
                                             borderwidth=1,
                                             bg='#1a1a1a',
                                             relief=tk.FLAT)
                
                self.square[x][y].grid(row=x, column=y)

        # hide 2x10 space to spawn pieces above screen
        for x in range(2):
            for y in range(10):
                self.square[x][y].grid_forget()

        # 2D array to represent the game grid
        self.array = [[[0, ' '] for width in range(10)] for height in range(22)]

        # hex color value for each piece
        self.color = {'Z':'#d66363', # red
                      'L':'#d6a463', # orange
                      'O':'#d4d663', # yellow
                      'S':'#74d663', # green
                      'I':'#63d6cc', # cyan                     
                      'J':'#6389d6', # blue
                      'T':'#bb63d6'} # purple

    
    
    def print_grid(self):
        '''
        Prints the game grid. The hidden portion of the grid (where pieces spawn) is separated by a line.\n
        0 = empty space\n
        1 = current piece\n
        2 = static piece
        '''
        print()
        for i, j in enumerate(self.array):
            if i == 2:
                print()
            print(j)
        print()


    def update_display(self):
        '''Draws the game grid based on the values for each position in the array.'''
        for x in range(22):
            for y in range(10):
                if self.array[x][y][0] == 0:
                    self.square[x][y].config(bg='#1a1a1a',
                                             borderwidth=1,
                                             relief=tk.FLAT)
                else:
                    self.square[x][y].config(bg=self.color.get(self.array[x][y][1]),
                                             borderwidth=5,
                                             relief=tk.RAISED)


    def reset_game(self):
        '''Erases everything from the array and updates the display.'''
        self.array = [[0 for width in range(10)] for height in range(22)]
        self.update_display()
                    

    def create_frames(self):
        self.main_window = tk.Frame(self.root,
                                    bg='#2d2a30')
        
        # left ///////////////////
        self.left_side_frame = tk.Frame(self.main_window,
                                   bg='#2d2a30')

        self.hold_frame = tk.Frame(self.left_side_frame,
                                   height=100,
                                   width=100,
                                   borderwidth=5,
                                   relief=tk.SUNKEN,
                                   bg='#1a1a1a')
        

        # right //////////////////
        self.right_side_frame = tk.Frame(self.main_window,
                                   bg='#2d2a30')

        self.queue_frame = tk.Frame(self.right_side_frame,
                                   height=300,
                                   width=100,
                                   bg='#1a1a1a',
                                   borderwidth=5,
                                   relief=tk.SUNKEN)
        
        self.next_frame = tk.Frame(self.right_side_frame,
                                   height=100,
                                   width=100,
                                   borderwidth=5,
                                   relief=tk.SUNKEN,
                                   bg='#1a1a1a')


        # game grid //////////////
        self.grid_frame = tk.Frame(self.main_window,
                                   borderwidth=3,
                                   relief=tk.SUNKEN)


    def create_labels(self):
        self.hold_label = tk.Label(self.left_side_frame,
                                   text='HOLD',
                                   font=('Calibri', 20, 'bold'),
                                   fg='white',
                                   borderwidth=3,
                                   relief=tk.RIDGE,
                                   bg='#3f3845',
                                   pady=(5))
        
        self.lines_header_label = tk.Label(self.left_side_frame,
                                   text='LINES',
                                   font=('Calibri', 20, 'bold'),
                                   fg='white',
                                   borderwidth=3,
                                   relief=tk.RIDGE,
                                   bg='#3f3845',
                                   pady=(5))
        
        self.lines_value_label = tk.Label(self.left_side_frame,
                                   text='0',
                                   font=('Calibri', 20, 'bold'),
                                   fg='white',
                                   borderwidth=5,
                                   relief=tk.SUNKEN,
                                   bg='#1a1a1a',
                                   pady=(5))

        self.next_label = tk.Label(self.right_side_frame,
                                   text='NEXT',
                                   font=('Calibri', 20, 'bold'),
                                   fg='white',
                                   borderwidth=3,
                                   relief=tk.RIDGE,
                                   bg='#3f3845',
                                   pady=(5))


    def load_images(self):
        # load shape png files
        self.img_Ishape = tk.PhotoImage(file='assets/Ishape.png')
        self.img_Jshape = tk.PhotoImage(file='assets/Jshape.png')
        self.img_Lshape = tk.PhotoImage(file='assets/Lshape.png')
        self.img_Sshape = tk.PhotoImage(file='assets/Sshape.png')
        self.img_Zshape = tk.PhotoImage(file='assets/Zshape.png')
        self.img_Tshape = tk.PhotoImage(file='assets/Tshape.png')
        self.img_Oshape = tk.PhotoImage(file='assets/Oshape.png')

        # assign the corresponding file to the shape
        self.image = {'Z':self.img_Zshape,
                      'L':self.img_Lshape,
                      'O':self.img_Oshape,
                      'S':self.img_Sshape,
                      'I':self.img_Ishape,                 
                      'J':self.img_Jshape,
                      'T':self.img_Tshape} 

        # image labels
        self.hold_image = tk.Label(self.hold_frame,
                                   bg='#1a1a1a')

        self.next_image = tk.Label(self.next_frame,
                                   bg='#1a1a1a')

        self.queue1_image = tk.Label(self.queue_frame,
                                     bg='#1a1a1a')
        
        self.queue2_image = tk.Label(self.queue_frame,
                                     bg='#1a1a1a')
        
        self.queue3_image = tk.Label(self.queue_frame,
                                     bg='#1a1a1a')


    def pack_widgets(self):
        self.main_window.pack()

        # left side /////////////////////
        self.left_side_frame.pack(side=tk.LEFT, fill='y')

        # hold
        self.hold_label.pack(side=tk.TOP, padx=(20,0), pady=(20,0), anchor=tk.N, fill='x')
        self.hold_frame.pack(side=tk.TOP, padx=(20,0), pady=(10,0))
        self.hold_frame.pack_propagate(0)

        # line counter
        self.lines_header_label.pack(side=tk.TOP, padx=(20,0), pady=(100,0), fill='x')
        self.lines_value_label.pack(side=tk.TOP, padx=(20,0), pady=(10,0), fill='x')


        # right side ////////////////////
        self.right_side_frame.pack(side=tk.RIGHT, fill='y')

        # next piece
        self.next_label.pack(side=tk.TOP, padx=(0,20), pady=(20,0), anchor=tk.N, fill='x')
        self.next_frame.pack(side=tk.TOP, padx=(0,20), pady=(10,20))
        self.next_frame.pack_propagate(0)

        # queue
        self.queue_frame.pack(side=tk.TOP, padx=(0,20), pady=(0,20))
        self.queue_frame.pack_propagate(0)


        # game grid /////////////////////
        self.grid_frame.pack(side=tk.LEFT, padx=(20,20), pady=(20,20))


if __name__ == '__main__':
    display = Display()

    display.root.mainloop()