import tkinter as tk
import time, cycles
from tkinter import messagebox  # For error messages
from vars import (r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start, r8_start, r9_start, r10_start, r11_start, r12_start, r13_start, r14_start, r15_start)
from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

def create_button2_window(menu_window):

    global register_start
    button2_window = tk.Toplevel(menu_window)
    button2_window.title("Button 1 Window")
    button2_window.attributes('-fullscreen', True)
    button2_window.configure(bg='#2E2E2E')

    # Smoothly show the toplevel window
    for i in range(0, 101, 10):
        button2_window.attributes("-alpha", i / 100)
        button2_window.update()
        time.sleep(0.02)

    r0=cycles.r0
    r1=cycles.r1
    r2=cycles.r2
    r3=cycles.r3
    r4=cycles.r4
    r5=cycles.r5
    r6=cycles.r6
    r7=cycles.r7
    r8=cycles.r8
    r9=cycles.r9
    r10=cycles.r10
    r11=cycles.r11
    r12=cycles.r12
    r13=cycles.r13
    r14=cycles.r14
    r15=cycles.r15

    r = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]

    # Define the initial values for each register
    register_start = [
        r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start,
        r8_start, r9_start, r10_start, r11_start, r12_start, r13_start, r14_start, r15_start
    ]

    # Initialize register rows with starting values
    rows = [[f"r{i}", *value] for i, value in enumerate(register_start)]
    inputs = []
    value_labels = []

    # Function to validate and append values to each register and update display
    def append_values():
        valid_hex_digits = '0123456789ABCDEF'
        global register_start  # Access the global register_start

        for i, input_field in enumerate(inputs):
            value = str(input_field.get()).upper()  # Get the input value and convert it to uppercase
            if value:
                # Pad single-digit inputs with a leading zero
                if len(value) == 1 and value in valid_hex_digits:
                    value = f"0{value}"  # Convert '3' to '03'
                # Check if the input has exactly two hex digits
                if len(value) == 2 and all(char in valid_hex_digits for char in value):
                    register_start[i][1] = value  # Update the hexadecimal content in register_start
                    r[i][1] = value
                    rows[i][2] = r[i][1]
                    input_field.delete(0, tk.END)  # Clear the input field
                else:
                    # Display an error if the input is invalid
                    messagebox.showerror("Invalid Input", f"'{value}' is not a valid 2-digit hex value (00-FF)")
        update_display()

    # Function to update display labels with current register values
    def update_display():
        for i, label in enumerate(value_labels):
            label.config(text=r[i][1])  # Display the stored hex value directly

    # Get screen width and height
    screen_width = button2_window.winfo_screenwidth()
    screen_height = button2_window.winfo_screenheight()

    # Font scaling based on screen width
    font_scale = screen_width / 1920

    # Create headers with scaled font sizes and positions
    tk.Label(button2_window, text="Καταχωρητής", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.02), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Κωδικός", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.135), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Τιμή", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.28), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Περιεχόμενο", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.37), y=int(screen_height * 0.15))

    tk.Label(button2_window, text="Καταχωρητής", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.475), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Κωδικός", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.59), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Τιμή", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.73), y=int(screen_height * 0.15))
    tk.Label(button2_window, text="Περιεχόμενο", font=("Arial", int(18 * font_scale)), fg="white", bg="#2E2E2E").place(x=int(screen_width * 0.82), y=int(screen_height * 0.15))

    # Create labels, input fields, and value displays in two columns of 8 rows each
    for i, row in enumerate(r):
        col_offset = 0.05 if i < 8 else 0.5  # Left column starts at 0.1, right column at 0.5
        y_position = int(screen_height * 0.2 + (i % 8) * screen_height * 0.05)

        # Register label (e.g., r0, r1)
        tk.Label(button2_window, text=row[2], font=("Arial", int(screen_width / 100)), fg="white", bg="#2E2E2E").place(x=int(screen_width * col_offset), y=y_position)

        # Reference code label (e.g., "0", "1", etc.)
        tk.Label(button2_window, text=row[0], font=("Arial", int(screen_width / 100)), fg="white", bg="#2E2E2E").place(x=int(screen_width * (col_offset + 0.1)), y=y_position)

        # Entry field for value input
        input_field = tk.Entry(button2_window, font=("Arial", int(screen_width / 120)))
        input_field.place(x=int(screen_width * (col_offset + 0.2)), y=y_position, width=int(screen_width * 0.1), height=int(screen_height * 0.05))
        inputs.append(input_field)

        # Label to display current content value
        current_values_label = tk.Label(button2_window, text=row[1], font=("Arial", int(screen_width / 100)), fg="white", bg="#2E2E2E")
        current_values_label.place(x=int(screen_width * (col_offset + 0.35)), y=y_position)
        value_labels.append(current_values_label)

    # Calculate center positions for the buttons
    button_width = int(200 * font_scale)
    button_height = int(40 * font_scale)
    center_x = screen_width * 0.45
    center_y = screen_height * 0.75

    # Button to append values
    append_button = tk.Button(button2_window, text="Καταχώρηση Τιμών", font=("Arial", int(14 * font_scale)), fg="black", bg="#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_values)
    append_button.place(x=center_x, y=center_y, width=button_width, height=button_height)
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    def close_button2_open_menu(event=None):
        """
        Close the current button1_window and show the menu_window.
        Triggered by pressing the "Esc" key.
        """
        # button1_window.destroy()  # Close the current window
        # menu_window.deiconify()  # Show the menu window
        show_root(menu_window, button2_window)

    # Exit button centered below the append button
    exit_button = tk.Button(button2_window, text="Έξοδος", font=("Arial", int(14 * font_scale)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white", command=lambda: close_button2_open_menu())
    exit_button.place(x=center_x, y=center_y + button_height + 10, width=button_width, height=button_height)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    # Bind the "Esc" key to close the current window and open the menu window
    button2_window.bind("<Escape>", close_button2_open_menu)

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

    button2_window.mainloop()