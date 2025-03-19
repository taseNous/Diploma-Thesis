# This file is responsible for the window of memory management

import tkinter as tk
import time, cycles
from tkinter import messagebox
from vars import (m0_starter, m1_starter, m2_starter, m3_starter, m4_starter, m5_starter, m6_starter, m7_starter, m8_starter, m9_starter, m10_starter, m11_starter, 
                  m12_starter, m13_starter, m14_starter, m15_starter, m16_starter, m17_starter, m18_starter, m19_starter, m20_starter, m21_starter, m22_starter, m23_starter)
from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

def create_button3_window(menu_window=None):

    global memory_start

    button3_window = tk.Toplevel(menu_window)
    button3_window.title("Button 1 Window")
    button3_window.attributes('-fullscreen', True)
    button3_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button3_window.attributes("-alpha", i / 100)
        button3_window.update()
        time.sleep(0.02)

    # Get screen width and height
    screen_width = button3_window.winfo_screenwidth()
    screen_height = button3_window.winfo_screenheight()

    # Font scaling based on screen width
    font_scale = screen_width / 1920

    m0 = cycles.m0
    m1 = cycles.m1
    m2 = cycles.m2
    m3 = cycles.m3
    m4 = cycles.m4
    m5 = cycles.m5
    m6 = cycles.m6
    m7 = cycles.m7
    m8 = cycles.m8
    m9 = cycles.m9
    m10 = cycles.m10
    m11 = cycles.m11
    m12 = cycles.m12
    m13 = cycles.m13
    m14 = cycles.m14
    m15 = cycles.m15
    m16 = cycles.m16
    m17 = cycles.m17
    m18 = cycles.m18
    m19 = cycles.m19
    m20 = cycles.m20
    m21 = cycles.m21
    m22 = cycles.m22
    m23 = cycles.m23

    m = [m0 , m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23]

    # Memory start values for each memory address
    memory_start = [
        m0_starter, m1_starter, m2_starter, m3_starter, m4_starter, m5_starter, m6_starter, m7_starter, m8_starter, m9_starter, m10_starter, m11_starter,
        m12_starter, m13_starter, m14_starter, m15_starter, m16_starter, m17_starter, m18_starter, m19_starter, m20_starter, m21_starter, m22_starter, m23_starter
    ]

    # Initialize memory with starting values
    memory = [[address, value] for address, value in memory_start]
    inputs = []
    value_labels = []

    # Function to append values to memory and update display
    def append_values():
        valid_hex_digits = '0123456789ABCDEF'
        global memory_start  # Access the global memory_start variable

        for i, input_field in enumerate(inputs):
            value = str(input_field.get()).upper()  # Get and uppercase the input value
            if value:
                # Pad single-digit inputs with a leading zero
                if len(value) == 1 and value in valid_hex_digits:
                    value = f"0{value}"  # Convert '3' to '03'
                # Check if the input has exactly two hex digits
                if len(value) == 2 and all(char in valid_hex_digits for char in value):
                    memory_start[i][1] = value  # Update the memory content in memory_start
                    m[i][1] = value
                    input_field.delete(0, tk.END)  # Clear the input field
                else:
                    # Show an error if the input is invalid
                    messagebox.showerror("Invalid Input", f"'{value}' is not a valid 2-digit hex value (00-FF)")
        update_display()

    def update_display():
        for i, label in enumerate(value_labels):
            label.config(text=m[i][1])

    # Create headers with scaled font sizes and positions
    tk.Label(button3_window, text="Memory Position", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.02), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Memory Address", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.125), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Value", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.28), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Content", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.37), y=int(screen_height * 0.05))

    tk.Label(button3_window, text="Memory Position", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.475), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Memory Address", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.575), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Value", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.73), y=int(screen_height * 0.05))
    tk.Label(button3_window, text="Content", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.82), y=int(screen_height * 0.05))

    # Create labels, input fields, and value displays in two columns of 12 rows each
    for i, row in enumerate(m):
        col_offset = 0.05 if i < 12 else 0.5  # Left column starts at 0.1, right column at 0.5
        y_position = int(screen_height * 0.1 + (i % 12) * screen_height * 0.05)

        # Label for the memory row (e.g., m0, m1)
        tk.Label(button3_window, text=row[2], font=("Arial", int(14 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * col_offset), y=y_position)

        # Label for the memory address
        tk.Label(button3_window, text=row[0], font=("Arial", int(14 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * (col_offset + 0.1)), y=y_position)

        # Entry field for user input
        input_field = tk.Entry(button3_window, font=("Arial", int(14 * font_scale)))
        input_field.place(x=int(screen_width * (col_offset + 0.2)), y=y_position, width=int(screen_width * 0.1), height=int(screen_height * 0.05))
        inputs.append(input_field)

        # Label to display the current memory content value
        current_values_label = tk.Label(button3_window, text=row[1], font=("Arial", int(14 * font_scale)), fg="white", bg="#2E2E2E")
        current_values_label.place(x=int(screen_width * (col_offset + 0.35)), y=y_position)
        value_labels.append(current_values_label)

    # Calculate center positions for the buttons
    button_width = int(200 * font_scale)
    button_height = int(40 * font_scale)
    center_x = screen_width * 0.45
    center_y = screen_height * 0.75

    # Button to append values
    append_button = tk.Button(button3_window, text="Add Values", font=("Arial", int(14 * font_scale)), fg="black", bg="#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_values)
    append_button.place(x=center_x, y=center_y, width=button_width, height=button_height)
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    def close_button3_open_menu(event=None):
        """
        Close the current button1_window and show the menu_window.
        Triggered by pressing the "Esc" key.
        """
        # button1_window.destroy()  # Close the current window
        # menu_window.deiconify()  # Show the menu window
        show_root(menu_window, button3_window)

    # Exit button centered below the append button
    exit_button = tk.Button(button3_window, text="Exit", font=("Arial", int(14 * font_scale)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white", command=lambda: close_button3_open_menu())
    exit_button.place(x=center_x, y=center_y + button_height + 10, width=button_width, height=button_height)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    # Bind the "Esc" key to close the current window and open the menu window
    button3_window.bind("<Escape>", close_button3_open_menu)

    def show_root(root, top):
        for i in range(100, -1, -10):
            top.attributes("-alpha", i / 100)
            top.update()
            time.sleep(0.02)
        top.withdraw()
        
        root.deiconify()
        for i in range(0, 101, 10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)

    button3_window.mainloop()