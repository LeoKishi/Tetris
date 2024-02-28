import tkinter as tk

root = tk.Tk()
root.resizable(0,0)
root.title('TETRIS')

class Button:
    def __init__(self):
        self.button = [[0 for width in range(10)] for height in range(20)]
        self.array = [[0 for width in range(10)] for height in range(20)]
        for x in range(20):
            for y in range(10):
                self.button[x][y] = tk.Frame(grid_frame, height=30, width=30, borderwidth=1, relief=tk.RIDGE)
                self.button[x][y].grid(row=x, column=y)





main_window = tk.Frame(root, height=600, width=400, bg='pink')
grid_frame = tk.Frame(main_window, borderwidth=3, relief=tk.SUNKEN)
side_frame = tk.Frame(main_window, height=600, width=200)

main_window.pack()
grid_frame.pack(side=tk.LEFT, padx=(20,20), pady=(20,20))
side_frame.pack(side=tk.RIGHT, padx=(0,20))

button = Button()

root.mainloop()