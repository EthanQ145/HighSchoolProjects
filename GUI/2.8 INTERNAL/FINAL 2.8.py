"""21st May 2021, Final version.

By Ethan Q. Inspired by Typing Shark.
"""
import tkinter as tk
import random
import time
# ===========VARIABLES===============
try:
    ENGLISH_WORDS_LEVEL_1 = open("English words 1").readlines()
    ENGLISH_WORDS_LEVEL_2 = open("English words 2").readlines()
    correct_format = True
except UnicodeDecodeError:
    ENGLISH_WORDS_LEVEL_1 = ''
    ENGLISH_WORDS_LEVEL_2 = ''
WIDTH = 1000
HEIGHT = 600
BACKGROUND = 'khaki'
TITLE = 'DodgerBlue2'
BUTTON = 'pink'
STATS = 'lawn green'
TITLE_FONT = ['Times', '50', 'bold']
START_FONT = ['Helvetica', '25', 'bold']
BUTTON_FONT = ['Helvetica', '17']
STATS_FONT = ['Sans', '18']
# For moving the words
WORDS_BORDER = round(HEIGHT/4)
DISTANCE_BETWEEN_WORDS = 50
# Global variables
text_index = 0
texts = []
# For the timings of printing the words
previous_y = 0
loop_delay = 0
# For pause
pause = False
pause_time = 0
# For checking and statistics
recheck = False
letters_typed = 0
letters_wrong = 0
starting_time = 0
words_being_typed = 0
# Level variables
TOTAL_LIVES = 5
lives = 0
level = 0
# Level 1
WORD_TYPES_LEVEL_1 = [ENGLISH_WORDS_LEVEL_1]
TOTAL_WORDS_LEVEL_1 = 10
SPEED_LEVEL_1 = 1.1
WORD_DELAY_LEVEL_1 = 1.1
# Level 2
WORD_TYPES_LEVEL_2 = [ENGLISH_WORDS_LEVEL_1, ENGLISH_WORDS_LEVEL_2]
TOTAL_WORDS_LEVEL_2 = 10
SPEED_LEVEL_2 = 1.3
WORD_DELAY_LEVEL_2 = 1
# Level 3
WORD_TYPES_LEVEL_3 = [ENGLISH_WORDS_LEVEL_2]
TOTAL_WORDS_LEVEL_3 = 15
SPEED_LEVEL_3 = 1.5
WORD_DELAY_LEVEL_3 = 1
# Level 4
WORD_TYPES_LEVEL_4 = [ENGLISH_WORDS_LEVEL_2]
TOTAL_WORDS_LEVEL_4 = 20
SPEED_LEVEL_4 = 1.5
WORD_DELAY_LEVEL_4 = 0.75
# Level 5
WORDS_TYPE_LEVEL_5 = [ENGLISH_WORDS_LEVEL_2]
TOTAL_WORDS_LEVEL_5 = 25
SPEED_LEVEL_5 = 2
WORD_DELAY_LEVEL_5 = 0.75
# ALL LEVELS
WORD_TYPES = [WORD_TYPES_LEVEL_1, WORD_TYPES_LEVEL_2, WORD_TYPES_LEVEL_3,
              WORD_TYPES_LEVEL_4, WORDS_TYPE_LEVEL_5]
TOTAL_WORDS = [TOTAL_WORDS_LEVEL_1, TOTAL_WORDS_LEVEL_2, TOTAL_WORDS_LEVEL_3,
               TOTAL_WORDS_LEVEL_4, TOTAL_WORDS_LEVEL_5]
SPEEDS = [SPEED_LEVEL_1, SPEED_LEVEL_2, SPEED_LEVEL_3, SPEED_LEVEL_4,
          SPEED_LEVEL_5]
WORD_DELAYS = [WORD_DELAY_LEVEL_1, WORD_DELAY_LEVEL_2, WORD_DELAY_LEVEL_3,
               WORD_DELAY_LEVEL_4, WORD_DELAY_LEVEL_5]
LAST_DIFFICULTY = len(WORD_TYPES)
# ==========FUNCTIONS=============


