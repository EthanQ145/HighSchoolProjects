"""28th March 2022. Flappy bird game.

By Ethan Q.
"""
# -----------IMPORTS--------------
import tkinter as tk
import random


# -----------CLASSES--------------
class GUI:
    """Represents the GUI of the game."""

    _WINDOW = tk.Tk()
    _WINDOW.title("Flappy bird")
    _WINDOW.resizable(False, False)
    _WALLPAPER = tk.PhotoImage(file="Background.png")
    # Height and width of the canvas
    WIDTH = _WALLPAPER.width()
    HEIGHT = _WALLPAPER.height()
    # Scoreboard location
    _SCORE_X_LOCATION = WIDTH / 2
    _SCORE_Y_LOCATION = HEIGHT * 0.1
    # Instruction location
    _INSTRUCTION_X_LOCATION = WIDTH * 1.2 / 2
    _INSTRUCTION_Y_LOCATION = HEIGHT / 2
    # Refresh rate of the program loop in ms
    _REFRESH_RATE = 15
    # Time before next pipe
    # Derived from refresh rate so distance between pipes are moderate
    _TIME_BETWEEN_PIPES = _REFRESH_RATE * 100
    # Default font
    _NUMBER_FONT = ['Times', int(WIDTH / 15)]
    _WORD_FONT = ["Helvetica", int(WIDTH / 35)]
    # Instructions
    _GAME_INSTRUCTIONS = "Press Space Bar / Left click to jump"

    def __init__(self):
        """Create GUI for the flappy bird game.

        attribute _score: the score number that will be updated.
        attribute _score_text: the canvas object containing _score.
        attribute _pipe_passed: pipes that the bird had passed.
        """
        # Create canvas and background
        self._canvas = tk.Canvas(GUI._WINDOW, width=GUI.WIDTH,
                                 height=GUI.HEIGHT)
        self._canvas.pack()
        self._background = self._canvas.create_image(
            0, 0, image=GUI._WALLPAPER, anchor='nw')
        # Create score, on top of background as it is created after
        self._score = 0
        self._score_text = self._canvas.create_text(
            GUI._SCORE_X_LOCATION, GUI._SCORE_Y_LOCATION,
            font=GUI._NUMBER_FONT, text=self._score, tags='score')
        # This variable show if score has already been added for this pipe
        self._pipe_passed = None
        # Create instructions, will be hidden when game starts
        self._game_instruction = self._canvas.create_text(
            GUI._INSTRUCTION_X_LOCATION, GUI._INSTRUCTION_Y_LOCATION,
            text=GUI._GAME_INSTRUCTIONS, font=GUI._WORD_FONT, state=tk.NORMAL)
        # Create bird, on top of score as it is created after
        self._bird = Bird(self._canvas)
        # List of pipes on canvas
        self._pipe_list = []
        # Time before next pipe appears
        self._time_before_next_pipe = 0
        # Bindings
        GUI._WINDOW.bind("<Button-1>", lambda _: self._start())
        GUI._WINDOW.bind("<space>", lambda _: self._start())
        GUI._WINDOW.mainloop()

    def _program_loop(self):
        """Loop that control the game.

        Move bird, pipes. Check for collisions. End game. Add score.
        """
        # Unbind jump control and end game if bird collide with pipe or ground
        if self._check_collision() or self._bird.get_coordinates()[3] >= \
                GUI.HEIGHT:
            # Avoid bird still jumping after collision
            GUI._WINDOW.unbind("<Button-1>")
            GUI._WINDOW.unbind("<space>")
            # Death animation
            self._bird.jump()
            self._drop()
        else:
            # Bird moves
            self._bird.move()
            # Create pipes
            self._time_before_next_pipe += GUI._REFRESH_RATE
            if self._time_before_next_pipe >= GUI._TIME_BETWEEN_PIPES:
                self._pipe = Pipe(self._canvas)
                self._pipe_list.append(self._pipe)
                self._time_before_next_pipe = 0
            # Move pipes
            for pipe in self._pipe_list:
                pipe.move()
            # Delete pipes that passed screen
            if self._pipe_list and \
                    self._pipe_list[0].get_x_coordinates()[1] < 0:
                self._pipe_list[0].remove_pipe()
                self._pipe_list.pop(0)
            # Adds score whenever the bird passes one pipe
            self._add_score()
            self._canvas.after(GUI._REFRESH_RATE, self._program_loop)

    def _add_score(self):
        """Add score when bird pass a pipe."""
        # Check if there is any pipes to avoid IndexError. Only check first
        # index because it's the closest pipe to bird. Check if score is
        # already added for pipe to avoid multiple scores for one pipe.
        if self._pipe_list and self._pipe_list[0].get_x_coordinates()[1] \
                < self._bird.get_coordinates()[0] and self._pipe_list[0] \
                != self._pipe_passed:
            self._score += 1
            self._canvas.itemconfigure(self._score_text, text=self._score)
            # Update variable to avoid score being added for this pipe
            self._pipe_passed = self._pipe_list[0]

    def _check_collision(self):
        """Check if there's a collision with the bird's coordinates.

        :return: True if there's a collision with pipe, False if there isn't.
        """
        overlaps = self._canvas.find_overlapping(*self._bird.get_coordinates())
        pipes = self._canvas.find_withtag('pipe')
        if pipes and (pipes[0] in overlaps or pipes[1] in overlaps):
            return True
        else:
            return False

    def _start(self):
        """Start the game."""
        # Set score to 0
        self._score = 0
        self._canvas.itemconfigure(self._score_text, text=self._score)
        # Rebind key to allow for bird to jump
        GUI._WINDOW.bind("<Button-1>", lambda _: self._bird.jump())
        GUI._WINDOW.bind("<space>", lambda _: self._bird.jump())
        # Hide instructions
        self._canvas.itemconfigure(self._game_instruction, state=tk.HIDDEN)
        # Bird jump once when game starts
        self._bird.jump()
        # Start game
        self._program_loop()

    def _drop(self):
        """End game, make bird drop to ground then restart."""
        if self._bird.get_coordinates()[3] < GUI.HEIGHT:
            self._bird.move()
            self._canvas.after(GUI._REFRESH_RATE, self._drop)
        else:
            self._restart()

    def _restart(self):
        """Restart the game."""
        # Reset variables
        self._time_before_next_pipe = 0
        self._pipe_passed = None
        # Delete pipes
        for pipe in self._pipe_list:
            pipe.remove_pipe()
        self._pipe_list = []
        # Reshow instruction
        self._canvas.itemconfigure(self._game_instruction, state=tk.NORMAL)
        # Reset position of bird
        self._bird.reset()
        # Rebind keys to start game
        GUI._WINDOW.bind("<Button-1>", lambda _: self._start())
        GUI._WINDOW.bind("<space>", lambda _: self._start())


