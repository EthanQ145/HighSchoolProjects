"""
This version fixes the problem of the v1 one, this is because it recalls the function again, therefore it can recheck
and turn the few matching letters at the start and turn it to green.
"""


import tkinter as tk
import random

# ===========VARIABLES===============
ENGLISH_WORDS_LEVEL_1 = open("English words 1").readlines()
i = 0
score = 0
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

WORDS_MOVING_BORDER = 100
SPEED = 2

words_left = 0
seconds_between_words = 1
texts = []
texts_value = []
typed_correctly = False
words_being_typed = 0
# ==========FUNCTIONS=============


def menu():
    global name, start_game_button, result, the_result, user_input, user_typing_input
    name = tk.Label(main_window, text='TYPING TEST', font=['Times', '36', 'bold'], bg='DodgerBlue2')
    name.pack(side=tk.TOP)

    start_game_button = tk.Button(main_window, text='START', font=['Helvetica', '25', 'bold'], bg='orchid1',
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


def start_game(event):
    global words_left, start_game_button, the_result, top_frame, bottom_frame
    # Removes the title on menu and replace the start button
    name.place_forget()
    start_game_button.place_forget()
    the_result.place_forget()

    # Packs the entry box
    top_frame = tk.Frame(main_window, width=WINDOW_WIDTH, height=WORDS_MOVING_BORDER - 30, bg='DeepSkyBlue2')

    bottom_frame = tk.Frame(main_window, width=WINDOW_WIDTH, height=WORDS_MOVING_BORDER - 30, bg='DeepSkyBlue2')

    the_result = tk.Label(bottom_frame, textvariable=result, font=['Sans', '17'], width=50, bg='SpringGreen2')
    result.set('Click START button or press Enter to begin typing test')

    start_game_button = tk.Button(top_frame, text='START', font=['Helvetica', '25', 'bold'], bg='turquoise',
                                  command=lambda: start_game("<Return>"), padx=30, pady=10)

    top_frame.pack(side=tk.TOP)
    top_frame.pack_propagate(0)
    bottom_frame.pack(side=tk.BOTTOM)
    bottom_frame.pack_propagate(0)

    start_game_button.pack(side=tk.TOP)
    the_result.pack(side=tk.BOTTOM)

    user_typing_input.pack(side=tk.LEFT, padx=10)

    # Disable the start button through clicking and pressing Enter (binding) while the game is on going
    start_game_button.configure(state=tk.DISABLED)
    main_window.unbind("<Return>")

    # Enable the entry box so the user can type and put user's cursor on Entry box
    user_typing_input.configure(state=tk.NORMAL)
    user_typing_input.focus_set()
    result.set('Type the words on window')
    the_result.configure(bg='light green')
    main_window.bind('<Key>', change_letter_colour)

    # Set the amount of words left for the user to type, if there are none then the game ends
    words_left = len(ENGLISH_WORDS_LEVEL_1)
    print_word()


def print_word():
    """
    Creates the label at index
    :return: Prints the word at the current i
    """
    global i, score, texts, texts_value

    # Creates a new label
    word = ENGLISH_WORDS_LEVEL_1[i].strip()
    words_printed = tk.Text(main_window, width=len(ENGLISH_WORDS_LEVEL_1[i].strip()), height=1, relief=tk.FLAT)
    words_printed.window_create(tk.END, window=tk.Label(words_printed, image=enemy_image))
    words_printed.insert(tk.INSERT, word)
    words_printed.config(font=['Helvetica', '17', 'bold'], width=len(word) + 1, state=tk.DISABLED)

    # Places the label on the left of the window, at a random height.
    words_printed.place(x=WINDOW_WIDTH, y=random.randint(WORDS_MOVING_BORDER, WINDOW_HEIGHT - WORDS_MOVING_BORDER))

    # Update the window so that the labels are placed
    main_window.update()

    # Store the label to a list of labels that is used in the move_word function
    texts.append(words_printed)

    # Store the text of the labels inside a list, which is used in check_user_typing and change_letter_colour function
    texts_value.append(words_printed.get(1.0, tk.END))
    move_word(words_printed)

    # If there are still words left, create another label with the next word on it
    if i < len(ENGLISH_WORDS_LEVEL_1) - 1:
        i += 1
        main_window.after(int(seconds_between_words * 1000), print_word)


def move_word(text):
    """
    This use the index passed through at the parameter to pick out the targeted label, and moves it
    """
    global i, score, texts, texts_value, words_left, top_frame, bottom_frame
    # Only get the coordinates of the label if the label still exists
    if text in texts:
        x = text.winfo_x()
        y = text.winfo_y()
    # Only move the label to the left if the label is still on the screen
        if x > 0:
            text.place(x=x - SPEED*2, y=y)
            main_window.after(20, lambda: move_word(text))
    # If the label is not on the screen anymore, destroy the label
        else:
            # Clear the entry box if the word that the user is typing already gone out of the screen
            if text.tag_names() == ('sel', 'Typed') and words_being_typed == 1:
                user_typing_input.delete(0, tk.END)
            texts.remove(text)
            texts_value.remove(text.get(1.0, tk.END))
            text.place_forget()
            words_left -= 1

    # Ends the game if there are no words left
    if words_left == 0:
        user_typing_input.delete(0, tk.END)
        main_window.unbind("<Key>")

        # Deletes the top and bottom frame and the Entry box
        top_frame.pack_forget()
        bottom_frame.pack_forget()
        user_typing_input.pack_forget()

        # Open menu
        menu()

        # Return the start game button back to normal for the user to restart the game
        start_game_button.configure(state=tk.NORMAL)
        main_window.bind("<Return>", start_game)

        # Disable the entry box until the user starts the game, prints the score
        # Resets the score and indexes to prepare for the next game
        user_typing_input.configure(state=tk.DISABLED)
        result.set("Score: {}/{}\n Retry?".format(score, len(ENGLISH_WORDS_LEVEL_1)))
        the_result.configure(bg='cyan')
        score = 0
        i = 0


def change_letter_colour(event):
    global score, texts, texts_value, words_left, typed_correctly, words_being_typed
    if words_being_typed > 0:
        result.set('Type the words on window')
        the_result.configure(bg='light green')
    words_being_typed = 0
    for text in texts_value:
        letter_typed_correctly = True
        texts[texts_value.index(text)].tag_delete('Typed')
        if user_input.get() + '\n' == text:
            # Adds the score
            score += 1

            typed_word = texts[texts_value.index(text)]
            # Removing the text and its value from the lists to make sure the lists don't have infinite length
            texts.remove(typed_word)
            texts_value.remove(typed_word.get(1.0, tk.END))

            # Destroys the label that the user typed after the user presses enter
            typed_word.destroy()

            # Now that word is gone, so there is one less word left for the user to type
            words_left -= 1
            user_typing_input.delete(0, tk.END)
        else:
            # Checks if what the user types matches any of the word currently moving on the screen
            for letter_index in range(len(user_input.get())):
                try:
                    # If the letters don't match then don't turn it green
                    if user_input.get()[letter_index] != text[letter_index]:
                        letter_typed_correctly = False
                # If what the user types has more letters than any of the words on the screen, don't turn it green
                except IndexError:
                    letter_typed_correctly = False
            # If there is no errors from above, turn the word that didn't have any errors green
            if letter_typed_correctly:
                words_being_typed += 1
                texts[texts_value.index(text)].tag_add('Typed', 1.0, 1.0 + len(user_input.get())/10)
                texts[texts_value.index(text)].tag_config('Typed', foreground='green')

    # Deletes the letter typed if it does not match any letters currently on the screen
    # Only happens when there are still words on the screen and the user entry box is not blank
    if words_being_typed == 0 and len(texts) > 0 and user_input.get() != '':
        result.set('Word not on window')
        the_result.configure(bg='red')
        user_typing_input.delete(len(user_input.get()) - 1, tk.END)
        change_letter_colour("<Key>")


# ===========MAIN===============
main_window = tk.Tk()
main_window.geometry('1000x600+0+0')
BACKGROUND_COLOUR = 'khaki'
main_window.configure(bg=BACKGROUND_COLOUR)
main_window.title('Typing test')

enemy_image = tk.PhotoImage(file='cat_300.png')

menu()

main_window.mainloop()
