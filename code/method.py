# This file is responsible for the window of choosing a method for resolving hazards

import tkinter as tk, time

from tkinter import messagebox

from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

# Define choose as a global variable
choose = 0
choose_bre = 0
start_over_method = 0

def create_button4_window(menu_window, screen_width, screen_height):

    # Function to handle selection
    def select_option():
        global choose, start_over_method
        try:
            user_input = int(input_field.get())
            if user_input in (1, 2, 3, 4):
                choose = user_input  # Update the global choose variable
                start_over_method += 1
                messagebox.showinfo("You chose method", f"{choose}")
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error!", "Please, choose only (1, 2, 3, or 4)")

    # Function to handle selection
    def select_option_bre():
        global choose_bre, start_over_method
        try:
            user_input = int(bre_choice_entry.get())
            if user_input in (1, 2):
                choose_bre = user_input  # Update the global choose variable
                start_over_method += 1
                messagebox.showinfo("You chose method", f"{choose_bre}")
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error!", "Please, choose only (1 or 2)")

    # Open a new Toplevel window
    button4_window = tk.Toplevel(menu_window)
    button4_window.attributes("-fullscreen", True)
    button4_window.configure(bg="#2E2E2E")

    # Scaling factor based on screen width
    font_scale = screen_width / 1920

    # Main frame to center all elements
    main_frame = tk.Frame(button4_window, bg="#2E2E2E")
    main_frame.pack(expand=True)

    # Labels for options with scaled font size
    labels_text = ["No Operation (NOP) - 1", "Pipeline Stages Lock - 2", "Bypassing with NOP - 3", "Bypassing with stages lock - 4"]
    for text in labels_text:
        label = tk.Label(main_frame, text=text, font=("Arial", int(20 * font_scale)), bg="#2E2E2E", fg="white")
        label.pack(anchor="center", pady=5)

    # Input frame for user selection
    input_frame = tk.Frame(main_frame, bg="#2E2E2E")
    input_frame.pack(anchor="center", pady=screen_height / 108)

    input_label = tk.Label(input_frame, text="Choose (1, 2, 3, or 4):", font=("Arial", int(18 * font_scale)), bg="#2E2E2E", fg="white")
    input_label.pack(side="left", padx=screen_height / 216)

    input_field = tk.Entry(input_frame, font=("Arial", int(16 * font_scale)))
    input_field.pack(side="right", padx=screen_height / 216)

    # Button frame for selection and exit buttons, placed below the input frame
    button_frame = tk.Frame(main_frame, bg="#2E2E2E")
    button_frame.pack(anchor="center", pady=screen_height / 108)

    select_button = tk.Button(button_frame, text="Choose", font=("Arial", int(18 * font_scale)), fg="black", bg="#61afef", activebackground="#4fa3e2", activeforeground="white", command=select_option)
    select_button.pack(side="left", padx=screen_height / 108)
    select_button.bind("<Enter>", on_enter)
    select_button.bind("<Leave>", on_leave)

    # Add a new frame for BRE options below the buttons
    new_frame = tk.Frame(main_frame)
    new_frame.pack(pady=screen_height/36)
    new_frame.configure(bg="#2E2E2E")

    # Labels for BRE options
    bre_label1 = tk.Label(
        new_frame,
        text="Branch (BRE) with stages lock - 1",
        font=("Arial", int(20 * font_scale)),
        bg="#2E2E2E", fg="white"
    )
    bre_label1.pack(pady=5)

    bre_label2 = tk.Label(
        new_frame,
        text="Branch (BRE) with prediction - 2",
        font=("Arial", int(20 * font_scale)),
        bg="#2E2E2E", fg="white"
    )
    bre_label2.pack(pady=5)

    # Frame to hold label and entry side by side
    bre_input_frame = tk.Frame(new_frame, bg="#2E2E2E")
    bre_input_frame.pack(pady=10)

    # Label for BRE choice
    bre_input_label = tk.Label(
        bre_input_frame,
        text="Choose (1 or 2):",
        font=("Arial", int(20 * font_scale)),
        bg="#2E2E2E", fg="white"
    )
    bre_input_label.grid(row=0, column=0, padx=5)  # Place on the left

    # Entry for BRE choice
    bre_choice_entry = tk.Entry(
        bre_input_frame,
        font=("Arial", int(18 * font_scale)),
        justify="center",
    )
    bre_choice_entry.grid(row=0, column=1, padx=5)  # Place on the right

    # Frame to hold the buttons side by side
    bre_buttons_frame = tk.Frame(new_frame)
    bre_buttons_frame.pack(pady=10)
    bre_buttons_frame.configure(bg="#2E2E2E")

    # BRE Select Button
    bre_select_button = tk.Button(
        bre_buttons_frame,
        text="Choose",
        font=("Arial", int(18 * font_scale)),
        fg="black",
        bg="#61afef",
        activebackground="#4fa3e2",
        activeforeground="white",
        command=select_option_bre
    )
    bre_select_button.grid(row=0, column=0, padx=5)  # Place on the left

    bre_select_button.bind("<Enter>", on_enter)
    bre_select_button.bind("<Leave>", on_leave)

    # BRE Exit Button
    bre_exit_button = tk.Button(
        bre_buttons_frame,
        text="Exit",
        font=("Arial", int(18 * font_scale)),
        bg="#ff6666",
        fg="black",
        activebackground="#cc0000",
        activeforeground="white",
        command=lambda: close_button4_open_menu()
    )
    bre_exit_button.grid(row=0, column=1, padx=5)  # Place on the right

    bre_exit_button.bind("<Enter>", on_enter_exit)
    bre_exit_button.bind("<Leave>", on_leave_exit)



    def close_button4_open_menu(event=None):
        """
        Close the current button1_window and show the menu_window.
        Triggered by pressing the "Esc" key.
        """
        # button1_window.destroy()  # Close the current window
        # menu_window.deiconify()  # Show the menu window
        show_root(menu_window, button4_window)

    exit_button = tk.Button(button_frame, text="Exit", font=("Arial", int(18 * font_scale)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white", command=lambda: close_button4_open_menu())
    exit_button.pack(side="right", padx=screen_height / 108)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    # Bind the "Esc" key to close the current window and open the menu window
    button4_window.bind("<Escape>", close_button4_open_menu)

    # Smooth transition back to main menu
    def show_root(menu_window, top):
        # Withdraw the toplevel window smoothly
        for i in range(100, -1, -10):
            top.attributes("-alpha", i / 100)
            top.update()
            time.sleep(0.02)
        top.withdraw()

        # Show the main menu window smoothly
        menu_window.deiconify()
        for i in range(0, 101, 10):
            menu_window.attributes("-alpha", i / 100)
            menu_window.update()
            time.sleep(0.02)

    button4_window.mainloop()