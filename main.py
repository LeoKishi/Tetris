from gui import Display
from movement import Move
from collision import Collision
from points import Points
from piece import Choice
from playsound import playsound


class Clock:
    # variables to store tkinter 'after' function execution id
    timer_stop_id = None
    game_tick_stop_id = None

    # game tick speed
    speed = 720

    game_is_paused = True

    def start_timer(self):
        '''Starts the timer. If the timer reaches the limit, the current piece freezes.'''
        self.timer_stop_id = display.root.after(1000, freeze)

    def stop_timer(self):
        '''Stops the timer if the timer is currently running.'''
        if self.timer_stop_id is not None:
            display.root.after_cancel(self.timer_stop_id)
            self.timer_stop_id = None

    def start_game_tick(self):
        '''Starts the game tick. Makes the piece move one step downwards for each tick.'''
        if self.game_tick_stop_id is not None:
            move.down(display.array)
            display.update_display()
            freeze_timer()
            display.ghost_piece(move.get_ghost_piece(display.array), move.current_shape.code)
        self.game_tick_stop_id = display.root.after(self.speed, self.start_game_tick)

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
choice = Choice()
points = Points()


# bind user input
display.root.bind('<Key>', lambda event: actions(event.keysym))


def actions(key: str):
    '''Executes action for corresponding key pressed.'''
    if not move.topped_out:
        match key:
            # rotate piece
            case 'Up':
                move.rotate(display.array)
                display.update_display()

            # move piece one step downwards
            case 'Down':
                if move.down(display.array):
                    display.update_display()
                    points.score += 1
                    display.score_var.set(points.score)

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
                playsound('assets/click.wav', block=False)
                clock.stop_timer()
                count = move.drop(display.array)
                points.score += count*2
                display.score_var.set(points.score)
                freeze()
                display.update_display()
                return

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

        freeze_timer()
        display.ghost_piece(move.get_ghost_piece(display.array), move.current_shape.code)

    elif key == 'space' and clock.game_is_paused:
        move.topped_out = False
        start_game()
        display.show_game_grid()
        display.start_game_label.destroy()


def freeze_timer():
    '''Starts the freeze timer if the piece is on the floor or on top of another piece'''
    if not collision.bottom_is_empty(display.array):
        if clock.timer_stop_id is None:
            clock.start_timer()
    else:
        clock.stop_timer()


def freeze():
    '''Freezes the current piece, checks for completed lines and spawn the next piece.'''
    clock.stop_game_tick()
    move.freeze_piece(display.array)

    if collision.top_out(display.array):
        move.topped_out = True

        if is_highscore:= points.score > points.get_highscore():
            points.new_highscore(points.score)

        display.show_score(points.lines, points.score, points.get_highscore(), is_highscore)
        display.ending_animation()

        playsound('assets/top out.wav', block=False)

        reset_values()

        display.root.after(2750, enable_play_again)
        return

    if lines := points.search_completed_lines(display.array):
        points.clear_and_collapse(display.array, lines)

        if len(lines) < 3:
            playsound('assets/small clear.wav', block=False)
        else:
            playsound('assets/big clear.wav', block=False)

        points.score += points.get_points(lines)

        display.lines_var.set(points.lines)
        display.score_var.set(points.score)
        set_game_speed()

    move.new_piece(display.array, choice.dequeue())

    display.load_queue(choice.queue)
    display.update_display()

    clock.start_game_tick()
    move.can_store_piece = True
    clock.timer_stop_id = None


def start_game():
    '''Loads the queue, spawns a new piece and starts the game tick clock.'''
    choice.fill_queue()

    move.new_piece(display.array, choice.dequeue())

    display.load_queue(choice.queue)
    display.update_display()

    clock.start_game_tick()
    clock.game_is_paused = False

    
def set_game_speed():
    '''Speeds up the game tick as the game progresses.'''
    if clock.speed > 150:
        clock.speed = 720 - (70*points.level)
    elif clock.speed > 30:
        clock.speed -= 10


def reset_values():
    move.clear(display.array)
    points.clear()
    choice.clear()
    clock.speed = 720


def enable_play_again():
    clock.game_is_paused = True



if __name__ == '__main__':




    display.root.mainloop()