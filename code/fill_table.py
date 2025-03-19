# Functions to print "λ λ+1 λ+2..." in the table in the canvas

import re

from vars import counter_l

from gui_vars import position_x_l, Instr_Cache

index = 1
previous_max_x = 0
time = -10
result = 0

def find_max_x_in_first_row(canvas, screen_width, screen_height, tolerance=5):
    """
    Find the text with the largest X position in the first row.
    Adds tolerance to account for slight deviations in Y-coordinates.
    
    Parameters:
        canvas (Canvas): The Tkinter canvas to search.
        screen_width (int): Screen width for calculations (unused here).
        screen_height (int): Screen height for row calculations.
        tolerance (int): The acceptable deviation in Y-coordinate.
    
    Returns:
        float: The largest X position in the first row or 0 if no text is found.
    """
    first_row_y = screen_height / 7.4482
    max_x = 0

    # Define the list of texts to search for
    texts_to_search = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

    # Get all the items in the canvas
    items = canvas.find_all()

    # Iterate over all items and check for the texts in the first row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)

            # Check if the text is one of the specified texts and within the tolerance range of the first row
            if text in texts_to_search and abs(coords[1] - first_row_y) <= tolerance:
                # Update the max X position if this text's X is larger
                if max_x is None or coords[0] > max_x:
                    max_x = coords[0]

    return max_x  # Return its X position

def check_if_pipeline_texts_absent(canvas):
    """Check if any of the pipeline texts ('ΠΕ', 'ΑΕ', etc.) are present on the canvas."""
    # Define the list of texts to search for
    pipeline_texts = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

    # Get all the items in the canvas
    items = canvas.find_all()

    # Iterate over all items and check if any pipeline text is present
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            if text in pipeline_texts:
                return False  # Return False as soon as any pipeline text is found

    return True  # Return True if none of the pipeline texts were found

def periodL():
    global index

    if counter_l > len(Instr_Cache) + 4:
        pass
    else:
        x = "λ+" + str(index)
        return x

