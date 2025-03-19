# This file is responsible for the window of instruction management

import tkinter as tk, gui_vars, vars, time, json

from instr import Instruction, namestr

from vars import r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, none

from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit, on_enter_delete, on_leave_delete, on_enter_instr, on_leave_instr

from tkinter import filedialog

# Mapping of instruction names to opcodes
opcode_mapping = {
    "NOP": "0000000",
    "LOAD": "0010000",
    "STORE": "0100000",
    "ADD": "0000001",
    "SUB": "0000010",
    "AND": "0000011",
    "BRE": "1110000"
}

def create_button1_window(menu_window, screen_width, screen_height):
    global d
    Instr_Cache = gui_vars.Instr_Cache  # Access Instr_Cache

    button1_window = tk.Toplevel(menu_window)
    button1_window.title("Button 1 Window")
    button1_window.attributes('-fullscreen', True)
    button1_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button1_window.attributes("-alpha", i / 100)
        button1_window.update()
        time.sleep(0.02)

    def save_instructions_to_file():
        """
        Save the current instructions to a chosen .json file.
        """
        instructions = []
        for instr in Instr_Cache:
            instructions.append({
                "name": instr.name,
                "opcode": instr.opcode,
                "r1": instr.r1[2] if instr.r1 else None,  # Save register name (e.g., "r0")
                "r2": instr.r2[2] if instr.r2 else None,  # Save register name (e.g., "r1")
                "r3": instr.r3[2] if instr.r3 else None,  # Save register name (e.g., "r2")
                "d": instr.d if instr.d is not None else None,  # Handle `d` safely
            })

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save Instructions As"
        )

        if file_path:
            try:
                with open(file_path, "w") as file:
                    json.dump(instructions, file, indent=4)
                print(f"Instructions saved to {file_path}")
            except Exception as e:
                print(f"Error saving instructions: {e}")
        else:
            print("Save operation canceled.")



    def load_instructions_from_file():
        """
        Load instructions from a selected .json file.
        """
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Load Instructions From"
        )

        if file_path:
            try:
                with open(file_path, "r") as file:
                    instructions = json.load(file)

                gui_vars.Instr_Cache.clear()  # Clear the current cache

                for instr_data in instructions:
                    new_instr = Instruction(
                        name=instr_data["name"],
                        opcode=instr_data["opcode"],
                        r1=vars.__dict__.get(instr_data["r1"], None),  # Map register name back to object
                        r2=vars.__dict__.get(instr_data["r2"], None),  # Map register name back to object
                        r3=vars.__dict__.get(instr_data["r3"], None),  # Map register name back to object
                        d=instr_data["d"]
                    )
                    gui_vars.Instr_Cache.append(new_instr)

                create_dynamic_rows_from_cache()
                print(f"Instructions loaded successfully from {file_path}")
            except Exception as e:
                print(f"Error loading instructions: {e}")
        else:
            print("Load operation canceled.")

        append_and_display()


    # Create a main frame to hold all content
    content_frame = tk.Frame(button1_window, bg='#2E2E2E')
    content_frame.grid(row=0, column=0, sticky="nsew")

    # Fixed size for the left canvas (e.g., half of screen height)
    left_canvas_height = int(screen_height / 2)  # Half the screen height
    left_canvas_width = int(screen_width / 2.4)  # Fixed width for the left canvas

    # Scrollable left frame
    left_canvas = tk.Canvas(content_frame, bg='#2E2E2E', width=left_canvas_width, height=left_canvas_height)
    left_scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=left_canvas.yview)
    left_canvas.configure(yscrollcommand=left_scrollbar.set)

    # Place the scrollbar and canvas
    left_scrollbar.grid(row=0, column=0, sticky="ns")
    left_canvas.grid(row=0, column=1, sticky="n")

    # Create the left frame inside the canvas
    left_frame = tk.Frame(left_canvas, bg='#2E2E2E')
    left_canvas.create_window((0, 0), window=left_frame, anchor="nw")

    # Update the scroll region dynamically
    left_frame.bind("<Configure>", lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all")))

    # Enable mouse wheel scrolling
    def on_mousewheel(event):
        left_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    left_canvas.bind_all("<MouseWheel>", on_mousewheel)  # For Windows and Mac
    left_canvas.bind_all("<Button-4>", lambda event: left_canvas.yview_scroll(-1, "units"))  # For Linux scroll up
    left_canvas.bind_all("<Button-5>", lambda event: left_canvas.yview_scroll(1, "units"))  # For Linux scroll down

    # Right frame remains the same
    right_frame = tk.Frame(content_frame, bg='#2E2E2E')
    right_frame.grid(row=0, column=2, padx=int(screen_width/38.4), pady=int(screen_height/21.6), sticky='n')

    # Left column: Headers and input for commands (Unchanged)
    left_header = tk.Label(left_frame, text="Instrutions in Instruction Cache", font=("Arial", int(int(screen_width/106.6666))), bg='#2E2E2E', fg="white")
    left_header.grid(row=0, column=0, columnspan=3, pady=int(screen_height/108))

    command_label = tk.Label(left_frame, text="How many instructions do you want to add?", font=("Arial", int(int(screen_width/137.1428))), bg='#2E2E2E', fg="white")
    command_label.grid(row=1, column=0, columnspan=3, pady=int(screen_height/108))

    command_input = tk.Entry(left_frame, font=("Arial", int(screen_width/137.1428)))
    command_input.grid(row=2, column=0, columnspan=2, pady=int(screen_height/216))

    add_button = tk.Button(left_frame, text="Add", font=("Arial", int(screen_width/137.1428)), fg="black", bg= "#61afef", activebackground="#4fa3e2", activeforeground="white", command=lambda: create_dynamic_rows_from_cache(left_frame))
    add_button.grid(row=2, column=2, pady=int(screen_height/216))
    add_button.bind("<Enter>", on_enter)
    add_button.bind("<Leave>", on_leave)

    # Position insertion input
    position_label = tk.Label(left_frame, text="In which row do you want to add the instruction?", font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white")
    position_label.grid(row=3, column=0, columnspan=3, pady=int(screen_height/108))

    position_input = tk.Entry(left_frame, font=("Arial", int(screen_width/137.1428)))
    position_input.grid(row=4, column=0, columnspan=2, pady=int(screen_height/216))

    def add_instruction_at_position():
        # Retrieve the position and command from the input fields
        try:
            position = int(position_input.get()) - 1  # Convert to zero-based index
            if position < 0 or position > len(gui_vars.Instr_Cache):
                print("Invalid position entered")
                return
        except ValueError:
            print("Please enter a valid integer position")
            return

        # Create a new instruction (you can customize the instruction details here)
        new_instruction = Instruction("N/A", "0000000", None, None, None, None)
        
        # Insert the new instruction at the specified position
        gui_vars.Instr_Cache.insert(position, new_instruction)
        
        # Refresh the displayed instructions to reflect the update
        create_dynamic_rows_from_cache()

    add_button1 = tk.Button(left_frame, text="Add", font=("Arial", int(screen_width/137.1428)), fg="black", bg= "#61afef", activebackground="#4fa3e2", activeforeground="white")
    add_button1.grid(row=4, column=2, pady=int(screen_height/216))
    add_button1.config(command=add_instruction_at_position)
    add_button1.bind("<Enter>", on_enter)
    add_button1.bind("<Leave>", on_leave)

    # Header row for the left column
    number_header = tk.Label(left_frame, text="Number", font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white", width=int(screen_width/128))
    instruction_header = tk.Label(left_frame, text="Instruction", font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white", width=int(screen_width/128))
    registers_header = tk.Label(left_frame, text="Registers", font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white", width=int(screen_width/128))
    action_header = tk.Label(left_frame, text="Action", font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white", width=int(screen_width/128))

    number_header.grid(row=5, column=0, sticky="w")
    instruction_header.grid(row=5, column=1)
    registers_header.grid(row=5, column=2)
    action_header.grid(row=5, column=3)

    # Frame to hold the dynamic rows for the added commands
    command_frame = tk.Frame(left_frame, bg='#2E2E2E')
    command_frame.grid(row=6, column=0, columnspan=5, pady=int(screen_height/108))

    # List to keep track of the command boxes
    command_boxes = []

    # Function to create dynamic rows based on the length of Instr_Cache
    def create_dynamic_rows_from_cache():
        Instr_Cache = gui_vars.Instr_Cache  # Access Instr_Cache
        num_commands = len(Instr_Cache)  # Determine how many rows to create

        # Clear existing rows and reset command_boxes list
        for widget in command_frame.winfo_children():
            widget.destroy()
        command_boxes.clear()  # Clear old widget references

        # Populate command_frame with new widgets
        for i in range(num_commands):
            number_label = tk.Label(command_frame, text=str(i + 1), font=("Arial", int(screen_width/137.1428)), bg='#2E2E2E', fg="white", width=int(screen_width/192))
            instruction_box = tk.Label(command_frame, text="", font=("Arial", int(screen_width/137.1428)), bg="lightgray", width=10, height=2, relief="solid")
            instruction_box1 = tk.Label(command_frame, text="", font=("Arial", int(screen_width/137.1428)), bg="lightgray", width=10, height=2, relief="solid")
            small_box1 = tk.Label(command_frame, text="", font=("Arial", int(screen_width/160)), bg="lightgray", width=int(screen_width/240), height=2, relief="solid")
            small_box2 = tk.Label(command_frame, text="", font=("Arial", int(screen_width/160)), bg="lightgray", width=int(screen_width/240), height=2, relief="solid")
            small_box3 = tk.Label(command_frame, text="", font=("Arial", int(screen_width/160)), bg="lightgray", width=int(screen_width/240), height=2, relief="solid")

            delete_button = tk.Button(command_frame, text="Delete", font=("Arial", int(screen_width/192)), bg="red", fg="white", command=lambda index=i: delete_row(index))
            delete_button.bind("<Enter>", on_enter_delete)
            delete_button.bind("<Leave>", on_leave_delete)

            # Place widgets in the grid
            number_label.grid(row=i + 1, column=0, sticky="w")
            instruction_box.grid(row=i + 1, column=1)
            small_box1.grid(row=i + 1, column=2, sticky='w')
            small_box2.grid(row=i + 1, column=3, sticky='w')
            small_box3.grid(row=i + 1, column=4, sticky='w')
            delete_button.grid(row=i + 1, column=5)

            # Store widget references in command_boxes
            command_boxes.append((instruction_box, instruction_box1, small_box1, small_box2, small_box3))

            # Populate rows with data from Instr_Cache
            instr_obj = Instr_Cache[i]
            instruction_box.config(text=instr_obj.name)
            small_box1.config(text=namestr(instr_obj.r1, globals()) if instr_obj.r1 != none else "None")
            small_box2.config(text=namestr(instr_obj.r2, globals()) if instr_obj.r2 != none else "None")
            small_box3.config(text=namestr(instr_obj.r3, globals()) if instr_obj.r3 != none else "None")

            # Bind click and hover events to each label to make them interactive
            instruction_box.bind("<Button-1>", lambda event, box=instruction_box: on_instruction_box_click(box))
            instruction_box.bind("<Enter>", on_enter_instr)
            instruction_box.bind("<Leave>", on_leave_instr)

            small_box1.bind("<Button-1>", lambda event, box=small_box1: on_register_box_click(box))
            small_box1.bind("<Enter>", on_enter_instr)
            small_box1.bind("<Leave>", on_leave_instr)

            small_box2.bind("<Button-1>", lambda event, box=small_box2: on_register_box_click(box))
            small_box2.bind("<Enter>", on_enter_instr)
            small_box2.bind("<Leave>", on_leave_instr)

            small_box3.bind("<Button-1>", lambda event, box=small_box3: on_register_box_click(box))
            small_box3.bind("<Enter>", on_enter_instr)
            small_box3.bind("<Leave>", on_leave_instr)

    # Restore click handler functions
    def on_instruction_box_click(box):
        button1_window.selected_box = box
        button1_window.box_type = "instruction"

    def on_register_box_click(box):
        button1_window.selected_box = box
        button1_window.box_type = "register"

    # Update the delete_row function
    def delete_row(index):
        Instr_Cache = gui_vars.Instr_Cache
        Instr_Cache.pop(index)
        create_dynamic_rows_from_cache()  # Refresh rows after deletion
        append_and_display()

    # Modify the add button's command to take the number of rows from the input field
    def add_rows():
        Instr_Cache = gui_vars.Instr_Cache
        max_rows = 40  # Define the maximum number of rows allowed

        try:
            num_to_add = int(command_input.get())
            
            # Limit the number of rows to add so that total rows do not exceed 20
            current_row_count = len(Instr_Cache)
            if current_row_count >= max_rows:
                print("Maximum of 20 rows already reached.")
                return

            # Calculate remaining rows that can be added
            num_to_add = min(num_to_add, max_rows - current_row_count)

            for _ in range(num_to_add):
                # Create a new blank instruction and add to Instr_Cache
                new_instruction = Instruction("N/A", "0000000", None, None, None, None)
                Instr_Cache.append(new_instruction)

            create_dynamic_rows_from_cache()
        except ValueError:
            print("Invalid number entered")



    # Replace the existing add_button command with the new function
    add_button.config(command=add_rows)

    # Call this function when the window opens to display rows automatically
    create_dynamic_rows_from_cache()

    

    # Functions to handle inserting text into the clicked boxes
    def on_instruction_box_click(box):
        button1_window.selected_box = box
        button1_window.box_type = "instruction"

    def on_register_box_click(box):
        button1_window.selected_box = box
        button1_window.box_type = "register"

    # Bind the instruction to the boxes for creation
    def insert_text_in_box(text):
        if hasattr(button1_window, 'selected_box') and button1_window.selected_box:
            if button1_window.box_type == "instruction" and text in ["LOAD", "ADD", "STORE", "NOP", "SUB", "AND", "BRE"]:
                button1_window.selected_box.config(text=text, bg="white")
                button1_window.instruction_name = text
            elif button1_window.box_type == "register" and text in ["r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]:
                button1_window.selected_box.config(text=text, bg="white")

    # Function to append instructions and update the row dynamically
    def append_and_display():
        Instr_Cache = gui_vars.Instr_Cache  # Access Instr_Cache

        for i, (instruction_box, instruction_text1, small_box1, small_box2, small_box3) in enumerate(command_boxes):
            instruction_text = instruction_box.cget("text")
            instruction_text1 = instruction_box.cget("text")
            reg1_text = small_box1.cget("text")
            reg2_text = small_box2.cget("text")
            reg3_text = small_box3.cget("text")

            # Update the existing instruction in Instr_Cache
            if instruction_text and instruction_text1 in ["LOAD"]:

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")

                # Only require reg1 and reg2, and set reg3 to None
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].r1 = r0 if reg1_text == 'r0' else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4 
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = none  # No third register

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                # small_box1.config(text=reg1_text)
                # small_box2.config(text=reg2_text)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                small_box3.config(text="None")

            elif instruction_text and instruction_text1 in ["STORE"]:

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")

                # Only require reg1 and reg2, and set reg3 to None
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].r1 = r0 if reg1_text == "r0" else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = none  # No third register

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                small_box3.config(text="None")

            elif instruction_text and instruction_text1 in ["ADD"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r0 if reg1_text == "r0" else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = r0 if reg3_text == "r0" else r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4 if reg3_text == "r4" else r5 if reg3_text == "r5" else r6 if reg3_text == "r6" else r7 if reg3_text == "r7" else r8 if reg3_text == "r8" else r9 if reg3_text == "r9" else r10 if reg3_text == "r10" else r11 if reg3_text == "r11" else r12 if reg3_text == "r12" else r13 if reg3_text == "r13" else r14 if reg3_text == "r14" else r15 if reg3_text == "r15" else r4
                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                small_box3.config(text=Instr_Cache[i].r3[2])

            elif instruction_text and instruction_text1 in ["AND"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r0 if reg1_text == "r0" else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = r0 if reg3_text == "r0" else r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4 if reg3_text == "r4" else r5 if reg3_text == "r5" else r6 if reg3_text == "r6" else r7 if reg3_text == "r7" else r8 if reg3_text == "r8" else r9 if reg3_text == "r9" else r10 if reg3_text == "r10" else r11 if reg3_text == "r11" else r12 if reg3_text == "r12" else r13 if reg3_text == "r13" else r14 if reg3_text == "r14" else r15 if reg3_text == "r15" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                small_box3.config(text=Instr_Cache[i].r3[2])

            elif instruction_text and instruction_text1 in ["SUB"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r0 if reg1_text == "r0" else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = r0 if reg3_text == "r0" else r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4 if reg3_text == "r4" else r5 if reg3_text == "r5" else r6 if reg3_text == "r6" else r7 if reg3_text == "r7" else r8 if reg3_text == "r8" else r9 if reg3_text == "r9" else r10 if reg3_text == "r10" else r11 if reg3_text == "r11" else r12 if reg3_text == "r12" else r13 if reg3_text == "r13" else r14 if reg3_text == "r14" else r15 if reg3_text == "r15" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                small_box3.config(text=Instr_Cache[i].r3[2])

            elif instruction_text and instruction_text1 in ["BRE"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r0 if reg1_text == "r0" else r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4 if reg1_text == "r4" else r5 if reg1_text == "r5" else r6 if reg1_text == "r6" else r7 if reg1_text == "r7" else r8 if reg1_text == "r8" else r9 if reg1_text == "r9" else r10 if reg1_text == "r10" else r11 if reg1_text == "r11" else r12 if reg1_text == "r12" else r13 if reg1_text == "r13" else r14 if reg1_text == "r14" else r15 if reg1_text == "r15" else r4
                Instr_Cache[i].r2 = r0 if reg2_text == "r0" else r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4 if reg2_text == "r4" else r5 if reg2_text == "r5" else r6 if reg2_text == "r6" else r7 if reg2_text == "r7" else r8 if reg2_text == "r8" else r9 if reg2_text == "r9" else r10 if reg2_text == "r10" else r11 if reg2_text == "r11" else r12 if reg2_text == "r12" else r13 if reg2_text == "r13" else r14 if reg2_text == "r14" else r15 if reg2_text == "r15" else r4
                Instr_Cache[i].r3 = Instr_Cache[i].d
                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=Instr_Cache[i].r1[2])
                small_box2.config(text=Instr_Cache[i].r2[2])
                # small_box3.config(text=Instr_Cache[i].r3[2])
                small_box3.config(text=reg3_text if reg3_text else "None")

            elif instruction_text and instruction_text1 in ["NOP"]:
                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = none  # No first register
                Instr_Cache[i].r2 = none  # No second register
                Instr_Cache[i].r3 = none  # No third register

        update_bre_rows()

    load_button = tk.Button(
        content_frame, 
        text="Load Instructions", 
        font=("Arial", int(screen_width/137.1428)), 
        fg="black", 
        bg="#61afef", 
        activebackground="#4fa3e2", 
        activeforeground="white", 
        command=load_instructions_from_file
    )
    load_button.grid(row=4, column=0, columnspan=2, pady=int(screen_height/108))
    load_button.bind("<Enter>", on_enter)
    load_button.bind("<Leave>", on_leave)

    save_button = tk.Button(
        content_frame, 
        text="Save Instructions", 
        font=("Arial", int(screen_width/137.1428)), 
        fg="black", 
        bg="#61afef", 
        activebackground="#4fa3e2", 
        activeforeground="white", 
        command=save_instructions_to_file
    )
    save_button.grid(row=3, column=0, columnspan=2, pady=int(screen_height/108))
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    # Right column: Headers and buttons
    right_header1 = tk.Label(right_frame, text="Add Instructions", font=("Arial", int(screen_width/106.6666)), bg='#2E2E2E', fg="white")
    right_header1.grid(row=0, column=2, columnspan=2, pady=int(screen_height/108))

    load_button = tk.Button(right_frame, text="LOAD", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("LOAD"))
    load_button.bind("<Enter>", on_enter_instr)
    load_button.bind("<Leave>", on_leave_instr)
    store_button = tk.Button(right_frame, text="STORE", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("STORE"))
    store_button.bind("<Enter>", on_enter_instr)
    store_button.bind("<Leave>", on_leave_instr)
    add_instr_button = tk.Button(right_frame, text="ADD", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("ADD"))
    add_instr_button.bind("<Enter>", on_enter_instr)
    add_instr_button.bind("<Leave>", on_leave_instr)
    sub_instr_button = tk.Button(right_frame, text="SUB", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("SUB"))
    sub_instr_button.bind("<Enter>", on_enter_instr)
    sub_instr_button.bind("<Leave>", on_leave_instr)
    and_instr_button = tk.Button(right_frame, text="AND", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("AND"))
    and_instr_button.bind("<Enter>", on_enter_instr)
    and_instr_button.bind("<Leave>", on_leave_instr)
    bre_instr_button = tk.Button(right_frame, text="BRE", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("BRE"))
    bre_instr_button.bind("<Enter>", on_enter_instr)
    bre_instr_button.bind("<Leave>", on_leave_instr)

    # if choose == 1 or choose == 3:
    nop_button = tk.Button(right_frame, text="NOP", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/192), height=2, command=lambda: insert_text_in_box("NOP"))
    nop_button.bind("<Enter>", on_enter_instr)
    nop_button.bind("<Leave>", on_leave_instr)
    nop_button.grid(row=1, column=6, pady=int(screen_height/216))

    load_button.grid(row=1, column=0, pady=int(screen_height/216))
    store_button.grid(row=1, column=1, pady=int(screen_height/216))
    add_instr_button.grid(row=1, column=2, pady=int(screen_height/216))
    sub_instr_button.grid(row=1, column=3, pady=int(screen_height/216))
    and_instr_button.grid(row=1, column=4, pady=int(screen_height/216))
    bre_instr_button.grid(row=1, column=5, pady=int(screen_height/216))

    # Adding a new header and buttons for registers
    register_header = tk.Label(right_frame, text="Add Registers", font=("Arial", 18), bg='#2E2E2E', fg="white")
    register_header.grid(row=2, column=0, columnspan=3, pady=10)

    # Label for "Μετατόπιση"
    metatopisi_label = tk.Label(right_frame, text="Offset", font=("Arial", int(screen_width/106.6666)), bg='#2E2E2E', fg="white")
    metatopisi_label.grid(row=7, column=0)

     # Placeholder for dynamically generated BRE rows
    bre_rows_frame = tk.Frame(right_frame, bg='#2E2E2E')
    bre_rows_frame.grid(row=8, column=0, columnspan=4, pady=int(screen_height/108))

    # Function to update BRE rows based on BRE instructions in Instr_Cache
    def update_bre_rows():
        # Clear any existing rows in bre_rows_frame
        for widget in bre_rows_frame.winfo_children():
            widget.destroy()

        # Create rows for each BRE instruction
        for index, instr in enumerate(gui_vars.Instr_Cache):
            if instr.name == "BRE":
                # Display the BRE instruction row
                row_number = tk.Label(bre_rows_frame, text=str(index + 1), font=("Arial", 14), bg='#2E2E2E', fg="white")
                bre_label = tk.Label(bre_rows_frame, text="BRE", font=("Arial", 14), bg='#2E2E2E', fg="white")
                bre_input = tk.Entry(bre_rows_frame, font=("Arial", 14), width=10)
                bre_button = tk.Button(bre_rows_frame, text="Καταχώρηση", font=("Arial", 14), command=lambda i=index, entry=bre_input: save_bre_value(i, entry))

                # Grid each widget in the row
                row_number.grid(row=index, column=0, padx=5, pady=5)
                bre_label.grid(row=index, column=1, padx=5, pady=5)
                bre_input.grid(row=index, column=2, padx=5, pady=5)
                bre_button.grid(row=index, column=3, padx=5, pady=5)

    # Function to save the input value for BRE instruction
    def save_bre_value(index, entry):
        value = entry.get()
        if value:
            # Update the corresponding Instruction object with the value from the input field
            gui_vars.Instr_Cache[index].d = value
            entry.delete(0, tk.END)  # Clear the entry field after saving

    # Call update_bre_rows initially to load any existing BRE instructions
    update_bre_rows()

    r0_button = tk.Button(right_frame, text="r0", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r0"))
    r0_button.bind("<Enter>", on_enter_instr)
    r0_button.bind("<Leave>", on_leave_instr)
    r1_button = tk.Button(right_frame, text="r1", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r1"))
    r1_button.bind("<Enter>", on_enter_instr)
    r1_button.bind("<Leave>", on_leave_instr)
    r2_button = tk.Button(right_frame, text="r2", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r2"))
    r2_button.bind("<Enter>", on_enter_instr)
    r2_button.bind("<Leave>", on_leave_instr)
    r3_button = tk.Button(right_frame, text="r3", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r3"))
    r3_button.bind("<Enter>", on_enter_instr)
    r3_button.bind("<Leave>", on_leave_instr)
    r4_button = tk.Button(right_frame, text="r4", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r4"))
    r4_button.bind("<Enter>", on_enter_instr)
    r4_button.bind("<Leave>", on_leave_instr)
    r5_button = tk.Button(right_frame, text="r5", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r5"))
    r5_button.bind("<Enter>", on_enter_instr)
    r5_button.bind("<Leave>", on_leave_instr)
    r6_button = tk.Button(right_frame, text="r6", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r6"))
    r6_button.bind("<Enter>", on_enter_instr)
    r6_button.bind("<Leave>", on_leave_instr)
    r7_button = tk.Button(right_frame, text="r7", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r7"))
    r7_button.bind("<Enter>", on_enter_instr)
    r7_button.bind("<Leave>", on_leave_instr)
    r8_button = tk.Button(right_frame, text="r8", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r8"))
    r8_button.bind("<Enter>", on_enter_instr)
    r8_button.bind("<Leave>", on_leave_instr)
    r9_button = tk.Button(right_frame, text="r9", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r9"))
    r9_button.bind("<Enter>", on_enter_instr)
    r9_button.bind("<Leave>", on_leave_instr)
    r10_button = tk.Button(right_frame, text="r10", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r10"))
    r10_button.bind("<Enter>", on_enter_instr)
    r10_button.bind("<Leave>", on_leave_instr)
    r11_button = tk.Button(right_frame, text="r11", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r11"))
    r11_button.bind("<Enter>", on_enter_instr)
    r11_button.bind("<Leave>", on_leave_instr)
    r12_button = tk.Button(right_frame, text="r12", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r12"))
    r12_button.bind("<Enter>", on_enter_instr)
    r12_button.bind("<Leave>", on_leave_instr)
    r13_button = tk.Button(right_frame, text="r13", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r13"))
    r13_button.bind("<Enter>", on_enter_instr)
    r13_button.bind("<Leave>", on_leave_instr)
    r14_button = tk.Button(right_frame, text="r14", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r14"))
    r14_button.bind("<Enter>", on_enter_instr)
    r14_button.bind("<Leave>", on_leave_instr)
    r15_button = tk.Button(right_frame, text="r15", font=("Arial", int(screen_width/137.1428)), width=int(screen_width/384), height=2, command=lambda: insert_text_in_box("r15"))
    r15_button.bind("<Enter>", on_enter_instr)
    r15_button.bind("<Leave>", on_leave_instr)

    r0_button.grid(row=3, column=0, pady=int(screen_height/216))
    r1_button.grid(row=3, column=1, pady=int(screen_height/216))
    r2_button.grid(row=3, column=2, pady=int(screen_height/216))
    r3_button.grid(row=3, column=3, pady=int(screen_height/216))
    r4_button.grid(row=4, column=0, pady=int(screen_height/216))
    r5_button.grid(row=4, column=1, pady=int(screen_height/216))
    r6_button.grid(row=4, column=2, pady=int(screen_height/216))
    r7_button.grid(row=4, column=3, pady=int(screen_height/216))
    r8_button.grid(row=5, column=0, pady=int(screen_height/216))
    r9_button.grid(row=5, column=1, pady=int(screen_height/216))
    r10_button.grid(row=5, column=2, pady=int(screen_height/216))
    r11_button.grid(row=5, column=3, pady=int(screen_height/216))
    r12_button.grid(row=6, column=0, pady=int(screen_height/216))
    r13_button.grid(row=6, column=1, pady=int(screen_height/216))
    r14_button.grid(row=6, column=2, pady=int(screen_height/216))
    r15_button.grid(row=6, column=3, pady=int(screen_height/216))

    # Button to append instructions to Instr_Cache and display them in rows
    append_button = tk.Button(content_frame, text="Instruction Registration", font=("Arial", int(screen_width/137.1428)), fg="black", bg= "#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_and_display)
    append_button.grid(row=2, column=0, columnspan=2, pady=int(screen_height/108))
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    def close_button1_open_menu(event=None):
        """
        Close the current button1_window and show the menu_window.
        Triggered by pressing the "Esc" key.
        """
        # button1_window.destroy()  # Close the current window
        # menu_window.deiconify()  # Show the menu window
        show_root(menu_window, button1_window)

    # Exit button centered at the bottom of the content frame
    exit_button = tk.Button(content_frame, text="Exit", font=("Arial", int(screen_width/137.1428)), bg="#ff6666", fg="black", activebackground="#cc0000", activeforeground="white",command=lambda: close_button1_open_menu())
    exit_button.grid(row=5, column=0, columnspan=2, pady=int(screen_height/108), sticky='s')
    exit_button.bind("<Enter>", on_enter_exit)
    exit_button.bind("<Leave>", on_leave_exit)
    
    # Bind the "Esc" key to close the current window and open the menu window
    button1_window.bind("<Escape>", close_button1_open_menu)

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

    button1_window.mainloop()