import tkinter as tk
from instr import Instruction, none, namestr
from vars import r0, r1, r2, r3, r4, r5, r6, r7
import gui_vars
from button_hover import on_enter, on_leave, on_leave_exit, on_enter_exit, on_enter_delete, on_leave_delete, on_enter_instr, on_leave_instr
import method
import time

# Mapping of instruction names to opcodes
opcode_mapping = {
    "NOP": "0000000",
    "LOAD": "0000001",
    "STORE": "0000010",
    "ADD": "0000011",
    "SUB": "0000011",
    "AND": "0000011",
    "BRE": "0000100"
}

def create_instruction_from_boxes(instruction, reg1, reg2, reg3=None, append_to_cache=True):
    Instr_Cache = gui_vars.Instr_Cache

    # Get the opcode for the instruction
    opcode = opcode_mapping.get(instruction, "unknown")
    
    # Convert register names to variables from vars
    reg_map = {
        "r1": r0,
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "r4": r4,
        "r5": r5,
        "r6": r6,
        "r7": r7
    }

    # Get the appropriate register variables
    reg1_value = reg_map.get(reg1, none)
    reg2_value = reg_map.get(reg2, none)

    # If instruction is LOAD or STORE, set reg3 to None
    if instruction in ["LOAD", "STORE"]:
        reg3_value = none
    elif instruction in ["NOP"]:
        reg1_value = none
        reg2_value = none
        reg3_value = none
    else:
        reg3_value = reg_map.get(reg3, none) if reg3 else none

    # Create the instruction object
    new_instruction = Instruction(instruction, opcode, reg1_value, reg2_value, reg3_value, none)

    # Append to Instr_Cache only if specified
    if append_to_cache:
        Instr_Cache.append(new_instruction)
        
    return new_instruction  # Return the newly created instruction for display purposes

