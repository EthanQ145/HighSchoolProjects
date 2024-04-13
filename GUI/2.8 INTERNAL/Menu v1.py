import tkinter as tk

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WORDS_MOVING_BORDER = 100


def start_game(event):
    global start_game_button, the_result
    # Removes the title on menu and replace the start button
    name.place_forget()
    start_game_button.place_forget()
    the_result.place_forget()

    # Packs the entry box
    top_frame = tk.Frame(main_window, width=WINDOW_WIDTH, height=WORDS_MOVING_BORDER - 30, bg='red')

    bottom_frame = tk.Frame(main_window, width=WINDOW_WIDTH, height=WORDS_MOVING_BORDER - 30, bg='red')

    the_result = tk.Label(bottom_frame, textvariable=result, font=['Sans', '17'], width=50, bg='SpringGreen2')
    result.set('Click START button or press Enter to begin typing test')

    start_game_button = tk.Button(top_frame, text='START', font=['Helvetica', '25', 'bold'], bg='turquoise',
                                  command=lambda: start_game("<Return>"), padx=30, pady=10)

    top_frame.config(bg='DeepSkyBlue2')
    bottom_frame.config(bg='DeepSkyBlue2')
    top_frame.pack(side=tk.TOP)
    top_frame.pack_propagate(0)
    bottom_frame.pack(side=tk.BOTTOM)
    bottom_frame.pack_propagate(0)

    start_game_button.pack(side=tk.TOP)
    the_result.pack(side=tk.BOTTOM)

    user_typing_input.pack(side=tk.LEFT, padx=10)


main_window = tk.Tk()
main_window.geometry('1000x600+0+0')
BACKGROUND_COLOUR = 'gold'
main_window.configure(bg=BACKGROUND_COLOUR)
main_window.title('Typing test')

name = tk.Label(main_window, text='TYPING TEST', font=['Times', '36', 'bold'], bg='salmon')
name.pack(side=tk.TOP)

start_game_button = tk.Button(main_window, text='START', font=['Helvetica', '25', 'bold'], bg='light salmon',
                              command=lambda: start_game("<Return>"), padx=30, pady=10)
main_window.bind("<Return>", start_game)
start_game_button.pack(side=tk.TOP)

result = tk.StringVar(main_window)
the_result = tk.Label(main_window, textvariable=result, font=['Sans', '17'], width=50, bg='SpringGreen2')
result.set('Click START button or press Enter to begin typing test')
the_result.pack(side=tk.BOTTOM)

main_window.update()
x_for_name = name.winfo_x()
name.place(x=x_for_name, y=WINDOW_HEIGHT/2 - WORDS_MOVING_BORDER)

x_for_start_button = start_game_button.winfo_x()
start_game_button.place(x=x_for_start_button, y=WINDOW_HEIGHT/2)

x_for_result_label = the_result.winfo_x()
the_result.place(x=x_for_result_label, y=WINDOW_HEIGHT-WORDS_MOVING_BORDER)


user_input = tk.StringVar(main_window)
user_typing_input = tk.Entry(main_window, width=10, state=tk.DISABLED,
                             textvariable=user_input, font=['Helvetica', '20'])


main_window.mainloop()