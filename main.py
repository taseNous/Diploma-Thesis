import tkinter as tk
import sys

import manage_instr, registers, memory, method, pipeline

from button_hover import on_enter, on_leave, on_enter_exit, on_leave_exit
from button_hover import on_enter_execute, on_leave_execute

import time

# Function to show the main menu with styled buttons and labels
def main():

    root = tk.Tk()
    root.attributes('-fullscreen', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='#2E2E2E')
    canvas.pack()

    canvas.delete("all")
    canvas.configure(bg='#2E2E2E')

    label1 = tk.Label(root, text="Καλώς ήλθατε! Αυτός είναι ένας εξομοιωτής ενός επεξεργαστή μερικώς επικαλυπτόμενων λειτουργιών.",
                    font=("Arial", 16), fg="#FFFFFF", bg='#2E2E2E')
    label2 = tk.Label(root, text="Δείχνει τη ροή δεδομένων του επεξεργαστή και το πως λειτουργεί ο μηχανισμός του pipeline.",
                    font=("Arial", 14), fg="#FFFFFF", bg='#2E2E2E')
    label4 = tk.Label(root, text="Διπλωματική Εργασία: Βένος Αναστάσιος", font=("Arial", 12), fg="#FFFFFF", bg='#2E2E2E')
    label5 = tk.Label(root, text="Τίτλος: Εξομοιωτής της Ροής Δεδομένων ενός Επεξεργαστή Μερικώς Επικαλυπτόμενων Λειτουργιών",
                    font=("Arial", 12), fg="#FFFFFF", bg='#2E2E2E')
    label6 = tk.Label(root, text="Επιβλέπων Καθηγητής: Νικολός Δημήτριος", font=("Arial", 12), fg="#FFFFFF", bg='#2E2E2E')

    canvas.create_window(screen_width/2, screen_height/3.5, window=label1)
    canvas.create_window(screen_width/2, screen_height/3.1, window=label2)
    canvas.create_window(screen_width/2, screen_height/2.8, window=label4)
    canvas.create_window(screen_width/2, screen_height/2.5, window=label5)
    canvas.create_window(screen_width/2, screen_height/2.3, window=label6)

    button_style = {
        "font": ("Arial", 14),
        "bg": "#61afef",
        "fg": "white",
        "activebackground": "#4fa3e2",
        "activeforeground": "white",
        "width": 20
    }

    #Έξοδος προγράμματος
    def exit():
        root.destroy()
        sys.exit()

    def show_toplevel1():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        manage_instr.create_button1_window(root)

    def show_toplevel2():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        registers.create_button2_window(root)

    def show_toplevel3():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        memory.create_button3_window(root)

    def show_toplevel4():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        method.create_button4_window(root)

    def show_pipeline():
        # Withdraw the root window smoothly
        for i in range(100, -1, -10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        root.withdraw()  # Hide the root window

        # Call the function to show the toplevel window
        pipeline.pipeline_program(root)
        
    button1 = tk.Button(canvas, text="Διαχείριση Εντολών", command=show_toplevel1, **button_style)
    button2 = tk.Button(canvas, text="Διαχείριση Καταχωρητών", command=show_toplevel2, **button_style)
    button3 = tk.Button(canvas, text="Διαχείριση Μνήμης", command=show_toplevel3, **button_style)
    button4 = tk.Button(canvas, text="Επιλογή Μεθόδου", command=show_toplevel4, **button_style)
    button5 = tk.Button(canvas, text="Εκτέλεση Προγράμματος", command=show_pipeline, font=("Arial",14), bg="#66FF66", fg="white", activeforeground="white", activebackground="#4fa3e2", width=20)
    button_exit = tk.Button(canvas, text="Exit", command=exit, 
                            font=("Arial", 14), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", width=20)
    
    button1.bind("<Enter>", on_enter)
    button1.bind("<Leave>", on_leave)
    button2.bind("<Enter>", on_enter)
    button2.bind("<Leave>", on_leave)
    button3.bind("<Enter>", on_enter)
    button3.bind("<Leave>", on_leave)
    button4.bind("<Enter>", on_enter)
    button4.bind("<Leave>", on_leave)
    button5.bind("<Enter>", on_enter_execute)
    button5.bind("<Leave>", on_leave_execute)
    button_exit.bind("<Enter>", on_enter_exit)
    button_exit.bind("<Leave>", on_leave_exit)

    button_y = screen_height / 1.8
    button_spacing = screen_height / 20

    for idx, button in enumerate([button1, button2, button3, button4, button5, button_exit]):
        canvas.create_window(screen_width/2, button_y + idx * button_spacing, window=button)

    root.mainloop()

if __name__ == "__main__":
    main()