from gui import Display
import piece


display = Display()

# user input
display.root.bind('<Key>', lambda event: actions(event.keysym))


def actions(key):
    '''Execute action for correspondent key pressed.'''
    match key:
        # rotate piece
        case 'Up':
            print('up')
            ...
        # move piece 1 step downwards
        case 'Down':
            print('down')
            ...
        # move piece 1 step to the right
        case 'Right':
            print('right')
            ...
        # move piece 1 step to the left    
        case 'Left':
            print('left')
            ...
        # drop piece
        case 'space':
            print('space')
            ...
        # hold piece
        case 'c':
            print('c')
            ...




if __name__ == '__main__':
    display.spawn_piece(piece.Tshape.rot1, (20,5))
    display.print_grid()
    display.update_display()




display.root.mainloop()