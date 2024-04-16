from gui import Display
from movement import Move
from collision import Collision
from score import Score
import piece






class Clock:
    # variables to store tkinter 'after' function execution id
    timer_stop_id = None
    game_tick_stop_id = None

    def start_timer(self):
        '''Starts the timer. If the timer reaches the limit, the current piece freezes.'''
        self.timer_stop_id = display.root.after(1000, freeze_and_restart)

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


# class instances
clock = Clock()
display = Display()
move = Move()
collision = Collision()
choice = piece.Choice()
score = Score()


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
            freeze_and_restart()
            display.update_display()

        # hold piece
        case 'c':
            if move.can_store_piece:
                if move.stored_piece is not None:
                    stored_piece = move.stored_piece
                    move.hold_piece(display.array)
                    move.new_piece(display.array, stored_piece)
                elif move.stored_piece is None:
                    move.hold_piece(display.array)
                    move.new_piece(display.array, choice.dequeue())

                display.update_display()
                display.load_stored_piece(move.stored_piece)
                display.load_queue(choice.queue)
                move.can_store_piece = False
            
    
    # show game array in terminal
    #display.print_grid()

    # start freeze timer if the piece is on the floor or on top of another piece
    if not collision.bottom_is_empty(display.array):
        if clock.timer_stop_id is None:
            clock.start_timer()
    else:
        clock.stop_timer()


def freeze_and_restart():
    '''Freezes the current piece, checks for completed lines and spawn the next piece.'''
    clock.stop_game_tick()
    move.freeze_piece(display.array)
    if lines := score.search_completed_lines(display.array):
        score.clear_and_collapse(display.array, lines)
    move.new_piece(display.array, choice.dequeue())
    display.load_queue(choice.queue)
    display.update_display()
    clock.start_game_tick()
    move.can_store_piece = True


def start_game():
    '''Loads the queue, spawns a new piece and starts the game tick clock.'''
    choice.reset_queue()
    move.new_piece(display.array, choice.dequeue())
    display.load_queue(choice.queue)
    display.update_display()
    clock.start_game_tick()







if __name__ == '__main__':
    start_game()

    




display.root.mainloop()