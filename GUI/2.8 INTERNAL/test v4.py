import tkinter as tk

main_window = tk.Tk()
main_window.geometry("1000x600+0+0")
numbers = ['1', '2', '3', '4', '5']
value = 0
coord = 0


def create_label():
    global value, coord
    coord = 0
    if value < len(numbers) - 1:
        value += 1
        move_label(tk.Label(main_window, text=numbers[value]))
        main_window.after(1000, create_label)


def move_label(target):
    global coord
    print(value)
    target.place(x=coord, y=value*100)
    main_window.after(10, lambda: move_label(target))


start_button = tk.Button(main_window, text="start", command=create_label)
start_button.grid(column=1, row=0)
main_window.mainloop()
