from gui import Display
from movement import Move
from collision import Collision
import piece


class Clock:
    # variables to store tkinter 'after' function execution id
    timer_stop_id = None
    game_tick_stop_id = None

    def start_timer(self):
        '''Starts the timer'''
        self.timer_stop_id = display.root.after(2000, freeze)

    def stop_timer(self):
        '''Stops the timer if the timer is currently running.'''
        if self.timer_stop_id is not None:
            display.root.after_cancel(self.timer_stop_id)
            self.timer_stop_id = None

    def start_game_tick(self):
        '''Starts the game tick. Makes the piece move one step downwards for each tick.'''
        if self.game_tick_stop_id is not None:
            actions('Down')
        self.game_tick_stop_id = display.root.after(500, self.start_game_tick)

    def stop_game_tick(self):
        '''Stops the game tick clock if the clock is currently running.'''
        if self.game_tick_stop_id is not None:
            display.root.after_cancel(self.game_tick_stop_id)
            self.game_tick_stop_id = None


display = Display()
move = Move()
collision = Collision()
clock = Clock()

# bind user input
display.root.bind('<Key>', lambda event: actions(event.keysym))


def actions(key: str):
    '''Executes action for corresponding key pressed.'''
    match key:
        # rotate piece
        case 'Up':
            move.rotate(display.array)
            display.update_display()

        # move piece one step downwards
        case 'Down':
            move.down(display.array)
            display.update_display()

        # move piece one step to the right
        case 'Right':
            move.right(display.array)
            display.update_display()

        # move piece one step to the left    
        case 'Left':
            move.left(display.array)
            display.update_display()

        # drop piece
        case 'space':
            move.drop(display.array)
            freeze()
            display.update_display()

        # hold piece
        case 'c':
            print('c')
            ...
    
    display.print_grid()

    # check if the piece is on the floor or on top of another piece
    if not collision.bottom_is_empty(display.array):
        if clock.timer_stop_id is None:
            clock.start_timer()
    else:
        clock.stop_timer()


def freeze():
    '''Freezes the piece and spawns the next one. Resets the game tick.'''
    clock.stop_game_tick()
    move.freeze_piece(display.array)

    move.new_piece(display.array, (5,5), piece.Tshape)
    display.update_display()
    clock.start_game_tick()


if __name__ == '__main__':
    #display.array[10][3][0] = 2

    move.new_piece(display.array, (5,5), piece.Tshape)

    clock.start_game_tick()

    display.print_grid()
    display.update_display()




display.root.mainloop()