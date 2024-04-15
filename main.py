from gui import Display
from movement import Move
import piece


display = Display()
move = Move()

# add user input
display.root.bind('<Key>', lambda event: actions(event.keysym))


def actions(key: str):
    '''Executes action for corresponding key pressed.'''
    match key:
        # rotate piece
        case 'Up':
            print('up')
            ...
        # move piece one step downwards
        case 'Down':
            move.down(display.array)
            display.update_display()
            display.print_grid()
        # move piece one step to the right
        case 'Right':
            print('right')
            ...
        # move piece one step to the left    
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
    shape = piece.Tshape

    display.spawn_piece(shape.rot1, (5,5), shape.color)
    move.current_shape = shape
    move.current_piece = shape.rot1
    move.current_pos = (5,5)

    display.print_grid()
    display.update_display()




display.root.mainloop()