"""Practising adding image file to tkinter label




"""

import tkinter as tk

main_window = tk.Tk()
main_window.geometry("800x450+10+20")

label_img = tk.PhotoImage(file="cat_300.png")
label_cat = tk.Label(main_window, padx=100, pady=100, image=label_img)
label_cat.pack()

main_window.mainloop()