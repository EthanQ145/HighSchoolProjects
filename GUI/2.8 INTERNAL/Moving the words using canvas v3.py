"""
Adding the menu function
"""

import tkinter as tk
import random

# ===========VARIABLES===============

BACKGROUND_COLOUR = 'khaki'
ENGLISH_WORDS_LEVEL_1 = open("English words 1").readlines()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
# For the correct timing between each word being printed
print_word_loop_delay = 0
seconds_between_words = 1
# For printing next word
current_word_index = 0
# Formatting for the lane where words move in
WORDS_MOVING_BORDER = 120
SPEED = 1

texts = []
# ==========FUNCTIONS=============


def menu():
    menu_frame.pack()
    menu_frame.pack_propagate(0)


def start_game(event):
    # Leaves menu screen
    menu_frame.pack_forget()

    # Disable the start button through pressing Enter (binding) while the game is on going
    main_window.unbind("<Return>")

    # Packs the game screen
    playing_lane.pack()

    # Enable the entry box so the user can type and put user's cursor on Entry box
    user_typing_input.configure(state=tk.NORMAL)
    user_typing_input.focus_set()
    result.set('Type the words on window')
    the_results.configure(bg='light green')

    # Set the amount of words left for the user to type, if there are none then the game ends
    program_loop()


def end_game():
    global current_word_index

    # Deletes the top and bottom frame and the Entry box
    playing_lane.pack_forget()

    # Open menu
    menu()

    # Return the start game button back to normal for the user to restart the game
    main_window.bind("<Return>", start_game)

    # Disable the entry box until the user starts the game, prints the score
    # Resets the score and indexes to prepare for the next game
    user_typing_input.configure(state=tk.DISABLED)
    current_word_index = 0


def program_loop():
    global print_word_loop_delay
    # Printing a word every second
    if print_word_loop_delay == 0 and current_word_index <= len(ENGLISH_WORDS_LEVEL_1) - 1:
        print_word()
        print_word_loop_delay = seconds_between_words * 100
    print_word_loop_delay -= 1

    # Move the words
    if texts:
        if playing_lane.coords('word')[0] >= 0:
            playing_lane.move('word', -SPEED, 0)
        else:
            playing_lane.delete(texts[0])
            texts.pop(0)
        main_window.after(10, program_loop)
    else:
        print_word_loop_delay = 0
        end_game()


def print_word():
    """
    Creates the label at index
    :return: Prints the word at the current i
    """
    global current_word_index
    # Coordinates of the words
    x_coord = WINDOW_WIDTH
    y_coord = random.randint(20, WINDOW_HEIGHT - WORDS_MOVING_BORDER)

    # Creates text
    word = ENGLISH_WORDS_LEVEL_1[current_word_index].strip()
    text_printed = tk.Text(playing_lane, font=['Helvetica', '17', 'bold'], width=len(word) + 1)
    text_printed.insert(tk.INSERT, word)
    text_printed.config(state=tk.DISABLED)

    words_printed = playing_lane.create_window(x_coord,
                                               y_coord,
                                               height=32, anchor=tk.W,
                                               window=text_printed, tag=['word'])

    # Store the label to a list of labels
    texts.append(words_printed)

    # If there are still words left, create another label with the next word on it
    current_word_index += 1


# ===========MAIN===============
main_window = tk.Tk()
main_window.geometry('1000x600+0+0')
main_window.configure(bg='gold')

# MENU SCREEN
menu_frame = tk.Frame(main_window,  width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOUR)

name = tk.Label(menu_frame, text='TYPING TEST', font=['Times', '36', 'bold'], bg='DodgerBlue2')

start_game_button = tk.Button(menu_frame, text='START', font=['Helvetica', '25', 'bold'], bg='turquoise',
                              command=lambda: start_game("<Return>"), padx=30, pady=10)
main_window.bind("<Return>", start_game)

menu_instruction = tk.StringVar(menu_frame)
menu_instructions = tk.Label(menu_frame, textvariable=menu_instruction, font=['Sans', '17'], width=50)
menu_instruction.set('Click START button or press Enter to begin typing test')

name.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
start_game_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
menu_instructions.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# GAME SCREEN
playing_lane = tk.Canvas(main_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='khaki')

result = tk.StringVar(playing_lane)
the_results = tk.Label(playing_lane, textvariable=result, font=['Sans', '17'], width=50)
result.set('Type the moving words on window')

user_input = tk.StringVar(playing_lane)
user_typing_input = tk.Entry(playing_lane, width=10, state=tk.DISABLED,
                             textvariable=user_input, font=['Helvetica', '20'])

user_typing_input.place(relx=0.01, rely=0.5, anchor=tk.W)
the_results.place(relx=0.5, rely=0.95, anchor=tk.S)

menu()

main_window.mainloop()
