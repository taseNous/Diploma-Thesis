# Add set of instructions in the table in the bottom left canvas

import gui_vars, method, cycles, tkinter as tk
from instr import namestr

from vars import r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15

from gui_vars import position_y, current_y

from tkinter import messagebox

try:
    # Instr_Cache = cycles.Instr_Cache  # Assuming Instr_Cache is a list of Instruction objects
    entolh_index = 0
    next_instr = 0
    time = 0
    change_pe_flag = 0
    change_pe_flag1 = 0
    index = 0
    indexx = 0

    def applytoLabel():
        global entolh_index

        Instr_Cache = gui_vars.Instr_Cache  # Assuming Instr_Cache is a list of Instruction objects

        # print(entolh_index)
        if entolh_index > len(Instr_Cache) - 1:
            # print(f"Index {entolh_index} out of range.")
            return ""  # Return an empty string or handle the out-of-bounds case appropriately
        else:
            w = Instr_Cache[entolh_index]
            if w == "NOP":
                return w
            elif w.opcode in ["0010000", "0100000"]:
                r11 = namestr(w.r1, globals()) + ","
                r22 = "(" + namestr(w.r2, globals()) + ")"
                return f"{w.name} {r11} {r22}"
            elif w.opcode in ["0000001", "0000010", "0000011"]:
                r11 = namestr(w.r1, globals()) + ","
                r22 = namestr(w.r2, globals()) + ","
                r33 = namestr(w.r3, globals())
                return f"{w.name} {r11} {r22} {r33}"
            elif w.opcode in ["1110000"]:
                r11 = namestr(w.r1, globals()) + ","
                r22 = namestr(w.r2, globals()) + ","
                r33 = "d"
                return f"{w.name} {r11} {r22} {r33}"
            else:
                return w.name  # Default case if no match


    def applytoLabel1(canvas, screen_width, screen_height, z, i):
        global entolh_index, position_y, d, current_y, next_instr, time, change_pe_flag, change_pe_flag1, index, indexx

        choose = method.choose
        bre_index = cycles.bre_index
        bre_index_pred = cycles.bre_index_pred
        Instr_Cache = gui_vars.Instr_Cache
        d_value = cycles.d_value

        change_pe_flag = 0
        change_pe_flag1 = 0

        def is_aa_in_first_row():
            items = canvas.find_all()
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    tolerance = 0.01 * screen_height  # Define tolerance as 1% of screen height, adjust as needed
                    if text == "ΑΑ" and abs(coords[1] - (screen_height / 7.4482)) <= tolerance:
                        return True

            return False

        if i == 0:
            position_y = screen_height/7.4482
            entolh_index = 0
            next_instr = 0
            current_y = screen_height/7.4482
        
        def is_pe_in_row():
            # Define the Y position for the first row
            global current_y
            # print(current_y)
            # Get all items in the canvas
            items = canvas.find_all()

            # Check each item in the canvas to see if "ΠΕ" is in the first row
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    
                    # Check if the text is "ΠΕ" and it's at the current_y position
                    if text == "ΠΕ" and abs(coords[1] - current_y) < 1:
                        # Increment current_y and return True if "ΠΕ" is found
                        current_y += screen_height / 36
                        return True

            # Return False if "ΠΕ" is not found in the first row
            return False

        def delete_texts_in_first_row(canvas, screen_height):
            """Delete texts in the canvas with Y position in a specific range and excluding specific texts."""
            # Define the Y position range
            lower_y = screen_height / 9.3913
            upper_y = screen_height / 7.4482 + screen_height / 36.2
            
            # Define the list of texts to exclude from deletion
            excluded_texts = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

            # Get all items in the canvas
            items = canvas.find_all()

            # Iterate over all items to check their type, position, and content
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    
                    # Check if Y position is within the specified range and text is not excluded
                    if lower_y < coords[1] < upper_y and text not in excluded_texts:
                        canvas.delete(item)  # Delete the text item if it meets the criteria

        def delete_texts_under_bre(canvas, screen_height):
            """Delete the text in the canvas that is positioned one row below any text starting with 'BRE', excluding specific texts."""
            # Define the Y position offset for the row below
            y_offset = screen_height / 36

            # Define the list of texts to exclude from deletion
            excluded_texts = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

            # Get all items in the canvas
            items = canvas.find_all()
            bre_y = None

            # First, find the Y position of any text that starts with "BRE"
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    
                    if text.startswith("BRE"):
                        bre_y = coords[1]
                        break  # Exit loop once a "BRE" text is found

            # If a "BRE" text was found, calculate the Y position to delete
            if bre_y is not None:
                target_y = bre_y + y_offset

                # Iterate again over all items to find texts at target_y and delete them
                for item in items:
                    if canvas.type(item) == "text":
                        text = canvas.itemcget(item, "text")
                        coords = canvas.coords(item)
                        
                        # Delete any text at the target Y position if it's not in the excluded list
                        if abs(coords[1] - target_y) < 1 and text not in excluded_texts:
                            canvas.delete(item)

        def arrange_texts(canvas, screen_width, screen_height):
            """Ensure texts at a specific X position have consistent Y spacing in the first five rows, excluding 'εντολή'."""
            
            # Define the target X position and Y distance
            x_position = screen_width / 18.2857
            y_distance = screen_height / 36
            initial_y = screen_height / 7.4482  # Starting Y position for the first row

            # Get all items in the canvas
            items = canvas.find_all()

            # Collect relevant texts (excluding 'εντολή') at the target X position
            texts_to_adjust = []

            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    
                    # Include items at the specified X position, within the first five rows, and exclude "εντολή"
                    if abs(coords[0] - x_position) < 1 and coords[1] >= initial_y and text != "εντολή":
                        texts_to_adjust.append((item, coords[1]))  # Append item and its Y position

            # Sort texts by Y position to ensure they are processed in the correct order
            texts_to_adjust.sort(key=lambda x: x[1])

            # Adjust Y positions for consistent spacing
            for i, (item, current_y) in enumerate(texts_to_adjust):
                # Calculate the expected Y position based on its position in the list
                expected_y = initial_y + i * y_distance

                # If the current Y position is off, move it to the expected Y position
                if abs(current_y - expected_y) > 1:
                    canvas.coords(item, x_position, expected_y)

        def resolve_overlapping_texts(canvas, screen_width, screen_height):
            """Check for overlapping texts at a specific X position and move any that overlap."""
            
            # Define the target X position and Y distance
            target_x = screen_width / 18.2857
            y_distance = screen_height / 36

            # Get all items in the canvas
            items = canvas.find_all()

            # Collect relevant texts at the target X position, excluding "εντολή"
            texts_at_x = []
            
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    
                    # Include only texts at the target X position and exclude "εντολή"
                    if abs(coords[0] - target_x) < 1 and text != "εντολή":
                        texts_at_x.append((item, coords[1]))  # Store item and Y position

            # Sort texts by Y position to identify overlaps
            texts_at_x.sort(key=lambda x: x[1])

            # Adjust positions for overlapping texts
            for i in range(1, len(texts_at_x)):
                item, y_position = texts_at_x[i]
                prev_item, prev_y_position = texts_at_x[i - 1]
                
                # Check if the current text overlaps with the previous one
                if abs(y_position - prev_y_position) < y_distance:
                    # Move the current text down by y_distance to avoid overlap
                    new_y_position = prev_y_position + y_distance
                    canvas.coords(item, target_x, new_y_position)

        def move_texts_up():
            """Move texts up by screen_height / 36 if their X position is less than screen_width / 10.3783 and text is not 'εντολή'."""
            # Define the X position threshold
            x_threshold = screen_width / 10.3783
            y_offset = screen_height / 36  # Amount to move texts up

            # Get all items in the canvas
            items = canvas.find_all()

            # Iterate over each item and check if it meets the criteria for movement
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)

                    # Check if the X position is less than the threshold and the text is not "εντολή"
                    if coords[0] < x_threshold and text != "εντολή":
                        new_y = coords[1] - y_offset  # Calculate the new Y position
                        canvas.coords(item, coords[0], new_y)  # Update the item's position

        if i == time+1 and i>1:
            delete_texts_in_first_row(canvas, screen_height)
            move_texts_up()
            current_y -= screen_height / 36

        if is_aa_in_first_row():
            time = i

        if i-2 in bre_index:
                current_y -= screen_height / 36

        if choose == 1:
            if i == 0:
                index = 0
            if i-1 in bre_index:
                delete_texts_under_bre(canvas, screen_height)
                entolh_index += d_value[index] - 1
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif i in bre_index_pred:
                entolh_index += d_value[index]
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1
        
            elif is_pe_in_row():
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                position_y += screen_height/36
                entolh_index += 1

            if i > 2:
                resolve_overlapping_texts(canvas, screen_width, screen_height)
                arrange_texts(canvas, screen_width, screen_height)
                
        if choose == 2:

            if i == 0:
                index = 0
            if i-1 in bre_index:
                print("d_value")
                print(d_value)
                delete_texts_under_bre(canvas, screen_height)
                entolh_index += d_value[index] - 1
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif i in bre_index_pred:
                entolh_index += d_value[index]
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif is_pe_in_row():
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                position_y += screen_height/36
                entolh_index += 1

            if i > 2:
                resolve_overlapping_texts(canvas, screen_width, screen_height)
                arrange_texts(canvas, screen_width, screen_height)
        
        if choose == 3:

            if i == 0:
                index = 0
                print("ioanna1")
            if i-1 in bre_index:
                delete_texts_under_bre(canvas, screen_height)
                entolh_index += d_value[index] - 1
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif i in bre_index_pred:
                entolh_index += d_value[index]
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif is_pe_in_row():
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                position_y += screen_height/36
                entolh_index += 1

            if i > 2:
                resolve_overlapping_texts(canvas, screen_width, screen_height)
                arrange_texts(canvas, screen_width, screen_height)

        if choose == 4:

            if i == 0:
                index = 0
                print("ioanna")
            if i-1 in bre_index:
                delete_texts_under_bre(canvas, screen_height)
                entolh_index += d_value[index] - 1
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif i in bre_index_pred:
                entolh_index += d_value[index]
                index += 1
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                
                try:
                    # Check if entolh_index will exceed the bounds of Instr_Cache
                    if entolh_index >= len(Instr_Cache):
                        # Open the file in write mode, which will truncate (clear) the file
                        with open("Log.txt", "w") as file:
                            pass  # Do nothing, just open and close to clear the file
                        # Display an error message and exit if it exceeds
                        root = tk.Tk()
                        root.withdraw()  # Hide the root window
                        messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                        root.destroy()
                        exit()

                except IndexError:
                    # Additional safety net if entolh_index somehow goes out of bounds
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Cache Error", "You have exceeded the Memory Cache")
                    root.destroy()
                    exit()

                entolh_index += 1

            elif is_pe_in_row():
                label_text = applytoLabel()
                if label_text == "":
                    pass  # Exit loop if out-of-bounds was encountered in applytoLabel
                canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
                position_y += screen_height/36
                entolh_index += 1

            if i > 2:
                resolve_overlapping_texts(canvas, screen_width, screen_height)
                arrange_texts(canvas, screen_width, screen_height)

        if is_pe_in_row():
            indexx += 1

except Exception as e:
    print(f"An error occurred: {e}")