class Bird:
    """Represents the bird that is jumping through the pipes."""

    _HEIGHT = GUI.HEIGHT / 13
    _WIDTH = _HEIGHT * 1.2
    _COLOUR = "#d962cb"
    _OUTLINE_COLOUR = "#663c99"
    _OUTLINE_WIDTH = 3
    # Constants for the bird's location
    _X_LOCATION = GUI.WIDTH * 0.2 - _WIDTH / 2
    _Y_LOCATION = GUI.HEIGHT / 2 - _HEIGHT / 2
    # Constants for speeds
    _JUMP_SPEED = GUI.HEIGHT / 50
    _GRAVITY = _JUMP_SPEED / 20
    # Make fall not become too fast
    _AIR_RESISTANCE = _HEIGHT / 2.5

    def __init__(self, canvas):
        """Create rectangle at Bird._X_PLACEMENT and Bird._Y_PLACEMENT as bird.

        attribute _y_speed: the vertical velocity of the bird.
        """
        self._canvas = canvas
        self._bird = self._canvas.create_oval(
            Bird._X_LOCATION, Bird._Y_LOCATION, Bird._X_LOCATION + Bird._WIDTH,
            Bird._Y_LOCATION + Bird._HEIGHT, fill=Bird._COLOUR, tags='bird',
            outline=Bird._OUTLINE_COLOUR, width=Bird._OUTLINE_WIDTH)
        # Vertical speed, will be Bird._JUMP_SPEED when game starts
        self._y_speed = 0

    def jump(self):
        """Set jump velocity so move() can make the bird jump."""
        self._y_speed = -Bird._JUMP_SPEED

    def move(self):
        """Responsible for the bird's movement, make the bird fall and jump."""
        # Move bird speed set by self._y_speed, bird can't go above canvas
        if self.get_coordinates()[1] > 0:
            self._canvas.move(self._bird, 0, self._y_speed)
        else:
            # If bird tries to go above canvas, move bird back to top of canvas
            self._canvas.moveto(self._bird, Bird._X_LOCATION, 0)
            self._y_speed = 0
        # Limit fall speed, limit is Bird._AIR_RESISTANCE
        if self._y_speed <= Bird._AIR_RESISTANCE:
            # Make bird accelerate downwards
            self._y_speed += Bird._GRAVITY

    def get_coordinates(self):
        """Return bird's coordinates in the canvas.

        :return: List with bird's left, top, right, bottom coordinates.
        """
        return self._canvas.coords(self._bird)

    def reset(self):
        """Move bird back to starting position when game is restarted."""
        self._canvas.moveto(self._bird, Bird._X_LOCATION, Bird._Y_LOCATION)


