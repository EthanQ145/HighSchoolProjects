import tkinter as tk


def check(event):
    if input_box.get() == '':
        word.tag_remove('Correct', 1.0, tk.END)
        word.tag_remove('Wrong', 1.0, tk.END)
        word.config(fg='black')
    else:
        for letter_index in range(len(list(input_box.get()))):
            word.tag_remove('Correct', 1.0 + letter_index/10, tk.END)
            word.tag_remove('Wrong', 1.0 + letter_index/10, tk.END)
            try:
                if input_box.get()[letter_index] == word.get(1.0, tk.END)[letter_index]:
                    word.tag_add('Correct', 1 + letter_index/10, 1 + (letter_index + 1)/10)
                else:
                    word.tag_add('Wrong', 1 + letter_index/10, 1 + (letter_index + 1)/10)
            except IndexError:
                word.tag_add('Wrong', 1 + letter_index/10, 1 + (letter_index + 1)/10)
        word.tag_config('Correct', foreground="green")
        word.tag_config('Wrong', foreground="red")


main_window = tk.Tk()
word = tk.Text(main_window, font=['Helvetica', '30'], width=10, height=1)
word.insert(tk.INSERT, "Hello")
word.config(state=tk.DISABLED)
input_box = tk.Entry(main_window, width=30)
word.pack()
input_box.pack()
input_box.focus_set()
main_window.bind("<Key>", check)
main_window.mainloop()
