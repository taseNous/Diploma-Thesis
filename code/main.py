import tkinter as tk, sys, manage_instr, registers, memory, pipeline, method, time

from button_hover import on_enter, on_leave, on_enter_exit, on_leave_exit, on_enter_execute, on_leave_execute

start_over = 0

# Function to show the main menu with styled buttons and labels
def main():

    global start_over
    start = pipeline.start
    start_over = 0

    root = tk.Tk()
    root.attributes('-fullscreen', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Scaling factor for font and button sizes
    font_scale = screen_width / 1920

    # Canvas to cover the entire window
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='#2E2E2E')
    canvas.pack()

    # Labels with relative positioning and scaled font size
    label1 = tk.Label(root, text="Καλώς ήλθατε! Αυτός είναι ένας προσομοιωτής ενός επεξεργαστή μερικώς επικαλυπτόμενων λειτουργιών.",
                    font=("Arial", int(18 * font_scale)), fg="#FFFFFF", bg='#2E2E2E')
    label2 = tk.Label(root, text="Δείχνει τη ροή δεδομένων του επεξεργαστή και το πως λειτουργεί ο μηχανισμός του μερικώς επικαλυτπόμενων λειτουργιών.",
                    font=("Arial", int(16 * font_scale)), fg="#FFFFFF", bg='#2E2E2E')
    label4 = tk.Label(root, text="Διπλωματική Εργασία: Βένος Αναστάσιος", font=("Arial", int(14 * font_scale)), fg="#FFFFFF", bg='#2E2E2E')
    label5 = tk.Label(root, text="Τίτλος: Εξομοιωτής της Ροής Δεδομένων ενός Επεξεργαστή Μερικώς Επικαλυπτόμενων Λειτουργιών",
                    font=("Arial", int(14 * font_scale)), fg="#FFFFFF", bg='#2E2E2E')
    label6 = tk.Label(root, text="Επιβλέπων Καθηγητής: Νικολός Δημήτριος", font=("Arial", int(14 * font_scale)), fg="#FFFFFF", bg='#2E2E2E')

    # Center labels on the canvas
    canvas.create_window(screen_width/2, screen_height/3.5, window=label1)
    canvas.create_window(screen_width/2, screen_height/3.1, window=label2)
    canvas.create_window(screen_width/2, screen_height/2.8, window=label4)
    canvas.create_window(screen_width/2, screen_height/2.5, window=label5)
    canvas.create_window(screen_width/2, screen_height/2.3, window=label6)

    # Button styling with scaled font size and width
    button_style = {
        "font": ("Arial", int(16 * font_scale)),
        "bg": "#61afef",
        "fg": "black",
        "activebackground": "#4fa3e2",
        "activeforeground": "white",
        "width": int(screen_width / 60)
    }

    # Exit program
    def exit():
        with open("Log.txt", "w", encoding="utf-8") as file:
            file.truncate(0)
        root.destroy()
        sys.exit()

    # Smooth transition to sub-windows
    def smooth_transition(target_function):
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()
        target_function(root)

    def show_pipeline():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        pipeline.pipeline_program(root)

    def show_pipeline1():
        global start_over
        start_over = 1
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        pipeline.pipeline_program(root)

    # Button commands with transition
    button_commands = [
        ("Διαχείριση Εντολών", lambda: smooth_transition(lambda r: manage_instr.create_button1_window(r, screen_width, screen_height))),
        ("Διαχείριση Καταχωρητών", lambda: smooth_transition(registers.create_button2_window)),
        ("Διαχείριση Μνήμης", lambda: smooth_transition(memory.create_button3_window)),
        ("Επιλογή Μεθόδου", lambda: smooth_transition(lambda r: method.create_button4_window(r, screen_width, screen_height)))
    ]

    # Create the buttons with bindings
    buttons = []
    for text, command in button_commands:
        button = tk.Button(canvas, text=text, command=command, **button_style)
        buttons.append(button)

    # Custom styling for Execute and Exit buttons
    execute_button_style = {
        "font": ("Arial", int(16 * font_scale)),
        "bg": "#66FF66",
        "fg": "black",
        "activebackground": "#66FF66",
        "activeforeground": "white",
        "width": int(screen_width / 60)
    }

    if start == 0:
        button5 = tk.Button(canvas, text="Εκτέλεση Προγράμματος", command=show_pipeline, **execute_button_style)
        button_exit = tk.Button(canvas, text="Έξοδος", command=exit, 
                                font=("Arial", int(16 * font_scale)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white", width=int(screen_width/60))
        button5.bind("<Enter>", on_enter_execute)
        button5.bind("<Leave>", on_leave_execute)
    elif start == 1:
        button6 = tk.Button(canvas, text="Συνέχεια Εκτέλεσης", command=show_pipeline, **execute_button_style)
        button7 = tk.Button(canvas, text="Καινούριο Πρόγραμμα", command=show_pipeline1, **execute_button_style)
        button_exit = tk.Button(canvas, text="Έξοδος", command=exit, 
                                font=("Arial", int(16 * font_scale)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white", width=int(screen_width/60))
        button6.bind("<Enter>", on_enter_execute)
        button6.bind("<Leave>", on_leave_execute)
        button7.bind("<Enter>", on_enter_execute)
        button7.bind("<Leave>", on_leave_execute)
    
    # Add button hover effects
    for button in buttons:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    button_exit.bind("<Enter>", on_enter_exit)
    button_exit.bind("<Leave>", on_leave_exit)

    # Position buttons with relative Y positions
    button_y = screen_height / 1.8
    button_spacing = screen_height / 20

    if start == 0:
        # Add buttons to canvas with calculated positions
        for idx, button in enumerate(buttons + [button5, button_exit]):
            canvas.create_window(screen_width/2, button_y + idx * button_spacing, window=button)
    elif start == 1:
        # Add buttons to canvas with calculated positions
        for idx, button in enumerate(buttons + [button6, button7, button_exit]):
            canvas.create_window(screen_width/2, button_y + idx * button_spacing, window=button)

    root.mainloop()

if __name__ == "__main__":
    main()