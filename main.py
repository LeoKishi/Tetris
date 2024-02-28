import tkinter as tk

root = tk.Tk()
root.resizable(0,0)
root.title('Tetris')






main_window = tk.Frame(root, height=600, width=400)

main_window.pack()

root.mainloop()