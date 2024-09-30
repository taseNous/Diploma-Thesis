import tkinter as tk
import time
from vars import choose  # Assuming 'choose' is defined in another module

from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit

def create_button4_window(menu_window=None, show_menu_function=None, canvas=None):

    button4_window = tk.Toplevel(menu_window)
    button4_window.title("Button 4 Window")
    button4_window.attributes('-fullscreen', True)
    button4_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button4_window.attributes("-alpha", i / 100)
        button4_window.update()
        time.sleep(0.02)

    # Get screen width and height
    screen_width = button4_window.winfo_screenwidth()
    screen_height = button4_window.winfo_screenheight()

    # Radio button logic: only one selection allowed
    radio_var = tk.IntVar(value=0)  # Default selection set to No Operation (0)

    def choose_nop():
        global choose
        choose = 0
        print("Selected: No Operation (Nop)")

    def choose_freeze():
        global choose
        choose = 1
        print("Selected: Freeze")

    def choose_bypass():
        global choose
        choose = 2
        print("Selected: Bypassing")

    center_y = (screen_height // 2) + 100

    # First row: No Operation (Nop) with radio button
    nop_label = tk.Label(button4_window, text="No Operation (Nop)", font=("Arial", 18), fg="white", bg="#2E2E2E")
    nop_label.place(x=screen_width // 2 - 150, y=center_y - 140)
    nop_radio = tk.Radiobutton(button4_window, variable=radio_var, value=0, command=choose_nop, bg='#2E2E2E')
    nop_radio.place(x=screen_width // 2 + 100, y=center_y - 140)

    # Second row: Freeze with radio button
    freeze_label = tk.Label(button4_window, text="Freeze", font=("Arial", 18), fg="white", bg="#2E2E2E")
    freeze_label.place(x=screen_width // 2 - 150, y=center_y - 100)
    freeze_radio = tk.Radiobutton(button4_window, variable=radio_var, value=1, command=choose_freeze, bg='#2E2E2E')
    freeze_radio.place(x=screen_width // 2 + 100, y=center_y - 100)

    # Third row: Bypassing with radio button
    bypass_label = tk.Label(button4_window, text="Bypassing", font=("Arial", 18), fg="white", bg="#2E2E2E")
    bypass_label.place(x=screen_width // 2 - 150, y=center_y - 60)
    bypass_radio = tk.Radiobutton(button4_window, variable=radio_var, value=2, command=choose_bypass, bg='#2E2E2E')
    bypass_radio.place(x=screen_width // 2 + 100, y=center_y - 60)

    # Calculate center positions for the buttons
    button_width = 180
    button_height = 50
    center_x = (screen_width // 2) - (button_width // 2)
    center_y = (screen_height // 2) + 100

    # Exit button centered below the radio buttons
    exit_button = tk.Button(button4_window, text="Exit", font=("Arial", 18), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", command=lambda: show_root(menu_window, button4_window))
    exit_button.place(x=center_x, y=center_y + 80, width=button_width, height=button_height)
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

    button4_window.mainloop()
