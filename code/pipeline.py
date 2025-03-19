# Window for the program execution

import tkinter as tk, schema, schema_values, table, cycles, fill_table, table_instructions, grades, method, time, main

from tkinter import scrolledtext

from vars import counter

from gui_vars import Instr_Cache

from button_hover import on_enter_pipeline, on_leave_pipeline, on_leave_exit, on_enter_exit

z = 0
start = 0
start_over_var = 0

def pipeline_program(root):

    start_over = main.start_over
    start_over_method = method.start_over_method

    global counter, z, start_over_var
    
    # Create a new top-level window in fullscreen mode with smooth appearance
    new_window = tk.Toplevel(root)
    new_window.title("Pipeline Simulation")
    new_window.attributes('-fullscreen', True)
    new_window.configure(bg='#2E2E2E')

    # Smoothly show the new window
    for i in range(0, 101, 10):
        new_window.attributes("-alpha", i / 100)
        new_window.update()
        time.sleep(0.02)

    # Get screen dimensions to scale elements appropriately
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    # Calculate height for the top left frame (45% of screen height)
    top_left_height = int(screen_height * 0.45)  # 45% of total screen height

    # Calculate the width for the right frame (30% of screen width)
    right_frame_width = int(screen_width * 0.25)  # 30% of total screen width

    # Set base dimensions (e.g., 1920x1080) and calculate scaling factors
    base_width, base_height = 1920, 1080
    width_scale = screen_width / base_width

    # Set fixed width for right frame and scale heights for the canvases
    right_frame_width = int(180 * width_scale)  # Fixed width scaled based on display resolution
    top_left_height = int(screen_height * 0.58)  # 50% of screen height
    bottom_left_height = screen_height - top_left_height  # Remaining height for bottom canvas

    # Create Canvas and Frame widgets with scaled sizes
    top_left_canvas = tk.Canvas(new_window, bg="#E6E6FA", height=top_left_height)
    bottom_left_canvas = tk.Canvas(new_window, bg="#FFDAB9", height=bottom_left_height)
    right_frame = tk.Frame(new_window, bg="#FF6F61", width=right_frame_width)

    # Place the widgets in a grid layout to occupy fullscreen space
    top_left_canvas.grid(row=0, column=0, sticky="nsew")
    bottom_left_canvas.grid(row=1, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

    # Prevent the right frame from expanding in width
    right_frame.grid_propagate(False)

    # Set row and column weights to ensure canvases resize with the window
    new_window.grid_rowconfigure(0, weight=1)
    new_window.grid_rowconfigure(1, weight=1)
    new_window.grid_columnconfigure(0, weight=3)  # Left side (canvases) takes up most space
    new_window.grid_columnconfigure(1, weight=1)  # Right frame with fixed width

    # Add a scrolled text widget to the right frame to display the text file content
    text_display = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, bg="#20B2AA", font=("Arial", int(screen_width/160)))
    text_display.pack(expand=True, fill="both")
    text_display.config(width=right_frame_width // int(screen_width / 192))

    # Functions for updating the display, managing pipeline cycles, and clearing log files
    def next_clock_cycle():
        try:
            with open("Log.txt", "r", encoding="utf-8") as file:
                content = file.read()
                text_display.delete(1.0, tk.END)
                text_display.insert(tk.END, content)
        except FileNotFoundError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "File not found!")
        except UnicodeDecodeError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "Error decoding the file. Please check the file encoding.")
        
        # Scroll to the bottom
        text_display.yview_moveto(1.0)

    if start_over == 1:
        with open("Log.txt", "w", encoding="utf-8") as file:
            file.truncate(0)
        counter = 0
        z = 0

    if start_over_method > start_over_var:
        with open("Log.txt", "w", encoding="utf-8") as file:
            file.truncate(0)
        counter = 0
        z = 0
        start_over_var = start_over_method

    def update_file_content():
        global x, y, z, counter

        choose = method.choose
        
        counter += 1
        y = -1
        x = 0

        # Clear canvases and log file for new cycle
        top_left_canvas.delete('all')
        bottom_left_canvas.delete('all')

        with open("Log.txt", "w") as file:
            pass

        z += 1

        # Write new cycle information to the log file and update the display
        for i in range(z):
            y += 1
            x += 1
            quote = f"\n\nΚύκλος ρολογιού: {x}\n"
            with open("Log.txt", "a", encoding="utf-8") as file:
                file.write(quote)

            cycles.Clock_Cycles(x, y, i)

            if choose == 1:
                grades.vathmides_nop(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 2:
                grades.vathmides_freeze(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 3:
                grades.vathmides_bypassing_nop(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 4:
                grades.vathmides_bypassing_freeze(bottom_left_canvas, screen_width, screen_height, z, i)    
            table_instructions.applytoLabel1(bottom_left_canvas, screen_width, screen_height, z, i)
            fill_table.periodL1(bottom_left_canvas, screen_width, screen_height, i, z)

            next_clock_cycle()

        # Redraw schema pipeline
        schema.pipeline(top_left_canvas, screen_width, screen_height, z)
        schema_values.sch_values(top_left_canvas, screen_width, screen_height, z)
        table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)
        

    def previous_clock_cycle():
        global x, y, z, counter
        y = -1
        x = 0

        choose=method.choose

        counter = counter - 1
        
        # Clear the top_left_canvas
        top_left_canvas.delete('all')
        bottom_left_canvas.delete('all')
        
        # Open the file in write mode, which will truncate (clear) the file
        with open("Log.txt", "w") as file:
            pass  # Do nothing, just open and close to clear the file
        
        z = z - 1

        for i in range(z):
            y = y + 1
            x = x + 1
            quote = "\n\nΚύκλος ρολογιού: "  + str(x) + "\n"
            with open("Log.txt", "a", encoding="utf-8") as file:
                file.write(quote)
            
            cycles.Clock_Cycles(x, y, i)

            if choose == 1:
                grades.vathmides_nop(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 2:
                grades.vathmides_freeze(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 3:
                grades.vathmides_bypassing_nop(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 4:
                grades.vathmides_bypassing_freeze(bottom_left_canvas, screen_width, screen_height, z, i)
            table_instructions.applytoLabel1(bottom_left_canvas, screen_width, screen_height, counter, i)
            fill_table.periodL1(bottom_left_canvas, screen_width, screen_height, i, z)
        
            next_clock_cycle()  # Manually update the display after writing new content

        # Redraw the schema pipeline
        schema.pipeline(top_left_canvas, screen_width, screen_height, z)
        schema_values.sch_values(top_left_canvas, screen_width, screen_height, z)
        table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)
        

    def clear_file_on_exit():
        with open("Log.txt", "w", encoding="utf-8") as file:
            pass
        new_window.destroy()

    def last_cycle():
        global counter, z
        counter = len(Instr_Cache) - 1 + 4
        z = len(Instr_Cache) - 1 + 4
        update_file_content()

    # Call the drawing functions to draw on the canvases
    schema.pipeline(top_left_canvas, screen_width, screen_height, z)
    schema_values.sch_values(top_left_canvas, screen_width, screen_height, z)
    table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)
    next_clock_cycle()

    # Add buttons on the canvas with adaptive placements
    # Define base resolution (e.g., 1920x1080)
    base_width, base_height = 1920, 1080

    # Calculate scaling factors based on the actual screen resolution
    width_scale = screen_width / 1920

    min_font_size = 2
    max_font_size = 8
    # Set font size and positions using scaled dimensions
    font_size = max(min_font_size, min(int(11 * width_scale), max_font_size))  # Set a minimum font size to avoid text being too small

    # Adjust button placement and font size with scaling
    next_button = tk.Button(
        top_left_canvas, 
        text="Next Cycle", 
        font=("Arial", font_size), 
        fg="black", 
        bg="#9370DB", 
        command=update_file_content
    )
    next_button.place(x=screen_width * 0.58 + screen_width/38.4, y=screen_height * 0.45 + screen_height/30.8571, anchor=tk.CENTER)
    next_button.bind("<Enter>", on_enter_pipeline)
    next_button.bind("<Leave>", on_leave_pipeline)

    previous_button = tk.Button(
        top_left_canvas, 
        text="Previous Cycle", 
        font=("Arial", font_size), 
        fg="black", 
        bg="#9370DB", 
        command=previous_clock_cycle
    )
    previous_button.place(x=screen_width * 0.67 + screen_width/48, y=screen_height * 0.45 + screen_height/30.8571, anchor=tk.CENTER)
    previous_button.bind("<Enter>", on_enter_pipeline)
    previous_button.bind("<Leave>", on_leave_pipeline)

    last_button = tk.Button(
        top_left_canvas, 
        text="Last Cycle", 
        font=("Arial", font_size), 
        fg="black", 
        bg="#9370DB", 
        command=last_cycle
    )
    last_button.place(x=screen_width * 0.58 + screen_width/38.4, y=screen_height * 0.48 + screen_height/30.8571, anchor=tk.CENTER)
    last_button.bind("<Enter>", on_enter_pipeline)
    last_button.bind("<Leave>", on_leave_pipeline)

    def close_new_open_menu(event=None):
        global start
        """
        Close the current button1_window and show the menu_window.
        Triggered by pressing the "Esc" key.
        """
        start = 1
        show_root(root, new_window)

    exit_button = tk.Button(
        top_left_canvas, 
        text="Exit", 
        font=("Arial", font_size), 
        bg="#ff6666", 
        command=lambda: close_new_open_menu()
    )
    exit_button.place(x=screen_width * 0.67 + screen_width/48, y=screen_height * 0.48 + screen_height/30.8571, anchor=tk.CENTER)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    # Bind the "Esc" key to close the current window and open the menu window
    new_window.bind("<Escape>", close_new_open_menu)

    # Bind the clear_file_on_exit function to the window close event
    new_window.protocol("WM_DELETE_WINDOW", clear_file_on_exit)

    def show_root(root, top):
        global z, counter

        for i in range(100, -1, -10):
            top.attributes("-alpha", i / 100)
            top.update()
            time.sleep(0.02)
        
        top.withdraw()
        for widget in root.winfo_children():
            widget.destroy()

        main.main()
        for i in range(0, 101, 10):
            root.attributes("-alpha", i / 100)
            root.update()
            time.sleep(0.02)
        
    # Run the application
    new_window.mainloop()