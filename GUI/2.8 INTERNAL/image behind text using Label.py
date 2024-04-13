import tkinter as tk

main_window = tk.Tk()

image = tk.PhotoImage(file='cat_300.png')

canvas = tk.Canvas(main_window, bg='blue')
canvas.pack()

image_label = tk.Label(canvas, text='HELLO', compound=tk.CENTER, image=image, anchor=tk.CENTER)
canvas_label = canvas.create_window(200, 200, height = 80, width=200, window=image_label)

canvas_image = canvas.create_image(0, 0, image=image, anchor=tk.NW)
main_window.wm_attributes('-transparentcolor', 'cornsilk')

text = tk.Text(canvas, font=['Helvetica', '17', 'bold'], bg='cornsilk')
text.insert(tk.INSERT, 'HELLO')
canvas_text = canvas.create_window(30, 30, height=32, width=100, anchor=tk.NW, window=text)
canvas.tag_raise(canvas_text)


main_window.mainloop()

