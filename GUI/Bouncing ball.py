"""


"""

import tkinter as tk
import random

canvas_hidden = True
ball_stopped = False
WIDTH = 590
HEIGHT = 450


def show_canvas():
    global canvas_hidden
    if canvas_hidden:
        graphics.pack(side=tk.LEFT)
        instructions_label.config(text="Click Show/Hide Button to Hide Canvas")
        canvas_hidden = False
    else:
        graphics.pack_forget()
        instructions_label.config(text="Click Show/Hide Button to Display Canvas")
        canvas_hidden = True


def set_focus_canvas(event):
    graphics.focus_set()


def move_ball(count):
    global speed_x, speed_y, ball_stopped
    if count == 0:
        speed_x = random.randrange(1, 10)
        speed_y = random.randrange(1, 10)
        ball_stopped = False
    count = 1
    graphics.move(red_ball, speed_x, speed_y)
    position = graphics.coords(red_ball)
    print(position[2], WIDTH, "speed x:", speed_x)
    if position[2] >= WIDTH or position[0] <= 0:
        speed_x *= -1
        print(speed_x)
    if position[3] >= HEIGHT or position[1] <= 0:
        speed_y *= -1
    print(count)
    main_window.update_idletasks()
    if not ball_stopped:
        main_window.after(30, lambda: move_ball(count))


def stop_ball():
    global speed_x, speed_y, ball_stopped
    speed_x = 0
    speed_y = 0
    ball_stopped = True


main_window = tk.Tk()
main_window.title("Canvas appear")
main_window.geometry("800x450+10+10")

left_frame = tk.Frame(main_window, width="200", height='450', bg='yellow')
left_frame.pack(side=tk.LEFT, fill=tk.Y)
left_frame.pack_propagate(0)

instructions_label = tk.Label(left_frame, text="Click Show/Hide Button to Display Canvas",
                              relief="groove", fg="white", bg="black", font=("Verdana", "10"),
                              wraplength="180")
# wrap length means text wrapped after 180 characters

instructions_label.pack(anchor=tk.N, fill=tk.X, pady="5", padx="5")

graphics = tk.Canvas(main_window, width="600", height="450", bg="light blue")

blue_rectangle = graphics.create_rectangle(100, 150, 250, 300, fill="blue")

red_ball = graphics.create_oval(0, 0, 100, 150, fill="red", activefill="red", dash=(1, 1))

move_count = 0
move_ball_btn = tk.Button(left_frame, text="Move Ball", command=lambda: move_ball(move_count))
move_ball_btn.pack()

stop_ball_btn = tk.Button(left_frame, text="Stop Ball", command=stop_ball)
stop_ball_btn.pack()

graphics.bind("<Button-1>", set_focus_canvas)

show_hide_btn = tk.Button(left_frame, text="Show/Hide", command=show_canvas)
show_hide_btn.pack()

main_window.mainloop()
