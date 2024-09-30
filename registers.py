import tkinter as tk
import time
from tkinter import messagebox  # For error messages
from vars import r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start
from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

def create_button2_window(menu_window):

    button2_window = tk.Toplevel(menu_window)
    button2_window.title("Button 1 Window")
    button2_window.attributes('-fullscreen', True)
    button2_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button2_window.attributes("-alpha", i / 100)
        button2_window.update()
        time.sleep(0.02)

    # Function to validate and append values to r1, r2, r3, r4 and update display
    def append_values():
        valid_hex_digits = '0123456789ABCDEF'  # Valid hex digits
        for i, input_field in enumerate(inputs):
            value = str(input_field.get()).upper()  # Convert input to uppercase
            if value:  # Only append if input is not empty
                if value in valid_hex_digits:  # Check if it's a valid hex digit
                    # Convert A-F to 10-15
                    if value in 'ABCDEF':
                        value = str(10 + ord(value) - ord('A'))  # Convert to 10-15
                    rows[i][1] = value  # Append to register
                    input_field.delete(0, tk.END)  # Clear the input field
                else:
                    messagebox.showerror("Invalid Input", f"'{value}' is not a valid hex digit (0-9, A-F)")
        update_display()

    # Function to update the display labels for current values of r1, r2, r3, r4
    def update_display():
        for i, label in enumerate(value_labels):
            label.config(text="                                   ".join(rows[i]))  # Join the values and update the label

    # Get screen width and height
    screen_width = button2_window.winfo_screenwidth()
    screen_height = button2_window.winfo_screenheight()

    # Define the rows (r1, r2, r3, r4) and inputs list
    rows = [r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start]
    inputs = []
    value_labels = []

    # Create the headers
    tk.Label(button2_window, text="Καταχωρητής", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//2 - 410, y=150)
    tk.Label(button2_window, text="Τιμή", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//2 - 160, y=150)
    tk.Label(button2_window, text="Κωδικός Αναφοράς   Περιεχόμενο", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//2 + 50, y=150)

    # Create labels, input fields, and current value displays for r1, r2, r3, r4
    for i, row in enumerate(["r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7"]):
        # Label for the row name (Καταχωρητές)
        tk.Label(button2_window, text=row, font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//2 - 350, y=200 + i*60)

        # Entry field for user input (Τιμές)
        input_field = tk.Entry(button2_window, font=("Arial", 14))
        input_field.place(x=screen_width//2 - 200, y=200 + i*60, width=150, height=30)
        inputs.append(input_field)

        # Label to display current values (Κωδικός Αναφοράς - Περιεχόμενο)
        current_values_label = tk.Label(button2_window, text="                                   ".join(rows[i]), font=("Arial", 14), fg="white", bg="#2E2E2E")
        current_values_label.place(x=screen_width//2 + 150, y=200 + i*60)
        value_labels.append(current_values_label)


    # Calculate center positions for the buttons
    button_width = 200
    button_height = 40
    center_x = (screen_width // 2) - (button_width // 2)
    center_y = (screen_height // 2) + 200

    # Button to append values
    append_button = tk.Button(button2_window, text="Καταχώρηση Τιμών", font=("Arial", 14), fg="white", bg="#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_values)
    append_button.place(x=center_x, y=center_y, width=button_width, height=button_height)
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    # Exit button centered below the append button
    exit_button = tk.Button(button2_window, text="Έξοδος", font=("Arial", 14), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", command=lambda: show_root(menu_window, button2_window))
    exit_button.place(x=center_x, y=center_y + 50, width=button_width, height=button_height)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    def show_root(root, top):
        # Withdraw the toplevel window smoothly
        for i in range(100, -1, -10):
            top.attributes("-alpha", i / 100)
            top.update()
            time.sleep(0.02)
        top.withdraw()  # Hide the toplevel window
        
        # Show the root window smoothly
        root.deiconify()
        for i in range(0, 101, 10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)

    button2_window.mainloop()