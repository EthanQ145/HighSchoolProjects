import tkinter as tk

main_window = tk.Tk()

image = tk.PhotoImage(file='cat_300.png')
text = tk.Text(main_window)
text.image_create(tk.END, image=image)

text.pack()

main_window.mainloop()
