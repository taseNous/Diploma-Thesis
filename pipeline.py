import tkinter as tk
import importlib
import schema, schema_values, table, cycles, fill_table, table_instructions, dependencies, grades
from tkinter import scrolledtext
import vars
from vars import r, r2, r3, r4, counter, start_test
from gui_vars import Instr_Cache
from button_hover import on_enter_pipeline, on_leave_pipeline, on_leave_exit, on_enter_exit
import method
import time

z = 0

def pipeline_program(root):

    choose=method.choose

    new_window = tk.Toplevel(root)
    new_window.title("Button 1 Window")
    new_window.attributes('-fullscreen', True)
    new_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        new_window.attributes("-alpha", i / 100)
        new_window.update()
        time.sleep(0.02)

    if choose == 0:
        dependencies.depend_nop()
    elif choose == 1:
        dependencies.depend_freeze()
    
    # Function to read the content of the text file and update the display
    def update_text_display():
        try:
            # Open the file with UTF-8 encoding
            with open("Log.txt", "r", encoding="utf-8") as file:
                content = file.read()
                text_display.delete(1.0, tk.END)  # Clear the existing content
                text_display.insert(tk.END, content)  # Insert the updated content
        except FileNotFoundError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "File not found!")
        except UnicodeDecodeError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "Error decoding the file. Please check the file encoding.")

    # Function to clear the canvas and reload the schema pipeline
    def update_file_content():
        global x, y, z, counter

        choose=method.choose
        
        counter = counter + 1
        y = -1
        x = 0
        
        # Clear the top_left_canvas
        top_left_canvas.delete('all')
        bottom_left_canvas.delete('all')
        
        # Open the file in write mode, which will truncate (clear) the file
        with open("Log.txt", "w") as file:
            pass  # Do nothing, just open and close to clear the file
        
        z = z + 1
        
        for i in range(z):
            y = y + 1
            x = x + 1
            quote = "\n\nΚύκλος ρολογιού: "  + str(x) + "\n"
            with open("Log.txt", "a", encoding="utf-8") as file:
                file.write(quote)
            if choose == 0:
                grades.vathmides(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 1:
                grades.vathmides1(bottom_left_canvas, screen_width, screen_height, z, i)
            cycles.Clock_Cycles(x, y, i)
            update_text_display()  # Manually update the display after writing new content
        
        # Redraw the schema pipeline
        schema.pipeline(top_left_canvas, screen_width, screen_height)
        schema_values.sch_values(top_left_canvas, screen_width, screen_height)
        table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)
        fill_table.periodL1(bottom_left_canvas, screen_width, screen_height, counter)
        table_instructions.applytoLabel1(bottom_left_canvas, screen_width, screen_height, counter)
        
    def update_file_content1():
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
            if choose == 0:
                grades.vathmides(bottom_left_canvas, screen_width, screen_height, z, i)
            elif choose == 1:
                grades.vathmides1(bottom_left_canvas, screen_width, screen_height, z, i)
            cycles.Clock_Cycles(x, y, i)
            update_text_display()  # Manually update the display after writing new content

        # Redraw the schema pipeline
        schema.pipeline(top_left_canvas, screen_width, screen_height)
        schema_values.sch_values(top_left_canvas, screen_width, screen_height)
        table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)
        fill_table.periodL1(bottom_left_canvas, screen_width, screen_height, counter)
        table_instructions.applytoLabel1(bottom_left_canvas, screen_width, screen_height, counter)
        
    def clear_file_on_exit():
        """Clear the contents of the Log.txt file when the window is closed."""
        with open("Log.txt", "w", encoding="utf-8") as file:
            pass
        new_window.destroy()  # Close the Tkinter window

    def last_cycle():
        global counter, z

        counter = len(Instr_Cache) - 1 + 4
        z = len(Instr_Cache) - 1 + 4
        update_file_content()

    # Get the screen width and height
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    # Calculate the height for the top-left frame (45% of screen height)
    top_left = int(screen_height * 0.45)  # Adjust this percentage as needed

    # Calculate the width for the right frame (30% of screen width)
    right_frame_width = int(screen_width * 0.3)  # Adjust this percentage as needed

    # Configure the grid layout
    new_window.grid_rowconfigure(0, weight=1)
    new_window.grid_rowconfigure(1, weight=1)
    new_window.grid_columnconfigure(0, weight=1)  # Give full weight to the left column
    new_window.grid_columnconfigure(1, weight=0)  # No additional weight to the right column

    # Create Canvas widgets for the left grids
    top_left_canvas = tk.Canvas(new_window, bg="#E6E6FA", height=top_left)
    bottom_left_canvas = tk.Canvas(new_window, bg="#FFDAB9")
    right_frame = tk.Frame(new_window, bg="#FF6F61", width=right_frame_width)  # Use the calculated width

    # Place the widgets in the grid
    top_left_canvas.grid(row=0, column=0, sticky="nsew")
    bottom_left_canvas.grid(row=1, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")  # The right grid spans both rows

    # Disable the right frame's automatic resizing so it stays at the calculated width
    right_frame.grid_propagate(False)

    # Add a scrolled text widget to the right frame to display the text file content
    text_display = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, bg="#20B2AA", font=("Arial", int(screen_width/160)))
    text_display.pack(expand=True, fill="both")  # Fill the right frame

    # Set the width of the text display manually to match the right_frame_width
    text_display.config(width=right_frame_width // int(screen_width/192))  # Convert pixels to character width

    # Call the drawing functions to draw on the canvases
    schema.pipeline(top_left_canvas, screen_width, screen_height)
    schema_values.sch_values(top_left_canvas, screen_width, screen_height)
    table.create_simple_canvas(bottom_left_canvas, screen_width, screen_height)

    update_text_display()

    # Add a button to the bottom left canvas to trigger content update
    next_button = tk.Button(top_left_canvas, text="Επόμενος Κύκλος", bg="#9370DB", command=update_file_content)
    next_button.place(x=screen_width/1.7, y=screen_height/1.9636, anchor=tk.CENTER)
    next_button.bind("<Enter>", on_enter_pipeline)
    next_button.bind("<Leave>", on_leave_pipeline)

    # Add a button to the bottom left canvas to trigger content update
    previous_button = tk.Button(top_left_canvas, text="Προηγούμενος Κύκλος", bg="#9370DB", command=update_file_content1)
    previous_button.place(x=screen_width/1.5, y=screen_height/1.9636, anchor=tk.CENTER)
    previous_button.bind("<Enter>", on_enter_pipeline)
    previous_button.bind("<Leave>", on_leave_pipeline)

    # Add a button to the bottom left canvas to trigger content update
    last_button = tk.Button(top_left_canvas, text="Τελευταίος Κύκλος", bg="#9370DB", command=last_cycle)
    last_button.place(x=screen_width/1.7, y=screen_height/1.85, anchor=tk.CENTER)
    last_button.bind("<Enter>", on_enter_pipeline)
    last_button.bind("<Leave>", on_leave_pipeline)

    # Add a button to the bottom left canvas to trigger content update
    exit_button = tk.Button(top_left_canvas, text="Έξοδος", bg="#ff6666", command=lambda: show_root(root, new_window))
    exit_button.place(x=screen_width/1.5, y=screen_height/1.85, anchor=tk.CENTER)
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)

    # Bind the clear_file_on_exit function to the window close event
    new_window.protocol("WM_DELETE_WINDOW", clear_file_on_exit)

    def show_root(root, top):

        global z, counter

        with open("Log.txt", "w", encoding="utf-8") as file:
            pass

        importlib.reload(vars)
        
        counter = 0
        z = 0

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

    # Run the application
    new_window.mainloop()