def create_button1_window(menu_window):

    choose = method.choose

    button1_window = tk.Toplevel(menu_window)
    button1_window.title("Button 1 Window")
    button1_window.attributes('-fullscreen', True)
    button1_window.configure(bg='#2E2E2E')

    # Show the toplevel window smoothly
    for i in range(0, 101, 10):
        button1_window.attributes("-alpha", i / 100)
        button1_window.update()
        time.sleep(0.02)

    # Main frame for centering content
    main_frame = tk.Frame(button1_window, bg='#2E2E2E')
    main_frame.pack(expand=True, fill='both')

    # Create a subframe in the middle of the main frame
    content_frame = tk.Frame(main_frame, bg='#2E2E2E')
    content_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Create scrollable area for the left frame
    left_canvas = tk.Canvas(content_frame, bg='#2E2E2E', width=800, height=600)
    scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=left_canvas.yview)
    # Configure the canvas to use the scrollbar
    left_canvas.configure(yscrollcommand=scrollbar.set)

    # Place the scrollbar on the left, and the canvas on the right of the scrollbar
    scrollbar.grid(row=0, column=0, sticky='ns')  # Place scrollbar on the left
    left_canvas.grid(row=0, column=1, padx=30, pady=30, sticky='n')  # Canvas is now to the right of the scrollbar

    # Create the left frame inside the canvas
    left_frame = tk.Frame(left_canvas, bg='#2E2E2E')
    left_canvas.create_window((0, 0), window=left_frame, anchor="nw")

    # Update scroll region dynamically
    left_frame.bind("<Configure>", lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all")))

    # Right frame remains the same
    right_frame = tk.Frame(content_frame, bg='#2E2E2E')
    right_frame.grid(row=0, column=2, padx=50, pady=50, sticky='n')

    # Left column: Headers and input for commands (Unchanged)
    left_header = tk.Label(left_frame, text="Εντολές στην Κρυφή Μνήμη Εντολών", font=("Arial", 18), bg='#2E2E2E', fg="white")
    left_header.grid(row=0, column=0, columnspan=3, pady=10)

    command_label = tk.Label(left_frame, text="Πόσες εντολές θέλετε να προσθέσετε;", font=("Arial", 14), bg='#2E2E2E', fg="white")
    command_label.grid(row=1, column=0, columnspan=3, pady=10)

    command_input = tk.Entry(left_frame, font=("Arial", 14))
    command_input.grid(row=2, column=0, columnspan=2, pady=5)

    add_button = tk.Button(left_frame, text="Προσθήκη", font=("Arial", 14), fg="#FFFFFF", bg= "#61afef", activebackground="#4fa3e2", activeforeground="white", command=lambda: create_dynamic_rows_from_cache(left_frame))
    add_button.grid(row=2, column=2, pady=5)
    add_button.bind("<Enter>", on_enter)
    add_button.bind("<Leave>", on_leave)

    # Header row for the left column
    number_header = tk.Label(left_frame, text="Αριθμός", font=("Arial", 14), bg='#2E2E2E', fg="white", width=15)
    instruction_header = tk.Label(left_frame, text="Εντολή", font=("Arial", 14), bg='#2E2E2E', fg="white", width=15)
    registers_header = tk.Label(left_frame, text="Καταχωρητές", font=("Arial", 14), bg='#2E2E2E', fg="white", width=15)
    action_header = tk.Label(left_frame, text="Ενέργεια", font=("Arial", 14), bg='#2E2E2E', fg="white", width=15)

    number_header.grid(row=3, column=0, sticky="w")
    instruction_header.grid(row=3, column=1)
    registers_header.grid(row=3, column=2)
    action_header.grid(row=3, column=3)

    # Frame to hold the dynamic rows for the added commands
    command_frame = tk.Frame(left_frame, bg='#2E2E2E')
    command_frame.grid(row=4, column=0, columnspan=5, pady=10)

    # List to keep track of the command boxes
    command_boxes = []

    # Function to create dynamic rows based on the length of Instr_Cache
    def create_dynamic_rows_from_cache():
        Instr_Cache = gui_vars.Instr_Cache  # Access Instr_Cache
        num_commands = len(Instr_Cache)  # Determine how many rows to create

        # Clear existing rows
        for widget in command_frame.winfo_children():
            widget.destroy()

        for i in range(num_commands):
            number_label = tk.Label(command_frame, text=str(i + 1), font=("Arial", 14), bg='#2E2E2E', fg="white", width=10)
            instruction_box = tk.Label(command_frame, text="", font=("Arial", 14), bg="lightgray", width=10, height=2, relief="solid")
            instruction_box1 = tk.Label(command_frame, text="", font=("Arial", 14), bg="lightgray", width=10, height=2, relief="solid")

            small_box1 = tk.Label(command_frame, text="", font=("Arial", 10), bg="lightgray", width=8, height=1, relief="solid")
            small_box2 = tk.Label(command_frame, text="", font=("Arial", 10), bg="lightgray", width=8, height=1, relief="solid")
            small_box3 = tk.Label(command_frame, text="", font=("Arial", 10), bg="lightgray", width=8, height=1, relief="solid")

            delete_button = tk.Button(command_frame, text="Delete", font=("Arial", 10), bg="red", fg="white", command=lambda index=i: delete_row(index))
            delete_button.bind("<Enter>", on_enter_delete)
            delete_button.bind("<Leave>", on_leave_delete)

            number_label.grid(row=i + 1, column=0,sticky="w")
            instruction_box.grid(row=i + 1, column=1)
            small_box1.grid(row=i + 1, column=2, sticky='w')
            small_box2.grid(row=i + 1, column=3, sticky='w')
            small_box3.grid(row=i + 1, column=4, sticky='w')
            delete_button.grid(row=i + 1, column=5)

            # Bind the boxes to their respective functions
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

            command_boxes.append((instruction_box, instruction_box1, small_box1, small_box2, small_box3))

            # Automatically populate the rows with the instructions from Instr_Cache
            instr_obj = Instr_Cache[i]
            instruction_box.config(text=instr_obj.name)
            small_box1.config(text=namestr(instr_obj.r1, globals()) if instr_obj.r1 != none else "None")
            small_box2.config(text=namestr(instr_obj.r2, globals()) if instr_obj.r2 != none else "None")
            small_box3.config(text=namestr(instr_obj.r3, globals()) if instr_obj.r3 != none else "None")

    # Function to delete a row
    def delete_row(index):
        Instr_Cache = gui_vars.Instr_Cache
        Instr_Cache.pop(index)
        create_dynamic_rows_from_cache()

    # Modify the add button's command to take the number of rows from the input field
    def add_rows():
        Instr_Cache = gui_vars.Instr_Cache
        try:
            num_to_add = int(command_input.get())
            for _ in range(num_to_add):
                # Create a new blank instruction and add to Instr_Cache
                new_instruction = Instruction("N/A", "0000000", none, none, none, none)
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
            elif button1_window.box_type == "register" and text in ["r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7"]:
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
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = none  # No third register

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text="None")

            elif instruction_text and instruction_text1 in ["STORE"]:

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")

                # Only require reg1 and reg2, and set reg3 to None
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = none  # No third register

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text="None")

            elif instruction_text and instruction_text1 in ["ADD"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text=reg3_text if reg3_text else "None")

            elif instruction_text and instruction_text1 in ["AND"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text=reg3_text if reg3_text else "None")

            elif instruction_text and instruction_text1 in ["SUB"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text=reg3_text if reg3_text else "None")

            elif instruction_text and instruction_text1 in ["BRE"]:  # Instructions that take three registers

                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = r1 if reg1_text == "r1" else r2 if reg1_text == "r2" else r3 if reg1_text == "r3" else r4
                Instr_Cache[i].r2 = r1 if reg2_text == "r1" else r2 if reg2_text == "r2" else r3 if reg2_text == "r3" else r4
                Instr_Cache[i].r3 = r1 if reg3_text == "r1" else r2 if reg3_text == "r2" else r3 if reg3_text == "r3" else r4

                # Update UI to show the updated instruction
                instruction_box.config(text=Instr_Cache[i].name)
                small_box1.config(text=reg1_text)
                small_box2.config(text=reg2_text)
                small_box3.config(text=reg3_text if reg3_text else "None")

            elif instruction_text and instruction_text1 in ["NOP"]:
                # Get the opcode for the instruction
                opcode = opcode_mapping.get(instruction_text1, "unknown")
                Instr_Cache[i].opcode = opcode
                Instr_Cache[i].name = instruction_text
                Instr_Cache[i].r1 = none  # No first register
                Instr_Cache[i].r2 = none  # No second register
                Instr_Cache[i].r3 = none  # No third register


    # Right column: Headers and buttons
    right_header1 = tk.Label(right_frame, text="Προσθήκη Εντολών", font=("Arial", 18), bg='#2E2E2E', fg="white")
    right_header1.grid(row=0, column=2, columnspan=2, pady=10)

    load_button = tk.Button(right_frame, text="LOAD", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("LOAD"))
    load_button.bind("<Enter>", on_enter_instr)
    load_button.bind("<Leave>", on_leave_instr)
    store_button = tk.Button(right_frame, text="STORE", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("STORE"))
    store_button.bind("<Enter>", on_enter_instr)
    store_button.bind("<Leave>", on_leave_instr)
    add_instr_button = tk.Button(right_frame, text="ADD", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("ADD"))
    add_instr_button.bind("<Enter>", on_enter_instr)
    add_instr_button.bind("<Leave>", on_leave_instr)
    sub_instr_button = tk.Button(right_frame, text="SUB", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("SUB"))
    sub_instr_button.bind("<Enter>", on_enter_instr)
    sub_instr_button.bind("<Leave>", on_leave_instr)
    and_instr_button = tk.Button(right_frame, text="AND", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("AND"))
    and_instr_button.bind("<Enter>", on_enter_instr)
    and_instr_button.bind("<Leave>", on_leave_instr)
    bre_instr_button = tk.Button(right_frame, text="BRE", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("BRE"))
    bre_instr_button.bind("<Enter>", on_enter_instr)
    bre_instr_button.bind("<Leave>", on_leave_instr)

    if choose == 0:
        nop_button = tk.Button(right_frame, text="NOP", font=("Arial", 14), width=10, height=2, command=lambda: insert_text_in_box("NOP"))
        nop_button.bind("<Enter>", on_enter_instr)
        nop_button.bind("<Leave>", on_leave_instr)
        nop_button.grid(row=1, column=6, pady=5)

    load_button.grid(row=1, column=0, pady=5)
    store_button.grid(row=1, column=1, pady=5)
    add_instr_button.grid(row=1, column=2, pady=5)
    sub_instr_button.grid(row=1, column=3, pady=5)
    and_instr_button.grid(row=1, column=4, pady=5)
    bre_instr_button.grid(row=1, column=5, pady=5)

    # Adding a new header and buttons for registers
    register_header = tk.Label(right_frame, text="Προσθήκη Καταχωρητών", font=("Arial", 18), bg='#2E2E2E', fg="white")
    register_header.grid(row=2, column=0, columnspan=3, pady=10)

    r0_button = tk.Button(right_frame, text="r0", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r0"))
    r0_button.bind("<Enter>", on_enter_instr)
    r0_button.bind("<Leave>", on_leave_instr)
    r1_button = tk.Button(right_frame, text="r1", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r1"))
    r1_button.bind("<Enter>", on_enter_instr)
    r1_button.bind("<Leave>", on_leave_instr)
    r2_button = tk.Button(right_frame, text="r2", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r2"))
    r2_button.bind("<Enter>", on_enter_instr)
    r2_button.bind("<Leave>", on_leave_instr)
    r3_button = tk.Button(right_frame, text="r3", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r3"))
    r3_button.bind("<Enter>", on_enter_instr)
    r3_button.bind("<Leave>", on_leave_instr)
    r4_button = tk.Button(right_frame, text="r4", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r4"))
    r4_button.bind("<Enter>", on_enter_instr)
    r4_button.bind("<Leave>", on_leave_instr)
    r5_button = tk.Button(right_frame, text="r5", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r5"))
    r5_button.bind("<Enter>", on_enter_instr)
    r5_button.bind("<Leave>", on_leave_instr)
    r6_button = tk.Button(right_frame, text="r6", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r6"))
    r6_button.bind("<Enter>", on_enter_instr)
    r6_button.bind("<Leave>", on_leave_instr)
    r7_button = tk.Button(right_frame, text="r7", font=("Arial", 14), width=5, height=2, command=lambda: insert_text_in_box("r7"))
    r7_button.bind("<Enter>", on_enter_instr)
    r7_button.bind("<Leave>", on_leave_instr)

    r0_button.grid(row=3, column=0, pady=5)
    r1_button.grid(row=3, column=1, pady=5)
    r2_button.grid(row=3, column=2, pady=5)
    r3_button.grid(row=3, column=3, pady=5)
    r4_button.grid(row=4, column=0, pady=5)
    r5_button.grid(row=4, column=1, pady=5)
    r6_button.grid(row=4, column=2, pady=5)
    r7_button.grid(row=4, column=3, pady=5)

    # Button to append instructions to Instr_Cache and display them in rows
    append_button = tk.Button(content_frame, text="Καταχώρηση Εντολών", font=("Arial", 14), fg="#FFFFFF", bg= "#61afef", activebackground="#4fa3e2", activeforeground="white", command=append_and_display)
    append_button.grid(row=2, column=0, columnspan=2, pady=10)
    append_button.bind("<Enter>", on_enter)
    append_button.bind("<Leave>", on_leave)

    # Exit button centered at the bottom of the content frame
    exit_button = tk.Button(content_frame, text="Έξοδος", font=("Arial", 14), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", command=lambda: show_root(menu_window, button1_window))
    exit_button.grid(row=3, column=0, columnspan=2, pady=10, sticky='s')
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

    button1_window.mainloop()