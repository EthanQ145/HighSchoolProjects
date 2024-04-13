# =======Imports=============
import tkinter as tk
import math
import random
import time

# =======Set Variable========
SIZE = 40
WIDTH = 11
HEIGHT = 11
SPEED = 3
x_speed, y_speed = 0, 0
player_x, player_y = 0, 0
start_time = 0
x1, y1, x2, y2 = 0, 0, 0, 0
movement = []

# =======Functions===========


def key_pressed(event):
    """check whether player entered movement command

    :param: event = property of key pressed
    """
    global x_speed, y_speed, start_time
    if event.char == "w" or event.keysym == "Up":
        y_speed = -SPEED
    elif event.char == "a" or event.keysym == "Left":
        x_speed = -SPEED
    elif event.char == "s" or event.keysym == "Down":
        y_speed = SPEED
    elif event.char == "d" or event.keysym == "Right":
        x_speed = SPEED
    if start_time == 0:
        start_time = time.time()
    canvas.unbind("<KeyPress>")


def key_released(event):
    global x_speed, y_speed
    x_speed = 0
    y_speed = 0
    canvas.bind("<KeyPress>", key_pressed)


def player_move():
    global player_x, player_y, x_speed, y_speed, start_time, x1, y1, x2, y2, movement
    canvas.move(player, x_speed, y_speed)
    overlapping = list(canvas.find_overlapping(*canvas.coords(player)))
    if len(overlapping) > 1:
        if len(list(canvas.find_overlapping(*canvas.coords(goal)))) > 1:
            canvas.delete("all")
            print("{:.3}s".format(time.time() - start_time))
            start_time = 0
            main()
        else:
            canvas.coords(player, x1, y1, x2, y2)
    else:
        player_x += x_speed
        player_y += y_speed
    if len(overlapping) == 1:
        x1 = player_x - SIZE * 0.2
        x2 = player_x + SIZE * 0.2
        y1 = player_y - SIZE * 0.2
        y2 = player_y + SIZE * 0.2
    window.after(10, player_move)


def random_maze_generator():
    """ Generates a random maze"""

    # Variables
    path = []
    m = WIDTH - 2
    n = HEIGHT - 2
    the_maze = {}

    # outline the maze
    for o in range(HEIGHT):
        for p in range(WIDTH):
            if (math.ceil(o % 2) == 0) or (math.ceil(p % 2) == 0):
                the_maze[p, o] = "##"
            else:
                the_maze[p, o] = "U"

    # set each cell of the maze
    for o in range(WIDTH + 1):
        the_maze[o, -1] = "##"
        the_maze[o, HEIGHT] = "##"
    for p in range(HEIGHT + 1):
        the_maze[-1, p] = "##"
        the_maze[WIDTH, p] = "##"

    # set staring point
    the_maze[m, n] = "A"

    # loop until every tile has been reached
    while "U" in the_maze.values():

        # find possible directions to unreached tiles
        choices = []
        if the_maze[m, n - 2] == "U":
            choices.append("N")
        if the_maze[m + 2, n] == "U":
            choices.append("E")
        if the_maze[m, n + 2] == "U":
            choices.append("S")
        if the_maze[m - 2, n] == "U":
            choices.append("W")

        # check is there is a possible directions
        if choices:
            # choose a random possible direction
            direction = random.choice(choices)
        else:
            # move back to the previous location
            m, n = path[0]
            path.pop(0)
            direction = 0

        # move base on the direction
        if direction == "N":
            move = m, n
            the_maze[m, n - 1] = "  "
            the_maze[m, n - 2] = "  "
            n -= 2
        elif direction == "E":
            move = m, n
            the_maze[m + 1, n] = "  "
            the_maze[m + 2, n] = "  "
            m += 2
        elif direction == "S":
            move = m, n
            the_maze[m, n + 1] = "  "
            the_maze[m, n + 2] = "  "
            n += 2
        elif direction == "W":
            move = m, n
            the_maze[m - 1, n] = "  "
            the_maze[m - 2, n] = "  "
            m -= 2
        else:
            move = 0

        # record the moves
        if move:
            path.insert(0, move)

    return the_maze


def main():
    global goal, player_x, player_y, player
    maze = random_maze_generator()
    goal = canvas.create_rectangle(SIZE, SIZE, 2*SIZE, 2*SIZE, fill="green",
                                   outline="")
    player_x, player_y = SIZE*(WIDTH-1.5), SIZE*(HEIGHT-1.5)
    # Resize and print the maze
    for i in range(0, WIDTH*SIZE, SIZE):
        for j in range(0, HEIGHT*SIZE, SIZE):
            if maze[i/SIZE, j/SIZE] == "##":
                canvas.create_rectangle(i, j, i+SIZE, j+SIZE, fill="red",
                                        outline="")

    player = canvas.create_rectangle(SIZE*(WIDTH-1.7), SIZE*(HEIGHT-1.7),
                                     SIZE*(WIDTH-1.3), SIZE*(HEIGHT-1.3),
                                     fill="blue", outline="")


# =======Main Window===========
window = tk.Tk()
window.geometry("{}x{}+0+0".format(WIDTH*SIZE, HEIGHT*SIZE))


canvas = tk.Canvas(window, width=WIDTH*SIZE, height=HEIGHT*SIZE,
                   background="BlanchedAlmond")
canvas.bind("<KeyPress>", key_pressed)
canvas.bind("<KeyRelease>", key_released)
canvas.focus_set()
canvas.pack()

main()
player_move()

window.mainloop()