def clear_screen():
    """Hides all the available screens for the wanted screen to be shown."""
    menu_frame.pack_forget()
    help_frame.pack_forget()
    game_frame.pack_forget()
    progress_frame.pack_forget()


def reset():
    """Reset all variables. Used at the start of each level."""
    global texts, text_index, letters_wrong, letters_typed
    # Reset variables
    user_input.delete(0, tk.END)
    for text in range(len(texts)):
        texts[text].destroy()
    texts = []
    text_index = 0
    letters_wrong = 0
    letters_typed = 0


def pause_screen():
    """Prepare variables and show pause screen."""
    global pause
    user_input.configure(state=tk.DISABLED)
    pause = True
    end_result.set('PAUSE')
    end_info.set('Press Enter or click Resume button to resume')
    continue_button.configure(text='Resume', state=tk.NORMAL)
    progress_screen()
    window.bind("<Return>", lambda event: start_game())


def menu():
    """Prepare variables and show menu screen."""
    global level, lives, pause
    level = 0
    lives = TOTAL_LIVES
    pause = False
    clear_screen()
    reset()
    menu_frame.pack()
    menu_frame.pack_propagate(False)
    window.bind("<Return>", lambda event: help_screen())


def help_screen():
    """Show instruction screen."""
    clear_screen()
    help_frame.pack()
    help_frame.pack_propagate(False)
    window.bind("<Return>", lambda event: start_game())


def game_screen():
    """Set up test and show typing screen."""
    # Disable the start button while the game is playing
    window.unbind("<Return>")
    clear_screen()
    game_frame.pack()
    game_frame.pack_propagate(False)


def progress_screen():
    """Show results, also used for pause."""
    clear_screen()
    progress_frame.pack()
    progress_frame.pack_propagate(False)


def set_difficulty(difficulty):
    """Set variables for the given difficulty.

    Arg: The given difficulty level.
    Return: The level's amount, type of words; speed; and time between words.
    """
    level_total_words = TOTAL_WORDS[difficulty]
    words = WORD_TYPES[difficulty]
    speed = SPEEDS[difficulty]
    word_delay = WORD_DELAYS[difficulty]
    return level_total_words, words, speed, word_delay


def start_game():
    """Prepare variables and start test."""
    global starting_time, pause
    user_input.configure(state=tk.NORMAL)
    # Start timer
    if pause:
        starting_time += time.time() - pause_time
    else:
        starting_time = time.time()
        user_input.delete(0, tk.END)
        game_instruction.set('Type the words on window')
        game_instructions.configure(bg='light green')
    pause = False
    game_screen()
    window.bind('<Key>', lambda event: check_typing())
    window.bind('<Escape>', lambda event: pause_screen())
    # Set amount of lives
    lives_info.set('Lives: {}'.format(lives))
    # Put cursor on Entry box
    user_input.focus()
    game_instruction.set('Type the words on window')
    stats.set('Level: {}\nTime: 0s\nAccuracy: 0%\nWPM: 0'.format(level + 1))
    set_difficulty(level)
    program_loop()


def end_game():
    """Reset variables, show results and modify difficulty."""
    global level
    window.unbind("<Key>")
    window.unbind("<Escape>")
    game_frame.pack_forget()
    reset()
    continue_button.configure(text="Continue to next level")
    progress_screen()
    if lives != 0:
        if level < LAST_DIFFICULTY - 1:
            # Open progress screen if there are more levels
            level += 1
            continue_button.configure(state=tk.NORMAL)
            end_result.set('COMPLETE')
            end_info.set('Great typing!')
            window.bind("<Return>", lambda event: start_game())
        else:
            end_result.set('THE END')
            end_info.set('Thank you for using my typing test')
            continue_button.configure(state=tk.DISABLED)
    else:
        end_result.set('GAME OVER')
        end_info.set('Retry?')
        continue_button.configure(state=tk.DISABLED)
    reset()