class Pipe:
    """Represents the pipes that are travelling to the left on the window."""

    _PIPE_IMAGE = tk.PhotoImage(file="Pipe.png")
    _WIDTH = _PIPE_IMAGE.width()
    _GAP_SIZE = GUI.HEIGHT * 0.35
    if _PIPE_IMAGE.height() <= GUI.HEIGHT - _GAP_SIZE:
        raise Exception("Pipe is too short for this background")
    elif _PIPE_IMAGE.width() < GUI.WIDTH * 0.015:
        raise Exception("Pipe is too thin for this background")
    elif _PIPE_IMAGE.width() > GUI.WIDTH * 0.15:
        raise Exception("Pipe is too wide for this background")
    # Boundaries so gap isn't too close to top or bottom of window
    _GAP_BOUNDARY = GUI.HEIGHT * 0.05
    # Speed that the pipe travels to the left
    _SPEED = GUI.WIDTH * 0.005

    def __init__(self, canvas):
        """Create 2 images stacking with a gap vertically as pipe with gap.

        attribute _gap_position: the vertical position of pipe gap.
        attribute _top_pipe: the top rectangle of the pipe.
        attribute _bottom_pipe: the bottom rectangle of the pipe.
        """
        self._canvas = canvas
        # Set random gap position with boundaries at top and bottom of window
        self._gap_position = random.randint(
            round(Pipe._GAP_SIZE + Pipe._GAP_BOUNDARY),
            round(GUI.HEIGHT - Pipe._GAP_BOUNDARY))
        self._top_pipe = self._canvas.create_image(
            GUI.WIDTH, self._gap_position - Pipe._GAP_SIZE,
            image=Pipe._PIPE_IMAGE, tags='pipe', anchor='sw')
        self._bottom_pipe = self._canvas.create_image(
            GUI.WIDTH, self._gap_position,
            image=Pipe._PIPE_IMAGE, tags='pipe', anchor='nw')
        # Pipe is below score and therefore below bird
        self._canvas.tag_lower(self._top_pipe, 'score')
        self._canvas.tag_lower(self._bottom_pipe, 'score')

    def move(self):
        """Move pipe to left of canvas."""
        self._canvas.move(self._top_pipe, -Pipe._SPEED, 0)
        self._canvas.move(self._bottom_pipe, -Pipe._SPEED, 0)

    def remove_pipe(self):
        """Remove pipe from canvas."""
        self._canvas.delete(self._top_pipe)
        self._canvas.delete(self._bottom_pipe)

    def get_x_coordinates(self):
        """Return horizontal coordinates of top and bottom pipe in the canvas.

        :return: List of left, right location of top pipe, same as bottom pipe.
        """
        # Anchor west so first index will be x1, so x2 will be x1 + width
        return [self._canvas.coords(self._top_pipe)[0],
                self._canvas.coords(self._top_pipe)[0] + Pipe._WIDTH]


if __name__ == "__main__":
    GUI()
