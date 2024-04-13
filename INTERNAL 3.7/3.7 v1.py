import tkinter as tk


class GUI:
    HEIGHT = 500
    WIDTH = 500
    _WINDOW = tk.Tk()
    _WINDOW.title("Flappy, shooty bird")
    _WINDOW.geometry("{}x{}".format(HEIGHT, WIDTH))
    CANVAS = tk.Canvas(_WINDOW, height=HEIGHT, width=WIDTH, background="red")
    CANVAS.pack()

    def __init__(self):
        bird = Bird()

        GUI._WINDOW.mainloop()


class Bird:
    _HEIGHT = 10
    _WIDTH = 10

    def __init__(self):
        GUI.CANVAS.create_rectangle(GUI.WIDTH * 0.2 - Bird._WIDTH / 2,
                                    GUI.HEIGHT / 2 - Bird._HEIGHT / 2,
                                    GUI.WIDTH * 0.2 + Bird._WIDTH / 2,
                                    GUI.HEIGHT / 2 + Bird._HEIGHT / 2,
                                    fill="yellow")



GUI()
