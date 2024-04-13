import tkinter as tk

main_window = tk.Tk()


text = tk.Text(main_window, bg='cornsilk')
text.insert(tk.INSERT, 'hello')
main_window.wm_attributes('-transparentcolor', 'cornsilk')

image = tk.PhotoImage(file='cat_300.png')

image_lbl = tk.Label(main_window, image=image)

text.window_create(tk.END, )
text.pack()

main_window.mainloop()

