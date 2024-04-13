from tkinter import *
import random
window = Tk()
window.title("Drawing shapes")
window.geometry('1500x800')
canvas = Canvas(window, height=700, width=1000, bg="yellow")
COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
pressing = False


def moving(event):
    print("Coordinates: {}, {}".format(event.x, event.y))
    size = 50
    random_size = random.randint(50, 150)
    square = canvas.create_rectangle(size, size, random_size, random_size, fill=random.choice(COLORS))
    canvas.move(square, event.x - (size + random_size)/2, event.y - (size + random_size)/2)


def released(event):
    print('User released at: {}, {}\n Colour changed to {}'.format(event.x, event.y, random.choice(COLORS)))
    canvas.config(bg=random.choice(COLORS))


canvas.grid(column=3, row=800)
canvas.bind('<B1-Motion>', moving)
canvas.bind('<ButtonRelease-1>', released)


window.mainloop()
