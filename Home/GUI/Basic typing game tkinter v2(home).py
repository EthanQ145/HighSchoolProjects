import tkinter as tk
import random
# ===========VARIABLES===============
ENGLISH_WORDS_LEVEL_1 = open("test text file").readlines()
scrambled_words = random.sample(ENGLISH_WORDS_LEVEL_1, len(ENGLISH_WORDS_LEVEL_1))
index = 0
score = 0
entry_hidden = True
# ==========FUNCTIONS=============


def end_game():
    """
    Ends the game and resets the variables and widgets
    :return: None
    """
    global score, scrambled_words, index, score, user_typing_input
    english_words_output_text.config(state='normal')
    english_words_output_text.delete('1.0', tk.END)
    english_words_output_text.insert(tk.INSERT, "Score: {}".format(score))
    english_words_output_text.config(state='disabled')
    scrambled_words = random.sample(ENGLISH_WORDS_LEVEL_1, len(ENGLISH_WORDS_LEVEL_1))
    # Resetting the score and the game
    index = 0
    score = 0
    user_typing_input.configure(state=tk.DISABLED)
    main_window.unbind("<Key>")
    main_window.unbind("<Return>")
    main_window.unbind("<BackSpace>")
    start_typing_game_button.configure(text="Retry?", command=lambda: start_game(scrambled_words))


def start_game(words_list):
    """
    Enables the entry box and prints a word for the user to type in the entry box
    :param words_list: The entire words list that would be printed index to index.
    :return: None
    """
    global index
    print(index, words_list)
    main_window.bind("<Key>", user_typing)
    main_window.bind("<BackSpace>", user_typing)
    main_window.bind("<Return>", check_user_typing)
    user_typing_input.configure(state=tk.NORMAL)
    english_words_output_text.config(state='normal')
    english_words_output_text.delete('1.0', tk.END)
    english_words_output_text.insert('1.0', words_list[index].split())
    english_words_output_text.config(state='disabled')


def user_typing(event):
    global index, scrambled_words
    user_input = user_typing_input.get()
    current_word = scrambled_words[index].strip()
    current_word_as_list = list(current_word.strip())
    for letter_index in range(len(list(user_input))):
        print(user_input, len(user_input))
        english_words_output_text.config(state='normal')
        english_words_output_text.tag_remove('Correctly typed', str(1 + letter_index / 10), tk.END)
        english_words_output_text.tag_remove('Wrongly typed', str(1 + letter_index / 10), tk.END)
        # If no words is on the entry box, the printed word remains the colour black
        if len(list(user_input)) == 0:
            english_words_output_text.config(fg='black')
        try:
            # If the word is correct, add that index to the tag Correctly typed
            if user_input[letter_index] == current_word_as_list[letter_index]:
                english_words_output_text.tag_add('Correctly typed', str(1 + letter_index / 10),
                                                  str(1 + (letter_index + 1) / 10))
            # If the word is wrong, add that index to the tag Wrongly typed
            else:
                english_words_output_text.tag_add('Wrongly typed', str(1 + letter_index / 10),
                                                  str(1 + (letter_index + 1) / 10))
            # Change Correctly typed into green font, change Wrongly typed into red font
            english_words_output_text.tag_config('Correctly typed', foreground="green")
            english_words_output_text.tag_config('Wrongly typed', foreground="red")
        except IndexError:
            print('Reached end of index')
            pass
        english_words_output_text.config(state='disabled')


def check_user_typing(event):
    """
    Check if what the user typed is correct or not.
    :param event: Starts when the user presses Enter
    :return: add points when the user types correctly
    """
    global index, scrambled_words, score
    user_input = user_typing_input.get()
    if user_input.strip() == scrambled_words[index].strip():
        score += 1
    user_typing_input.delete(0, tk.END)
    index += 1
    if index <= len(scrambled_words)-1:
        start_game(scrambled_words)
    else:
        end_game()


# ===========MAIN===============
main_window = tk.Tk()

english_words_output_text = tk.Text(main_window)
english_words_output_text.insert(tk.INSERT, "Click the Start button to start the game")
english_words_output_text.config(state='disabled')
user_typing_input = tk.Entry(main_window, width=10, state=tk.DISABLED)
start_typing_game_button = tk.Button(main_window, text="Start",
                                     command=lambda: start_game(scrambled_words))
english_words_output_text.grid(row=0, column=0)
user_typing_input.grid(row=1, column=0)
start_typing_game_button.grid(row=3, column=0)


# =============BINDINGS===========
main_window.mainloop()
