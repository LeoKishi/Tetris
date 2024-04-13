import tkinter as tk
import piece


class Display:
    def __init__(self):
        '''
        Initialize the game window.

        Methods
        -------
        print_grid()
            Prints the game grid into the console.

        update_display()
            Draws the game grid on the display.

        reset_game()
            Erases everything from the array and updates the display.

        spawn_piece(piece, pos):
            Creates a new piece on the game grid at the specified position.
        '''

        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.title('TETRIS')

        # frame creation
        self.main_window = tk.Frame(self.root,
                                    height=600,
                                    width=400,
                                    bg='#2d2a30')
        
        self.grid_frame = tk.Frame(self.main_window,
                                   borderwidth=3,
                                   relief=tk.SUNKEN)
        
        self.side_frame = tk.Frame(self.main_window,
                                   height=600,
                                   width=200,
                                   bg='#1a1a1a')

        # frame packing
        self.main_window.pack()
        self.grid_frame.pack(side=tk.LEFT, padx=(20,20), pady=(20,20))
        self.side_frame.pack(side=tk.RIGHT, padx=(0,20))

        # populating 'grid_frame' with small square frames in a grid
        self.square = [[None for width in range(10)] for height in range(24)]
        for x in range(24):
            for y in range(10):
                self.square[x][y] = tk.Frame(self.grid_frame,
                                             height=30,
                                             width=30,
                                             borderwidth=1,
                                             bg='#1a1a1a',
                                             relief=tk.RIDGE)
                
                self.square[x][y].grid(row=x, column=y)

        # hide 4x10 space to spawn pieces above screen
        for x in range(4):
            for y in range(10):
                self.square[x][y].grid_forget()

        # 2D array to represent the game grid
        self.array = [[0 for width in range(10)] for height in range(24)]
    
    def print_grid(self):
        '''
        Prints the game grid. The hidden portion of the grid (where pieces spawn) is separated by a line.\n
        0 = empty space\n
        1 = moving piece\n
        2 = static piece
        '''

        print()
        for i, j in enumerate(self.array):
            if i == 4:
                print()
            print(j)
        print()

    def update_display(self):
        '''Draws the game grid based on the values for each position in the array.'''
        for x in range(24):
            for y in range(10):
                if self.array[x][y] == 0:
                    self.square[x][y]['bg'] = '#1a1a1a'
                else:
                    self.square[x][y]['bg'] = 'white'

    def reset_game(self):
        '''Erases everything from the array and updates the display.'''
        self.array = [[0 for width in range(10)] for height in range(24)]
        self.update_display()

    def spawn_piece(self, piece: list[int], pos: tuple[int, int]):
        '''
        Creates a new piece on the game grid at the specified position.\n
        Does not check wether the position is empty or not.

        Parameters:
            piece:
                2D list with the position of each square that forms the piece
            pos:
                (x, y) position where the piece is going to be spawned
        '''

        width, height = len(piece[0]), len(piece)
        x, y = pos[0], pos[1]
        for i in range(width):
            for j in range(height):
                if self.array[x+i][y+j] == 0 and piece[i][j] == 1:
                    self.array[x+i][y+j] = 1
                



if __name__ == '__main__':
    display = Display()

    display.spawn_piece(piece.Tshape.rot1, (20,5))
    display.print_grid()
    display.update_display()

    display.root.mainloop()