"""
Distance converter
Converts a distance value between metres, miles and feet depending on what the user enters.

Ethan Quach 4/3/2021
"""
import tkinter as tk
main_window = tk.Tk()

# ===========FUNCTIONS==============


def distance_converter():
    """
    Converts a distance measurement between metres, miles and feet depending on which unit the user enters.

    :return: The value of that distance in the unit of the other 2 that the user didn't enter.
    """
    # Checking for numeric data
    try:
        # If the user entered in the Feet entry box, calculate the value in metres and miles
        if feet_entry.get() != '':
            metres_entry.delete(0, tk.END)
            miles_entry.delete(0, tk.END)
            # Calculations
            metres = float(feet_entry.get()) / 3.281
            miles = float(feet_entry.get()) / 5280

            # Printing the results
            metres_entry.insert(0, metres)
            miles_entry.insert(0, miles)

        # If the user entered in the Metres entry box, calculate the value in feet and miles
        elif metres_entry.get() != '':
            feet_entry.delete(0, tk.END)
            miles_entry.delete(0, tk.END)
            # Calculations
            feet = float(metres_entry.get()) * 3.281
            miles = float(metres_entry.get()) / 1609

            # Printing the results
            feet_entry.insert(0, feet)
            miles_entry.insert(0, miles)

        # If the user entered in the Miles entry box, calculate the value in feet and metres
        elif miles_entry.get() != '':
            feet_entry.delete(0, tk.END)
            metres_entry.delete(0, tk.END)
            # Calculations
            feet = float(miles_entry.get()) * 5280
            metres = float(miles_entry.get()) * 1609

            # Printing the results
            feet_entry.insert(0, feet)
            metres_entry.insert(0, metres)

    except ValueError:
        print("Error - needs to be a number")
        clear_entry("<BackSpace>")


def clear_entry(event):
    """
    Clears all the entry for all units if the user decided to do another calculation
    :param event: If the user press backspace
    :return: Clears all entry boxes of all 3 units
    """
    feet_entry.delete(0, tk.END)
    metres_entry.delete(0, tk.END)
    miles_entry.delete(0, tk.END)


# =============MAIN=================

# User inputs
feet_entry = tk.Entry(width=30)
metres_entry = tk.Entry(width=30)
miles_entry = tk.Entry(width=30)

# Labels and buttons
feet_label = tk.Label(main_window, text='Feet')
metre_label = tk.Label(main_window, text='Metres')
miles_label = tk.Label(main_window, text='Miles')
calculate = tk.Button(main_window, text='Calculate', command=distance_converter)

# Formatting
feet_entry.grid(column=2, row=1)
metres_entry.grid(column=2, row=2)
miles_entry.grid(column=2, row=3)
feet_label.grid(column=3, row=1)
metre_label.grid(column=3, row=2)
miles_label.grid(column=3, row=3)
calculate.grid(column=3, row=4)

# Binding keys
main_window.bind("<BackSpace>", clear_entry)

# Main window loop
main_window.mainloop()