def program_loop():
    """Control statistics, test state, movement and printing of words."""
    global loop_delay, words_being_typed, lives, pause_time
    if lives == 0:
        loop_delay = 0
        end_game()
    else:
        time_taken = time.time() - starting_time
        if letters_typed + letters_wrong != 0:
            accuracy = 100 * letters_typed/(letters_typed + letters_wrong)
            wpm = letters_typed/5/(time_taken/60)
        else:
            accuracy = 0
            wpm = 0
        stats.set('Level: {}\nTime: {}s\nAccuracy: {}%\nWPM: {}'.format(
            level + 1, round(time_taken, 2), round(accuracy, 2), round(wpm)))
        if not pause:
            # Print words
            if loop_delay <= 0 and text_index <= set_difficulty(level)[0] - 1:
                print_word()
                loop_delay = set_difficulty(level)[3] * 100
            loop_delay -= 2
            # Move the words
            if texts:
                for text in texts:
                    x = text.winfo_x()
                    y = text.winfo_y()
                    if x > -len(text.get(1.0, tk.END))*10:
                        text.place(x=x - set_difficulty(level)[2] * 2, y=y)
                    else:
                        # Clear entry box if word already gone out of window
                        if text.tag_names() == ('sel', 'Typed'):
                            words_being_typed -= 1
                            if words_being_typed == 0:
                                user_input.delete(0, tk.END)
                        texts.remove(text)
                        text.destroy()
                        # Removes 1 live
                        lives -= 1
                        lives_info.set('Lives: {}'.format(lives))
                window.after(20, program_loop)
            else:
                # Print word if there's no word on screen
                if text_index <= set_difficulty(level)[0] - 1:
                    loop_delay = set_difficulty(level)[3] * 100
                    print_word()
                    window.after(20, program_loop)
                else:
                    loop_delay = 0
                    end_game()
        else:
            pause_time = time.time()


def print_word():
    """Print words and update information on current words on window."""
    global text_index, texts, previous_y
    # Choose a word to be moved out
    word_list = random.choice(set_difficulty(level)[1])
    word = random.choice(word_list).strip()
    words_printed = tk.Text(game_frame, width=len(word) + 2, height=1,
                            font=['Helvetica', '20', 'bold'], relief=tk.FLAT,
                            bg=BACKGROUND)
    words_printed.insert(tk.INSERT, word)
    words_printed.config(state=tk.DISABLED)
    # Place text on left of window, at a random height not overlapping others
    current_y = random.randint(WORDS_BORDER, HEIGHT - WORDS_BORDER)
    while current_y in range(previous_y - DISTANCE_BETWEEN_WORDS,
                             previous_y + DISTANCE_BETWEEN_WORDS):
        current_y = random.randint(WORDS_BORDER, HEIGHT - WORDS_BORDER)
    words_printed.place(x=WIDTH - len(word)*10, y=current_y)
    previous_y = current_y
    # Update the window so placement updates
    window.update()
    # Store updated location and text info to list
    texts.append(words_printed)
    text_index += 1


def check_typing():
    """Check user's typing and add data to variables for statistics."""
    global texts, words_being_typed, letters_wrong, letters_typed, recheck
    if words_being_typed > 0 or not recheck:
        game_instruction.set('Type the words on window')
        game_instructions.configure(bg='light green')
    words_being_typed = 0
    for text in texts:
        text.tag_delete('Typed')
        if user_input.get() == text.get(1.0, 'end-1c'):
            # Remove the word
            texts.remove(text)
            text.destroy()
            # Update variables and clear Entry box
            letters_typed += len(user_input.get())
            user_input.delete(0, tk.END)
            for word in texts:
                word.tag_delete('Typed')
        else:
            if user_input.get() != '':
                typed_correctly = True
                # Loop through each letter of each word
                for letter in range(len(user_input.get())):
                    try:
                        # Wrong if letter doesn't match
                        if user_input.get()[letter] != \
                                text.get(1.0, 'end-1c')[letter]:
                            typed_correctly = False
                    # Wrong if length of input higher than word
                    except IndexError:
                        typed_correctly = False
                # Turn matching letters to green
                if typed_correctly:
                    words_being_typed += 1
                    text.tag_add('Typed', 1.0, 1.0 + len(user_input.get())/10)
                    text.tag_config('Typed', foreground='green')
            recheck = False
    # If letter typed doesn't match, delete it
    if words_being_typed == 0 and user_input.get() != '':
        letters_wrong += 1
        game_instruction.set('Word not on window')
        game_instructions.configure(bg='red')
        user_input.delete(len(user_input.get()) - 1, tk.END)
        recheck = True
        check_typing()


