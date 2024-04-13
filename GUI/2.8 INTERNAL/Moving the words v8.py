"""
If the user enters letters that does not match any of the words currently on the screen, removing that letter from the
Entry box.
This version did not have that feature functioning well because after the not matching letter is removed from the Entry
box, the whole word in the Entry box got registered as not matching and the whole word turned back to black, even if the
beginning letters match one of the words on the screen.
"""


import tkinter as tk
import random

# ===========VARIABLES===============
ENGLISH_WORDS_LEVEL_1 = open("English words 1").readlines()
word_index = 0
score = 0
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
words_left = 0
texts = []
texts_value = []
typed_correctly = False
words_being_typed = 0
# ==========FUNCTIONS=============


def start_game(event):
    global words_left
    start_game_button.configure(state=tk.DISABLED)
    main_window.unbind("<Return>")
    user_typing_input.configure(state=tk.NORMAL)
    user_typing_input.focus_set()
    result.set('Type the words on the window')

    # Set the amount of words left for the user to type, if there are none then the game ends
    words_left = len(ENGLISH_WORDS_LEVEL_1)
    print_word()


def print_word():
    """
    Creates the label at index
    :return: Prints the word at the current i
    """
    global word_index, score, texts, texts_value

    # Creates a new label
    words_printed = tk.Text(main_window, width=len(ENGLISH_WORDS_LEVEL_1[word_index].strip()) + 1, height=1, relief=tk.FLAT)
    words_printed.insert(tk.INSERT, ENGLISH_WORDS_LEVEL_1[word_index].strip())
    words_printed.config(font=['Helvetica', '20', 'bold'], state=tk.DISABLED)

    # Places the label on the left of the window, at a random height.
    words_printed.place(x=WINDOW_WIDTH, y=random.randint(35, WINDOW_HEIGHT - 35))

    # Update the window so that the labels are placed
    main_window.update()

    # Store the label to a list of labels that is used in the move_word function
    texts.append(words_printed)

    # Store the text of the labels inside a list, which is used in check_user_typing and change_letter_colour function
    texts_value.append(words_printed.get(1.0, tk.END))
    move_word(words_printed)

    # If there are still words left, create another label with the next word on it
    if word_index < len(ENGLISH_WORDS_LEVEL_1) - 1:
        word_index += 1
        main_window.after(1000, print_word)


def move_word(text):
    """
    This use the index passed through at the parameter to pick out the targeted label, and moves it
    """
    global word_index, score, texts, texts_value, words_left
    # Only get the coordinates of the label if the label still exists
    if text in texts:
        x = text.winfo_x()
        y = text.winfo_y()
    # Only move the label to the left if the label is still on the screen
        if x > 0:
            text.place(x=x - 2, y=y)
            main_window.after(10, lambda: move_word(text))
    # If the label is not on the screen anymore, destroy the label
        else:
            texts.remove(text)
            texts_value.remove(text.get(1.0, tk.END))
            text.place_forget()
            words_left -= 1

    # Ends the game if there are no words left
    if words_left == 0:
        user_typing_input.delete(0, tk.END)

        # Return the start game button back to normal for the user to restart the game
        start_game_button.configure(state=tk.NORMAL)
        main_window.bind("<Return>", start_game)

        # Disable the entry box until the user starts the game, prints the score
        # Resets the score and indexes to prepare for the next game
        user_typing_input.configure(state=tk.DISABLED)
        result.set("Score: {}/{}\n Retry?".format(score, len(ENGLISH_WORDS_LEVEL_1)))
        score = 0
        word_index = 0


def change_letter_colour(user_typed, write, changing_colour):
    global score, texts, texts_value, words_left, typed_correctly, words_being_typed
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
    if words_being_typed == 0:
        user_typing_input.delete(len(user_input.get()) - 1, tk.END)


# ===========MAIN===============
main_window = tk.Tk()
main_window.geometry('1000x600+0+0')

result = tk.StringVar(main_window)
the_result = tk.Label(main_window, textvariable=result, font='Sans''12')

user_input = tk.StringVar(main_window)
user_input.trace_add('write', change_letter_colour)
user_typing_input = tk.Entry(main_window, width=10, state=tk.DISABLED, textvariable=user_input, font='Times''10')

start_game_button = tk.Button(main_window, text='Start', font='Times''12', command=lambda: start_game("<Return>"))
main_window.bind("<Return>", start_game)


user_typing_input.pack(side=tk.LEFT)
start_game_button.pack(side=tk.TOP)
the_result.pack(side=tk.BOTTOM)

main_window.mainloop()
