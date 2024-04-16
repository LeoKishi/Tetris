from gui import Display
from movement import Move
import piece


<<<<<<< Updated upstream
=======
class Clock:
    # variables to store tkinter 'after' function execution id
    timer_stop_id = None
    game_tick_stop_id = None

    def start_timer(self):
        '''Starts the timer'''
        self.timer_stop_id = display.root.after(2000, freeze)

    def stop_timer(self):
        '''Stop the timer if the timer is currently running.'''
        if self.timer_stop_id is not None:
            display.root.after_cancel(self.timer_stop_id)
            self.timer_stop_id = None

    def start_game_tick(self):
        if self.game_tick_stop_id is not None:
            actions('Down')
        self.game_tick_stop_id = display.root.after(500, self.start_game_tick)

    def stop_game_tick(self):
        if self.game_tick_stop_id is not None:
            display.root.after_cancel(self.game_tick_stop_id)
            self.game_tick_stop_id = None


>>>>>>> Stashed changes
display = Display()
move = Move()

# add user input
display.root.bind('<Key>', lambda event: actions(event.keysym))


def actions(key: str):
    '''Executes action for corresponding key pressed.'''
    match key:
        # rotate piece
        case 'Up':
<<<<<<< Updated upstream
            print('up')
            ...
=======
            move.rotate(display.array)
            display.update_display()

>>>>>>> Stashed changes
        # move piece one step downwards
        case 'Down':
            move.down(display.array)
            display.update_display()
<<<<<<< Updated upstream
            display.print_grid()
=======

>>>>>>> Stashed changes
        # move piece one step to the right
        case 'Right':
            move.right(display.array)
            display.update_display()
<<<<<<< Updated upstream
            display.print_grid()
=======

>>>>>>> Stashed changes
        # move piece one step to the left    
        case 'Left':
            move.left(display.array)
            display.update_display()
<<<<<<< Updated upstream
            display.print_grid()
        # drop piece
        case 'space':
            print('space')
            ...
=======

        # drop piece
        case 'space':
            move.drop(display.array)
            freeze()
            display.update_display()

>>>>>>> Stashed changes
        # hold piece
        case 'c':
            print('c')
            ...
<<<<<<< Updated upstream


=======
    
    display.print_grid()
    
    # check if the piece is on the floor or on top of another piece
    if not collision.bottom_is_empty(display.array):
        if clock.timer_stop_id is None:
            clock.start_timer()
    else:
        clock.stop_timer()


def freeze():
    '''Freezes the piece and spawn a new one. Resets the game tick.'''
    move.freeze_piece(display.array)
    clock.stop_game_tick()

    move.new_piece(display.array, (5,5), piece.Tshape)
    display.update_display()
    clock.start_game_tick()

>>>>>>> Stashed changes


if __name__ == '__main__':
    #display.array[10][3][0] = 2


    shape = piece.Sshape

    display.spawn_piece(shape.rot1, (5,5), shape.color)
    move.current_shape = shape
    move.current_piece = shape.rot1
    move.current_pos = (5,5)

    display.print_grid()
    display.update_display()




display.root.mainloop()