def periodL1(canvas, screen_width, screen_height, counter, z):
    global index, position_x_l, previous_max_x, time, result

    l_counter = 0

    # Find the maximum X position of the texts in the first row
    max_x = find_max_x_in_first_row(canvas, screen_width, screen_height)

    # Function to check if there is an "ΑΑ" at the given Y position
    def is_aa_at_position(canvas, screen_height):
        items = canvas.find_all()
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                tolerance = 0.01 * screen_height  # Define tolerance as 1% of screen height, adjust as needed
                if text == "ΑΑ" and abs(coords[1] - (screen_height / 7.4482)) <= tolerance:
                    return True
        return False    
    
    def delete_all_lambda_texts_above(canvas, screen_height, tolerance=0.1):
        """
        Deletes all texts in the canvas that start with 'λ' and have a y-coordinate < screen_height / 9.3913 (with a tolerance).

        Parameters:
            canvas (tk.Canvas): The canvas containing the text items.
            screen_height (float): The screen height to calculate the threshold.
            tolerance (float): A tolerance value to adjust the threshold comparison.
        """
        # Calculate the threshold with tolerance
        threshold = screen_height / 9.3913 - tolerance

        # Find all items in the canvas
        all_items = canvas.find_all()

        # Iterate over all items to find texts starting with "λ" and y-coordinate < threshold
        items_to_delete = [
            item for item in all_items
            if canvas.type(item) == "text"
            and canvas.itemcget(item, "text").startswith("λ")
            and canvas.coords(item)[1] < threshold
        ]

        # Delete the identified items
        for item in items_to_delete:
            canvas.delete(item)

        # print(f"Deleted {len(items_to_delete)} text(s) that start with 'λ' and have y < {threshold:.2f}.")

    def delete_and_move_lambda_texts(canvas, screen_width, screen_height):
        """
        Deletes text starting with 'λ' at specific coordinates and moves other texts starting with 'λ'
        on the same row to the left by screen_width / 38.4.
        """
        # Specific coordinates for deletion
        target_x = screen_width / 10.3783
        target_y = screen_height / 9.3913

        # Calculate the left shift distance
        shift_distance = screen_width / 38.4

        # Find all items in the canvas
        all_items = canvas.find_all()

        # Identify the item to delete and items to shift
        items_to_delete = []
        items_to_shift = []

        for item in all_items:
            # Only process text items
            if canvas.type(item) == "text":
                text_content = canvas.itemcget(item, "text")  # Get the text content
                coords = canvas.coords(item)  # Get the coordinates

                if text_content.startswith("λ"):
                    if abs(coords[0] - target_x) < 1 and abs(coords[1] - target_y) < 1:
                        # Mark this item for deletion
                        items_to_delete.append(item)
                    elif abs(coords[1] - target_y) < 1:
                        # Mark this item for shifting (same row, starts with "λ")
                        items_to_shift.append(item)

        # Delete the targeted text
        for item in items_to_delete:
            canvas.delete(item)

        # Shift other texts to the left
        for item in items_to_shift:
            coords = canvas.coords(item)
            new_x = coords[0] - shift_distance
            canvas.coords(item, new_x, coords[1])

        # print(f"Deleted {len(items_to_delete)} text(s) and moved {len(items_to_shift)} text(s).")

    def delete_all_lambda_texts(canvas):
        """
        Deletes all texts in the canvas that start with 'λ'.

        Parameters:
            canvas (tk.Canvas): The canvas containing the text items.
        """
        # Find all items in the canvas
        all_items = canvas.find_all()

        # Iterate over all items to find texts starting with "λ"
        items_to_delete = [
            item for item in all_items
            if canvas.type(item) == "text" and canvas.itemcget(item, "text").startswith("λ")
        ]


        # Delete the identified items
        for item in items_to_delete:
            canvas.delete(item)

        # print(f"Deleted {len(items_to_delete)} text(s) that start with 'λ'.")

    def find_lambda_text(canvas, screen_height, tolerance=20):
        """
        Finds the "ΠΕ" text in a specific row and retrieves the number from a "λ" text at the same x-coordinate.

        Parameters:
            canvas (tk.Canvas): The canvas containing the text items.
            screen_height (float): The screen height to calculate row coordinates.
            tolerance (float): A small tolerance for coordinate matching.

        Returns:
            int or None: The extracted number from the "λ" text, or None if no match is found.
        """
        # Calculate the target y-coordinate
        target_y = screen_height / 7.4482 + screen_height / 36

        # Find all items in the canvas
        all_items = canvas.find_all()

        # Tolerance bounds for Y-coordinate matching
        y_min = target_y - tolerance
        y_max = target_y + tolerance

        # Step 1: Find the first "ΠΕ" in the target row
        pe_coords_x = None
        for item in all_items:
            if canvas.type(item) == "text" and canvas.itemcget(item, "text") == "ΠΕ":
                coords = canvas.coords(item)
                # print(coords[1])
                if y_min <= coords[1] <= y_max:  # Check if y-coordinate matches the target
                    pe_coords_x = coords[0]  # Save the x-coordinate
                    # print(pe_coords_x)
                    break

        # If no "ΠΕ" found, return None
        if pe_coords_x is None:
            # print("No 'ΠΕ' found in the target row.")
            return None

        # Step 2: Find a text starting with "λ" at the same x-coordinate
        for item in all_items:
            if canvas.type(item) == "text":
                coords = canvas.coords(item)
                if abs(coords[0] - pe_coords_x) <= tolerance:  # Match x-coordinates with tolerance
                    text = canvas.itemcget(item, "text")
                    if text.startswith("λ"):
                        # Extract the number after "λ+"
                        match = re.match(r"λ\+(\d+)", text)
                        if match:
                            return int(match.group(1))

        # If no matching "λ" text is found, return None
        # print("No 'λ' text found at the same x-coordinate as 'ΠΕ'.")
        return None
        
    max_x = find_max_x_in_first_row(canvas, screen_width, screen_height)

    if check_if_pipeline_texts_absent(canvas):
        delete_all_lambda_texts(canvas)
    elif position_x_l > max_x + 1 + screen_width / 38.4:
        if result is not None:
            print(f"Extracted number: {result}")
            index = result
        else:
            print("No matching number found.")
        delete_all_lambda_texts(canvas)
        
        position_x_l = screen_width/10.3783
        while position_x_l < max_x + 1:
            canvas.create_text(position_x_l, screen_height / 9.3913, text=periodL(), font=("Arial", int(screen_width / 192), 'bold'))
            position_x_l += screen_width / 38.4
            index += 1
    elif counter == time:
        position_x_l = screen_width/10.3783 + 4*(screen_width/38.4)
        delete_and_move_lambda_texts(canvas, screen_width, screen_height)
        canvas.create_text(position_x_l, screen_height / 9.3913, text=periodL(), font=("Arial", int(screen_width / 192), 'bold'))
        position_x_l += screen_width / 38.4
        index += 1
    else:
        canvas.create_text(position_x_l, screen_height / 9.3913, text=periodL(), font=("Arial", int(screen_width / 192), 'bold'))
        position_x_l += screen_width / 38.4
        l_counter += 1
        index += 1
    
    # Increment index if "ΑΑ" is at the current position
    if is_aa_at_position(canvas, screen_height):
        time = counter + 1
        result = find_lambda_text(canvas, screen_height, tolerance=1)

    if counter == z - 1:
        index = 1
        position_x_l = screen_width/10.3783
        time = - 10
            
    previous_max_x = max_x # Update previous_max_x to the new max_x value
    delete_all_lambda_texts_above(canvas, screen_height, tolerance=0.1)