from tkinter import *
import random
window = Tk()
window.title("Drawing shapes")
window.geometry('1500x800')
canvas = Canvas(window, height=700, width=1000, bg="yellow")
COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
pressing = False


def pressed(event):
    window.focus_set()
    x = event.x
    y = event.y
    print('User pressed at x = {}, y = {}'.format(x, y))


def moving(event):
    x = event.x
    y = event.y
    print("Coordinates: {}, {}".format(x, y))
    size = 50
    random_size = random.randint(50, 150)
    square = canvas.create_rectangle(size, size, random_size, random_size, fill=random.choice(COLORS))
    canvas.move(square, x - (size + random_size)/2, y - (size + random_size)/2)


def released():
    print('User released, colour changed to {}'.format(random.choice(COLORS)))
    canvas.config(bg=random.choice(COLORS))


canvas.grid(column=3, row=800)
canvas.bind('<ButtonPress-1>', pressed)
canvas.bind('<B1-Motion>', moving)
canvas.bind('<ButtonRelease-1>', lambda event: [pressed(event), released()])


window.mainloop()
