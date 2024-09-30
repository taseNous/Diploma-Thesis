import tkinter as tk
import time
from tkinter import messagebox  # For error messages
from vars import m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16
from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

def create_button3_window(menu_window=None, show_menu_function=None, canvas=None):

    button3_window = tk.Toplevel(menu_window)
    button3_window.title("Button 1 Window")
    button3_window.attributes('-fullscreen', True)
    button3_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button3_window.attributes("-alpha", i / 100)
        button3_window.update()
        time.sleep(0.02)

    # Function to append values to r1, r2, r3, r4 and update display
    def append_values():
        valid_hex_digits = '0123456789ABCDEF'  # Valid hex digits
        for i, input_field in enumerate(inputs):
            value = str(input_field.get()).upper()  # Convert input to uppercase
            if value:  # Only append if input is not empty
                if value in valid_hex_digits:  # Check if it's a valid hex digit
                    # Convert A-F to 10-15
                    if value in 'ABCDEF':
                        value = str(10 + ord(value) - ord('A'))  # Convert to 10-15
                    memory[i][1] = value  # Append to memory (or register)
                    input_field.delete(0, tk.END)  # Clear the input field
                else:
                    messagebox.showerror("Invalid Input", f"'{value}' is not a valid hex digit (0-9, A-F)")
        update_display()


    # Function to update the display labels for current values of r1, r2, r3, r4
    def update_display():
        for i, label in enumerate(value_labels):
            label.config(text="                                        ".join(memory[i]))  # Join the values and update the label

    # Get screen width and height
    screen_width = button3_window.winfo_screenwidth()
    screen_height = button3_window.winfo_screenheight()

    memory = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16]
    inputs = []
    value_labels = []

    # Create the headers
    tk.Label(button3_window, text="Θέση Μνήμης", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//3 - 260, y=50)
    tk.Label(button3_window, text="Τιμή", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//3 + 40, y=50)
    tk.Label(button3_window, text="Διεύθυνση             Περιεχόμενο", font=("Arial", 18), fg="white", bg="#2E2E2E").place(x=screen_width//2 - 70, y=50)

    # Create labels, input fields, and current value displays for r1, r2, r3, r4
    for i, row in enumerate(["m1","m2","m3","m4","m5","m6","m7","m8","m9","m10","m11","m12","m13","m14","m15","m16"]):
        # Label for the row name
        tk.Label(button3_window, text=row, font=("Arial", 14), fg="white", bg="#2E2E2E").place(x=screen_width//3 - 210, y=100 + i*60)

        # Entry field for user input
        input_field = tk.Entry(button3_window, font=("Arial", 14))
        input_field.place(x=screen_width//3, y=100 + i*60, width=150, height=30)
        inputs.append(input_field)

        # Label to display current values
        current_values_label = tk.Label(button3_window, text="                                        ".join(memory[i]), font=("Arial", 14), fg="white", bg="#2E2E2E")
        current_values_label.place(x=screen_width//2 - 20, y=100 + i*60)
        value_labels.append(current_values_label)

    # Calculate center positions for the buttons
    button_width = 200
    button_height = 40
    center_x = (screen_width // 2) + (button_width // 2)
    center_y = (screen_height // 2)

    # Button to append values
    append_button = tk.Button(button3_window, text="Καταχώρηση Τιμών", font=("Arial", 14), fg="white", bg="#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_values)
    append_button.place(x=center_x + 250, y=center_y, width=button_width, height=button_height)
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    # Exit button centered below the append button
    exit_button = tk.Button(button3_window, text="Έξοδος", font=("Arial", 14), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", command=lambda: show_root(menu_window, button3_window))
    exit_button.place(x=center_x + 250, y=center_y + 50, width=button_width, height=button_height)
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

    button3_window.mainloop()