# ===========MAIN===============
window = tk.Tk()
window.geometry('{}x{}+0+0'.format(WIDTH, HEIGHT))
# MENU SCREEN
menu_frame = tk.Frame(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
name = tk.Label(menu_frame, text='TYPING TEST', font=TITLE_FONT, bg=TITLE)
start_game_button = tk.Button(menu_frame, text='START', command=help_screen,
                              font=START_FONT, bg=BUTTON)
menu_instruction = tk.StringVar()
menu_instructions = tk.Label(menu_frame, textvariable=menu_instruction,
                             font=STATS_FONT, width=50, bg='light green')
menu_instruction.set('Click START button or press Enter to start the test')
name.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
start_game_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
menu_instructions.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
# INSTRUCTION_SCREEN
help_frame = tk.Frame(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
title = tk.Label(help_frame, text='INSTRUCTION', bg=BACKGROUND, fg='red',
                 font=TITLE_FONT)
tutorial = tk.StringVar()
tutorial_label = tk.Label(help_frame, textvariable=tutorial, fg='green',
                          font=STATS_FONT, bg=BACKGROUND)
tutorial.set('Type all moving words on the window\n'
             'Non-matching typed letters will be deleted automatically\n'
             'This will decrease accuracy\nYou can press Escape to Pause\n\n'
             'There are {} levels, have fun!'.format(LAST_DIFFICULTY))
begin_test = tk.Button(help_frame, text='BEGIN', bg=BUTTON,
                       font=START_FONT, command=start_game)
title.place(relx=0.5, rely=0.1, anchor=tk.N)
tutorial_label.place(relx=0.5, rely=0.3, anchor=tk.N)
begin_test.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
# GAME SCREEN
game_frame = tk.Frame(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
game_instruction = tk.StringVar()
game_instructions = tk.Label(game_frame, textvariable=game_instruction,
                             font=STATS_FONT, width=50, bg='light green')
stats = tk.StringVar()
statistics_label = tk.Label(game_frame, textvariable=stats, bg=STATS,
                            font=STATS_FONT, width=WIDTH)
lives_info = tk.StringVar()
lives_label = tk.Label(game_frame, textvariable=lives_info, bg='light blue',
                       fg='red', font=['Sans', '25'])
user_input = tk.Entry(game_frame, width=10, font=['Times', '22', 'bold'])
user_input.place(relx=0.5, rely=0.88, anchor=tk.S)
statistics_label.place(relx=0.5, rely=0, anchor=tk.N)
lives_label.place(relx=0.1, rely=0)
game_instructions.place(relx=0.5, rely=0.9, anchor=tk.N)
# PROGRESS SCREEN
progress_frame = tk.Frame(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
end_result = tk.StringVar()
results_label = tk.Label(progress_frame, textvariable=end_result, bg=TITLE,
                         font=TITLE_FONT)
end_info = tk.StringVar()
end_info_label = tk.Label(progress_frame, textvariable=end_info, bg='black',
                          font=['Helvetica', '22', 'bold'], fg='white')
end_stats = tk.Label(progress_frame, textvariable=stats, bg=STATS,
                     font=STATS_FONT)
leave = tk.Button(progress_frame, font=BUTTON_FONT, bg=BUTTON, command=menu,
                  text='Return to Menu\nProgress will reset')
continue_button = tk.Button(progress_frame, text="Continue to next level",
                            font=BUTTON_FONT, bg=BUTTON, command=start_game)
lives_left = tk.Label(progress_frame, textvariable=lives_info, fg='red',
                      font=['Sans', '25'], bg='light blue')
results_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
end_info_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
end_stats.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
leave.place(relx=0.2, rely=0.9, anchor=tk.CENTER)
continue_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)
lives_left.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
if ENGLISH_WORDS_LEVEL_1 != '' and ENGLISH_WORDS_LEVEL_2 != '':
    menu()
else:
    print('Invalid file format.\n Please use text files.')
window.mainloop()
