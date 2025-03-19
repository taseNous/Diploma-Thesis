# Show pipeline stages in the table in the bottom left canvas

import gui_vars, dependencies, cycles

from vars import index1, index2, index3, index4, index5, index6, index8, index7

from gui_vars import (position_x1, position_x2, position_x3, position_x4, position_x5,
                      position_y1, position_y2, position_y3, position_y4, position_y5)

pe_flag = -1
ae_flag = -1
ep_flag = -1
pm_flag = -1
aa_flag = -1
index = 0
arrow = None
arrow1 = None
arrow2 = None
arrow3 = None
arrow4 = None

# Move texts in first row to the left
def move_texts_if_pe_condition_met(canvas, screen_width, screen_height):
    global position_x1, position_x2, position_x3, position_x4, position_x5

    # Check if "ΠΕ" is in the first row (Y = screen_height / 7.4482) but not at X = screen_width / 10.3783
    items = canvas.find_all()
    first_pe_coords = None
    pe_count = 0

    # Find the first "ΠΕ" in the first row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            if text == "ΠΕ" and coords[1] == screen_height / 7.4482:
                pe_count += 1
                if pe_count == 1:
                    first_pe_coords = coords
                elif pe_count > 1:
                    continue  # Ignore any additional "ΠΕ" texts

    # If the first "ΠΕ" is not in the correct X position
    if first_pe_coords and first_pe_coords[0] != screen_width / 10.3783:
        move_by_x = screen_width / 10.3783 - first_pe_coords[0]  # Difference from current "ΠΕ" X position to the new one
        texts_to_move = ["ΠΕ", "ΑΕ", "ΑΕ'", "ΕΠ", "ΠΜ", "ΑΑ", "Χ"]

        # Dictionary to map texts to their corresponding position_x variables
        position_map = {
            "ΠΕ": "position_x1",
            "Χ": "position_x2",
            "ΑΕ": "position_x2",
            "ΑΕ'": "position_x2",
            "ΕΠ": "position_x3",
            "ΠΜ": "position_x4",
            "ΑΑ": "position_x5"
        }

        # Move the texts in the first row and update their position_x values
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                if text in texts_to_move and coords[1] == screen_height / 7.4482:
                    new_x = screen_width / 10.3783 + texts_to_move.index(text) * (screen_width / 38.4)
                    canvas.coords(item, new_x, coords[1])
                    
                    # Update the position_x variables according to the text
                    if text in position_map:
                        globals()[position_map[text]] = new_x

        # Now move the texts in the next four rows by the same X adjustment
        for row_offset in range(1, 10):
            for item in items:
                if canvas.type(item) == "text":
                    text = canvas.itemcget(item, "text")
                    coords = canvas.coords(item)
                    if text in texts_to_move and coords[1] == screen_height / 7.4482 + row_offset * (screen_height / 36):
                        new_x = coords[0] + move_by_x  # Shift by the same amount as the first row
                        canvas.coords(item, new_x, coords[1])
                        
                        # Update position_x for texts in subsequent rows if needed
                        if text in position_map:
                            globals()[position_map[text]] = new_x

def check_and_move_pe_below_ae_if_needed1(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Iterate through each row, checking for "ΑΕ" in row i and adjusting "ΠΕ" in row i+1
    for row_index in range(len(row_heights) - 1):  # Exclude the last row since there's no i+1 row
        current_row_y = row_heights[row_index]
        next_row_y = row_heights[row_index + 1]

        # Collect texts and their X positions for the current row and the next row
        current_row_texts = {}
        next_row_texts = []

        # Get all items in the canvas
        items = canvas.find_all()

        # Flags to indicate if there's "BRE" or "ΠΜ" text in the current row
        has_bre_in_row = False
        pm_x = None  # X position of "ΠΜ" in the current row if it exists

        # Populate text positions for the current row and the next row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                
                # Check if text is in the current row
                if abs(coords[1] - current_row_y) < 1:
                    current_row_texts[text] = (item, coords[0], coords[1])  # (item, x, y)
                    
                    # Check if there's any text that starts with "BRE"
                    if text.startswith("BRE"):
                        has_bre_in_row = True  # Set the flag if "BRE" is found in the current row
                    
                    # Track the X position of "ΠΜ" if it exists in the current row
                    if text == "ΠΜ":
                        pm_x = coords[0]

                # Check if text is "ΠΕ" in the next row
                elif abs(coords[1] - next_row_y) < 1 and text == "ΠΕ":
                    next_row_texts.append((item, coords[0], coords[1]))  # Store each "ΠΕ" found in next row

        # If "ΑΕ" is in the current row and there's no "BRE", proceed to move "ΠΕ" below "ΑΕ"
        if "ΑΕ" in current_row_texts and not has_bre_in_row:
            ae_x = current_row_texts["ΑΕ"][1]  # X position of "ΑΕ" in the current row
            new_y = current_row_texts["ΑΕ"][2] + screen_height / 36  # Y position directly below "ΑΕ"

            # Move only the first "ΠΕ" in the next row, leave any others in their current positions
            if next_row_texts:
                first_pe_item = next_row_texts[0][0]  # Get the canvas item for the first "ΠΕ"
                canvas.coords(first_pe_item, ae_x, new_y)  # Move first "ΠΕ" to the same X as "ΑΕ" and adjusted Y

def check_and_move_overlap(canvas, screen_width):
    items = canvas.find_all()
    text_labels = [item for item in items if canvas.type(item) == "text"]
    
    for i in range(len(text_labels)):
        for j in range(i + 1, len(text_labels)):
            # Get the bounding boxes of two text labels
            bbox1 = canvas.bbox(text_labels[i])  # (x1, y1, x2, y2) of first label
            bbox2 = canvas.bbox(text_labels[j])  # (x1, y1, x2, y2) of second label
            
            # Check for overlap
            if bbox1 and bbox2 and (
                bbox1[2] > bbox2[0] and  # right of bbox1 > left of bbox2
                bbox1[0] < bbox2[2] and  # left of bbox1 < right of bbox2
                bbox1[3] > bbox2[1] and  # bottom of bbox1 > top of bbox2
                bbox1[1] < bbox2[3]      # top of bbox1 < bottom of bbox2
            ):
                # Move the overlapping text to the right by screen_width / 38.4
                current_coords = canvas.coords(text_labels[j])
                new_x = current_coords[0] + screen_width / 38.4  # Shift the text to the right
                canvas.coords(text_labels[j], new_x, current_coords[1])

                # Update position_x variables if needed
                text = canvas.itemcget(text_labels[j], "text")
                if text == "ΠΕ" or text == "X":
                    position_x1 = new_x
                elif text == "ΑΕ":
                    position_x2 = new_x
                elif text == "ΕΠ":
                    position_x3 = new_x
                elif text == "ΠΜ":
                    position_x4 = new_x
                elif text == "ΑΑ":
                    position_x5 = new_x

def delete_texts_above_threshold(canvas, screen_height):
    items = canvas.find_all()
    texts_to_delete = ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ", "Χ", "ΑΕ'"]
    
    # Define the Y threshold above which texts will be deleted
    threshold_y = screen_height / 7.4482 - 1

    # Iterate over all the items on the canvas
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # If the text is in the list and is above the threshold, delete it
            if text in texts_to_delete and coords[1] < threshold_y:
                canvas.delete(item)

def adjust_pe_and_other_positions(canvas, screen_width):
    items = canvas.find_all()
    row_texts = []
    row_y_positions = []

    # Define the texts to move along with "ΠΕ"
    texts_to_move = ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ", "X"]
    blocking_texts = ["ΑΕ'", "Χ"]  # These texts prevent movement

    # First, collect all texts of interest ("ΠΕ", "ΑΕ", etc.) and their positions
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            if text in texts_to_move or text in blocking_texts:
                coords = canvas.coords(item)
                row_texts.append((item, text, coords[0], coords[1]))  # (item, text, x, y)
                row_y_positions.append(coords[1])

    # Sort the texts by their Y position (row) to process row by row
    row_texts.sort(key=lambda x: x[3])  # Sort by Y position (row order)

    # Now, check each row and adjust positions
    for i in range(len(row_texts) - 1):
        # Get the current row's texts
        current_row_texts = [t for t in row_texts if t[3] == row_texts[i][3]]
        next_row_texts = [t for t in row_texts if t[3] == row_texts[i + 1][3]]
        
        # Check if "ΑΕ'" or "Χ" exists in the current row
        current_row_has_blocking_text = any(t[1] in blocking_texts for t in current_row_texts)

        # Find "ΠΕ" in the current and next rows
        current_pe = next((t for t in current_row_texts if t[1] == "ΠΕ"), None)
        next_pe = next((t for t in next_row_texts if t[1] == "ΠΕ"), None)

        if current_pe and next_pe and not current_row_has_blocking_text:
            current_x, current_y = current_pe[2], current_pe[3]
            next_x, next_y = next_pe[2], next_pe[3]

            # Check if the "ΠΕ" in the next row is more than screen_width / 38.4 units away
            expected_distance = screen_width / 38.4
            if next_x - current_x > expected_distance:
                # Calculate the new X position for the next row's texts
                move_by_x = current_x + expected_distance - next_x

                # Move all texts in the next row by the same amount
                for text_item in next_row_texts:
                    new_x = text_item[2] + move_by_x
                    canvas.coords(text_item[0], new_x, text_item[3])  # Update the position on the canvas

                    # Update global variables (for the corresponding text)
                    global_vars = {
                        "ΠΕ": "position_x1",
                        "ΑΕ": "position_x2",
                        "ΑΕ'": "position_x2",
                        "ΕΠ": "position_x3",
                        "ΠΜ": "position_x4",
                        "ΑΑ": "position_x5",
                        "X": "position_x2"  # Assuming "X" uses the same X as "ΠΕ"
                    }
                    if text_item[1] in global_vars:
                        globals()[global_vars[text_item[1]]] = new_x

def check_for_ae_and_x(canvas):
    items = canvas.find_all()
    # Iterate through all the items on the canvas
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            # Check if the text is either "ΑΕ'" or "Χ"
            if text == "ΑΕ'" or text == "Χ":
                return True  # Return False if either text is found
    return False  # Return True if neither "ΑΕ'" nor "Χ" is found

def rearrange_existing_texts(canvas, screen_width, screen_height):
    # Define the expected texts to arrange
    texts_to_arrange = [
        ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"],  # 1st row
        ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ"],        # 2nd row
        ["ΠΕ", "ΑΕ", "ΕΠ"],              # 3rd row
        ["ΠΕ", "ΑΕ"],                    # 4th row
        ["ΠΕ"]                           # 5th row
    ]
    
    # Define the initial positions
    start_x = screen_width / 10.3783  # Starting X position
    start_y = screen_height / 7.4482  # Starting Y position
    x_distance = screen_width / 38.4  # Distance between texts in X direction
    y_distance = screen_height / 36   # Distance between rows in Y direction

    # Get all the existing text items on the canvas
    items = canvas.find_all()

    # Dictionary to map text names to their canvas item IDs
    text_items = {text: [] for row in texts_to_arrange for text in row}

    # Collect all items that match the text names we need to rearrange
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            if text in text_items:
                text_items[text].append(item)

    # Re-arrange the texts row by row
    for row_index, row_texts in enumerate(texts_to_arrange):
        # Calculate the Y position for this row
        row_y = start_y + row_index * y_distance
        
        # Calculate the starting X position for this row
        row_x = start_x + row_index * x_distance  # Shift the starting X position for each row
        
        # Loop through each expected text in the row and position it
        for text in row_texts:
            # Get the first available item for the current text and place it
            if text_items[text]:
                item = text_items[text].pop(0)  # Use the first available item and remove it from the list
                canvas.coords(item, row_x, row_y)  # Update the coordinates of the existing text
                
                # Move the X position for the next text in the row
                row_x += x_distance

def check_and_rearrange_texts_in_rows(canvas, screen_width, screen_height):
    # Define the valid text sequences to check and arrange
    valid_sequences = [
        ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"],
        ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"],
        ["ΠΕ", "ΑΕ'", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]
    ]
    
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Define the expected X distance between texts
    x_distance = screen_width / 38.4

    # Iterate over each row height and check the texts in that row
    for row_y in row_heights:
        # Get all items in the current row
        items = canvas.find_all()
        text_positions = {}

        # Find the texts in the current row and their positions
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                # Only consider texts in the current row (based on Y position)
                if abs(coords[1] - row_y) < 1:
                    text_positions[text] = (item, coords[0], coords[1])  # Store item, x, and y

        # Try to identify the correct sequence in this row
        identified_sequence = None
        for sequence in valid_sequences:
            # If all the texts in the sequence are present in the row, mark it as the identified sequence
            if all(text in text_positions for text in sequence):
                identified_sequence = sequence
                break
        
        # If we have identified a valid sequence in this row, we proceed to rearrange if needed
        if identified_sequence:
            # Extract the texts and their x positions
            positions = [(text_positions[text][0], text_positions[text][1]) for text in identified_sequence]
            
            # Sort the texts by their current X position (to check the order)
            positions.sort(key=lambda x: x[1])

            # Check the distances between the texts and re-arrange if necessary
            for i in range(len(positions) - 1):
                current_x = positions[i][1]
                next_x = positions[i + 1][1]
                
                # Only rearrange if the distance is bigger than the expected distance
                if next_x - current_x > x_distance:
                    new_x = current_x + x_distance
                    canvas.coords(positions[i + 1][0], new_x, row_y)  # Update position in the same row

def check_and_move_pe(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Expected distance between two rows in terms of Y
    y_distance = screen_height / 36
    
    # Expected shift in X position
    x_distance = screen_width / 38.4
    
    # Iterate through the rows to check for "ΠΕ" in consecutive rows
    for row_index in range(len(row_heights) - 1):
        current_row_y = row_heights[row_index]
        next_row_y = row_heights[row_index + 1]
        
        # Find "ΠΕ" in the current row
        current_pe = None
        next_pe = None
        
        # Get all items in the canvas
        items = canvas.find_all()
        
        # Find "ΠΕ" in the current row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                # Check for "ΠΕ" in the current row
                if text == "ΠΕ" and abs(coords[1] - current_row_y) < 1:
                    current_pe = (item, coords[0], coords[1])
                # Check for "ΠΕ" in the next row
                elif text == "ΠΕ" and abs(coords[1] - next_row_y) < 1:
                    next_pe = (item, coords[0], coords[1])
        
        # If both "ΠΕ"s are found in current and next rows
        if current_pe and next_pe:
            current_x, current_y = current_pe[1], current_pe[2]
            next_x, next_y = next_pe[1], next_pe[2]
            
            # Check if the next "ΠΕ" is located exactly + screen_height/36 from the current one
            # And check if they are in the same X position
            if abs(next_y - current_y - y_distance) < 1 and abs(next_x - current_x) < 1:
                # Move the "ΠΕ" in row i+1 to the right by screen_width / 38.4
                new_x = next_x + x_distance
                canvas.coords(next_pe[0], new_x, next_y)  # Update the position on the canvas

def check_and_move_pe_below_ae_if_needed(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Iterate through each row, checking for "ΑΕ" in row i and adjusting "ΠΕ" in row i+1
    for row_index in range(len(row_heights) - 1):  # Exclude the last row since there's no i+1 row
        current_row_y = row_heights[row_index]
        next_row_y = row_heights[row_index + 1]

        # Collect texts and their X positions for the current row and the next row
        current_row_texts = {}
        next_row_texts = []

        # Get all items in the canvas
        items = canvas.find_all()

        # Populate text positions for the current row and the next row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                if abs(coords[1] - current_row_y) < 1:  # Check if text is in the current row
                    current_row_texts[text] = (item, coords[0], coords[1])  # (item, x, y)
                elif abs(coords[1] - next_row_y) < 1 and text == "ΠΕ":  # Check if text is "ΠΕ" in the next row
                    next_row_texts.append((item, coords[0], coords[1]))  # Store each "ΠΕ" found in next row

        # Check if the current row has "ΑΕ"
        if "ΑΕ" in current_row_texts:
            ae_x = current_row_texts["ΑΕ"][1]  # X position of "ΑΕ" in the current row
            new_y = current_row_texts["ΑΕ"][2] + screen_height / 36  # Y position directly below "ΑΕ"

            # Move only the first "ΠΕ" in the next row, leave any others in their current positions
            if next_row_texts:
                first_pe_item = next_row_texts[0][0]  # Get the canvas item for the first "ΠΕ"
                canvas.coords(first_pe_item, ae_x, new_y)  # Move first "ΠΕ" to the same X as "ΑΕ" and adjusted Y




def check_and_move_leftmost_pe(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Iterate through each row, checking the positions of "ΠΕ" in row i and i+1
    for row_index in range(len(row_heights) - 1):  # Exclude the last row since there's no i+1 row
        current_row_y = row_heights[row_index]
        next_row_y = row_heights[row_index + 1]

        # Collect all "ΠΕ" texts and their X positions for the current row and the next row
        current_pe = None
        next_pe = None

        # Get all items in the canvas
        items = canvas.find_all()

        # Populate "ΠΕ" positions for the current row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                if text == "ΠΕ":
                    if abs(coords[1] - current_row_y) < 1:  # Check if "ΠΕ" is in the current row
                        current_pe = (item, coords[0], coords[1])  # (item, x, y)
                    elif abs(coords[1] - next_row_y) < 1:  # Check if "ΠΕ" is in the next row
                        next_pe = (item, coords[0], coords[1])  # (item, x, y)

        # If both "ΠΕ" texts are found in row i and row i+1
        if current_pe and next_pe:
            current_pe_x = current_pe[1]  # X position of "ΠΕ" in the current row
            next_pe_x = next_pe[1]        # X position of "ΠΕ" in the next row

            # If the "ΠΕ" in row i+1 is placed more left than the one in row i
            if next_pe_x < current_pe_x:
                pe_item = next_pe[0]
                new_x = current_pe_x + screen_width / 38.4  # Shift "ΠΕ" to the right
                new_y = current_pe[2] + screen_height / 36   # Move "ΠΕ" below the current row's "ΠΕ"
                canvas.coords(pe_item, new_x, new_y)  # Update the position of "ΠΕ" in row i+1

def check_and_move_ae_right_of_pe(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]

    # Iterate through each row, checking the positions of "ΠΕ" and "ΑΕ"
    for row_y in row_heights:
        pe_item = None
        ae_item = None
        pe_x = None
        ae_x = None

        # Get all items in the canvas
        items = canvas.find_all()

        # Search for "ΠΕ" and "ΑΕ" in the current row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                if abs(coords[1] - row_y) < 1:  # Check if the text is in the current row
                    if text == "ΠΕ":
                        pe_item = item
                        pe_x = coords[0]  # X position of "ΠΕ"
                    elif text == "ΑΕ":
                        ae_item = item
                        ae_x = coords[0]  # X position of "ΑΕ"

        # If both "ΠΕ" and "ΑΕ" are found in the row
        if pe_item and ae_item:
            # If "ΑΕ" is placed more to the left than "ΠΕ"
            if ae_x < pe_x:
                # Move "ΑΕ" to the right of "ΠΕ"
                new_x = pe_x + screen_width / 38.4  # Shift "ΑΕ" to the right of "ΠΕ"
                canvas.coords(ae_item, new_x, row_y)  # Move "ΑΕ" to the new position, keeping the same Y

def check_and_adjust_text_spacing_without_ae_prime(canvas, screen_width, screen_height):
    # Define the Y positions for the 5 rows
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # The expected sequence and the X distance between the texts
    expected_texts = ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]
    x_distance = screen_width / 38.4  # The required distance between texts
    
    # Iterate through each row, checking for the presence and distance of the expected texts
    for row_y in row_heights:
        text_positions = {}
        ae_prime_found = False

        # Get all items in the canvas
        items = canvas.find_all()

        # Collect positions of the expected texts in the current row and check for "ΑΕ'"
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                if abs(coords[1] - row_y) < 1:  # Check if the text is in the current row
                    if text == "ΑΕ'":
                        ae_prime_found = True  # Mark that "ΑΕ'" is found
                        break  # Skip the rest of this row
                    if text in expected_texts:
                        text_positions[text] = (item, coords[0], coords[1])  # Store item and X, Y coordinates

        # If "ΑΕ'" is found in the row, skip it
        if ae_prime_found:
            continue

        # Check if all expected texts are present in the row
        if all(text in text_positions for text in expected_texts):
            # Sort the texts by their correct order: "ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"
            sorted_texts = [text_positions[text] for text in expected_texts]
            
            # Get the X position of the first text ("ΠΕ")
            current_x = sorted_texts[0][1]

            # Check and adjust the position of the remaining texts
            for i in range(1, len(sorted_texts)):
                item, x, y = sorted_texts[i]
                expected_x = current_x + x_distance  # Expected X position for the next text
                
                # If the text is too far to the right, move it to the correct position
                if x > expected_x:
                    canvas.coords(item, expected_x, y)  # Move the text to the correct position
                
                # Update the current X to the newly placed text's X
                current_x = expected_x

def adjust_ae_and_shift_texts(canvas, screen_width, screen_height):
    # Define the Y position for the second row
    row_y = screen_height / 7.4482 + screen_height / 36
    
    # Define the sequence of texts and the required X distance between "ΠΕ" and "ΑΕ"
    sequence = ["ΠΕ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]  # Sequence without "Χ" or "ΑΕ'"
    x_distance = screen_width / 38.4

    # Get all items in the canvas
    items = canvas.find_all()

    # Dictionary to store positions of found texts in the second row
    found_text_positions = {}

    # Check if the row contains "ΑΕ'" or "Χ"
    has_ae_prime_or_x = False

    # Collect items only in the second row and store positions of relevant texts
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Only consider texts in the second row (based on Y position)
            if abs(coords[1] - row_y) < 1:
                # If the row contains "ΑΕ'" or "Χ", set the flag and stop further checks
                if text == "ΑΕ'" or text == "Χ":
                    has_ae_prime_or_x = True
                    break
                # Store relevant text positions if they match the sequence
                if text in sequence:
                    found_text_positions[text] = (item, coords[0], coords[1])  # Store item, x, and y

    # Only proceed if "ΑΕ'" and "Χ" are not present in the row
    if not has_ae_prime_or_x and "ΠΕ" in found_text_positions and "ΑΕ" in found_text_positions:
        # Extract positions for "ΠΕ" and "ΑΕ"
        pe_item, pe_x, pe_y = found_text_positions["ΠΕ"]
        ae_item, ae_x, ae_y = found_text_positions["ΑΕ"]

        # Calculate the expected X position for "ΑΕ"
        correct_ae_x = pe_x + x_distance

        # If "ΑΕ" is positioned too far to the right, adjust it and shift other texts
        if ae_x - pe_x > x_distance:
            shift_x = ae_x - correct_ae_x  # Calculate how much to shift left

            # Move "ΑΕ" to the correct position
            canvas.coords(ae_item, correct_ae_x, ae_y)

            # Shift remaining texts to the left by the same amount
            for text in sequence[2:]:  # Start from "ΕΠ" and move rightwards
                if text in found_text_positions:
                    item, text_x, text_y = found_text_positions[text]
                    new_x = text_x - shift_x
                    canvas.coords(item, new_x, text_y)  # Update the position on the canvas

def check_and_rearrange_first_row(canvas, screen_width, screen_height):
    # Define the target row height
    row_y = screen_height / 7.4482
    
    # Define the correct order of texts and spacing
    correct_order = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]
    x_distance = screen_width / 38.4

    # Get all items in the canvas
    items = canvas.find_all()

    # Dictionary to store positions of texts found in the first row
    found_text_positions = {}

    # Collect positions of relevant texts in the first row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Only consider texts in the first row based on Y position
            if abs(coords[1] - row_y) < 1 and text in correct_order:
                if text not in found_text_positions:
                    found_text_positions[text] = []
                found_text_positions[text].append((item, coords[0], coords[1]))  # Store multiple items if needed

    # Check for the condition with two "ΠΕ"s and one "Χ"
    if "ΠΕ" in found_text_positions and len(found_text_positions["ΠΕ"]) == 2 and "Χ" in found_text_positions:
        # Place the first "ΠΕ" at the starting X position
        first_pe_item, first_pe_x, first_pe_y = found_text_positions["ΠΕ"][0]
        position_x = screen_width / 10.3783
        canvas.coords(first_pe_item, position_x, row_y)

        # Position "Χ" to the right of the first "ΠΕ"
        x_item, _, _ = found_text_positions["Χ"][0]
        position_x += x_distance
        canvas.coords(x_item, position_x, row_y)

        # Position the second "ΠΕ" to the right of "Χ"
        second_pe_item, _, _ = found_text_positions["ΠΕ"][1]
        position_x += x_distance
        canvas.coords(second_pe_item, position_x, row_y)

        # Arrange remaining texts in correct order with specified spacing
        for text in correct_order:
            if text in found_text_positions and text not in ["ΠΕ", "Χ"]:  # Skip already positioned texts
                for item, _, _ in found_text_positions[text]:  # Position each remaining text
                    position_x += x_distance
                    canvas.coords(item, position_x, row_y)

    else:
        # Proceed with standard re-arrangement if there aren’t two "ΠΕ"s and one "Χ"
        ordered_texts = [text for text in correct_order if text in found_text_positions]
        position_x = screen_width / 10.3783  # Initial position
        for text in ordered_texts:
            for item, _, _ in found_text_positions[text]:
                canvas.coords(item, position_x, row_y)
                position_x += x_distance  # Move to the next position

            
def check_and_swap_ae_prime_ae(canvas, screen_width, screen_height):
    # Define the Y position for the first row
    row_y = screen_height / 7.4482

    # Get all items in the canvas
    items = canvas.find_all()

    # Variables to store positions of "ΑΕ'" and "ΑΕ"
    ae_prime_position = None
    ae_position = None
    has_x = False

    # Scan items in the first row for "ΑΕ'", "ΑΕ", and "Χ"
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Only consider texts in the first row based on Y position
            if abs(coords[1] - row_y) < 1:
                if text == "ΑΕ'":
                    ae_prime_position = (item, coords[0], coords[1])  # (item, x, y) for "ΑΕ'"
                elif text == "ΑΕ":
                    ae_position = (item, coords[0], coords[1])  # (item, x, y) for "ΑΕ"
                elif text == "Χ":
                    has_x = True

    # Only proceed if "ΑΕ'" is present, "Χ" is not present, and "ΑΕ" is to the left of "ΑΕ'"
    if ae_prime_position and not has_x and ae_position and ae_position[1] < ae_prime_position[1]:
        # Swap positions of "ΑΕ" and "ΑΕ'"
        ae_item, ae_x, ae_y = ae_position
        ae_prime_item, ae_prime_x, ae_prime_y = ae_prime_position
        canvas.coords(ae_item, ae_prime_x, ae_y)       # Move "ΑΕ" to the X position of "ΑΕ'"
        canvas.coords(ae_prime_item, ae_x, ae_prime_y) # Move "ΑΕ'" to the X position of "ΑΕ"

def check_and_rearrange_rows(canvas, screen_width, screen_height):
    # Define the Y positions for each row
    row_heights = [
        screen_height / 7.4482,                           # 1st row
        screen_height / 7.4482 + screen_height / 36,      # 2nd row
        screen_height / 7.4482 + 2 * (screen_height / 36),# 3rd row
        screen_height / 7.4482 + 3 * (screen_height / 36),# 4th row
        screen_height / 7.4482 + 4 * (screen_height / 36) # 5th row
    ]
    
    # Define the correct order of texts and the required X distance between them
    x_distance = screen_width / 38.4

    # Iterate through each row
    for row_y in row_heights:
        # Get all items in the canvas
        items = canvas.find_all()
        
        # Dictionary to store the positions of "ΠΕ" and "Χ" in the current row
        found_pe_positions = []
        found_x_position = None

        # Collect positions of "ΠΕ" and "Χ" in the current row
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)
                # Only consider texts in the current row based on Y position
                if abs(coords[1] - row_y) < 1:
                    if text == "ΠΕ":
                        found_pe_positions.append((item, coords[0], coords[1]))  # Store "ΠΕ" (item, x, y)
                    elif text == "Χ":
                        found_x_position = (item, coords[0], coords[1])  # Store "Χ" (item, x, y)

        # Proceed only if there are two "ΠΕ"s and one "Χ" in the row
        if len(found_pe_positions) == 2 and found_x_position:
            # Sort "ΠΕ" positions by X coordinate to identify the first and second "ΠΕ"
            found_pe_positions.sort(key=lambda pos: pos[1])
            first_pe_item, first_pe_x, first_pe_y = found_pe_positions[0]
            second_pe_item, second_pe_x, second_pe_y = found_pe_positions[1]
            
            # Position "Χ" immediately to the right of the first "ΠΕ"
            x_item, x_current_x, x_current_y = found_x_position
            expected_x_position = first_pe_x + x_distance

            # Move "Χ" if it's not already in the correct position
            if abs(x_current_x - expected_x_position) > 1:
                canvas.coords(x_item, expected_x_position, x_current_y)

            # No further adjustments are made, as per the requirement


def clear_texts_beyond_limit(canvas, screen_height):
    # Define the Y position limit
    y_limit = screen_height / 7.4482 + 4 * (screen_height / 36)
    
    # Define the target texts to clear
    target_texts = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

    # Get all items in the canvas
    items = canvas.find_all()

    # Iterate through each item and delete if it meets the criteria
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Check if the item is one of the target texts and has a Y position beyond the limit
            if text in target_texts and coords[1] > y_limit:
                canvas.delete(item)  # Remove the text from the canvas

def clear_texts_beyond_first_row_x(canvas, screen_width, screen_height):
    # Define the Y position for the first row
    first_row_y = screen_height / 7.4482

    # Define the target texts to check
    target_texts = ["ΠΕ", "ΑΕ'", "Χ", "ΑΕ", "ΕΠ", "ΠΜ", "ΑΑ"]

    # Find the maximum X position of these texts in the first row
    max_x_first_row = 0
    items = canvas.find_all()

    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Check if text is in the target list and in the first row
            if text in target_texts and abs(coords[1] - first_row_y) < 1:
                max_x_first_row = max(max_x_first_row, coords[0])

    # Iterate through each item and delete if it has an X position beyond max_x_first_row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Check if the item is one of the target texts and has an X position beyond the limit
            if text in target_texts and coords[0] > max_x_first_row+0.1:
                canvas.delete(item)  # Remove the text from the canvas

def check_and_adjust_pm_position(canvas, screen_width, screen_height):
    # Define the target row height for the second row
    second_row_y = screen_height / 7.4482 + screen_height / 36
    x_distance = screen_width / 38.4  # Define the required x distance

    # Initialize variables to store the positions of "ΕΠ" and "ΠΜ" in the second row
    ep_item = None
    pm_item = None
    ep_x = None
    pm_x = None

    # Get all items in the canvas
    items = canvas.find_all()

    # Locate "ΕΠ" and "ΠΜ" in the second row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            if abs(coords[1] - second_row_y) < 1:  # Confirm it's in the second row
                if text == "ΕΠ":
                    ep_item = item
                    ep_x = coords[0]
                elif text == "ΠΜ":
                    pm_item = item
                    pm_x = coords[0]

    # Check if both "ΕΠ" and "ΠΜ" are found in the second row
    if ep_item and pm_item:
        # Check if "ΠΜ" is to the right of "ΕΠ" and if the x distance is too large
        if pm_x > ep_x and (pm_x - ep_x) > x_distance:
            # Move "ΠΜ" to be exactly x_distance from "ΕΠ"
            new_pm_x = ep_x + x_distance
            canvas.coords(pm_item, new_pm_x, second_row_y)

def adjust_pipeline_texts(canvas, screen_width, screen_height):
    """Move the first text in the first row to coords[0] = screen_width / 10.3783 
    and coords[1] = screen_height / 7.4482. Shift all other pipeline texts 
    ('ΠΕ', 'ΑΕ', 'ΑΕ'', 'Χ', 'ΕΠ', 'ΠΜ', 'ΑΑ') by the same delta_x."""
    
    target_x = screen_width / 10.3783  # Correct X position for the first text
    target_y = screen_height / 7.4482  # Correct Y position for the first row
    delta_x = 0  # To track how much to move all other texts

    pipeline_texts = {"ΠΕ", "ΑΕ", "ΑΕ'", "Χ", "ΕΠ", "ΠΜ", "ΑΑ"}  # Only adjust these texts

    # Step 1: Find the first text in the first row
    items = canvas.find_all()
    first_text_item = None
    first_text_coords = None

    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)

            # Look for the first pipeline text in the first row
            if abs(coords[1] - target_y) < 1 and text in pipeline_texts:
                first_text_item = item
                first_text_coords = coords
                break  # We only care about the first pipeline text in the first row

    # If no first text is found in the first row, exit the function
    if not first_text_item:
        return

    # Step 2: Check if the first text needs to be moved
    if first_text_coords[0] != target_x:
        # Calculate how much the first text needs to be moved
        delta_x = target_x - first_text_coords[0]

        # Move the first text to the correct position
        canvas.coords(first_text_item, target_x, target_y)

    # Step 3: Move all other pipeline texts by delta_x, skipping the first text
    if delta_x != 0:
        for item in items:
            if canvas.type(item) == "text":
                text = canvas.itemcget(item, "text")
                coords = canvas.coords(item)

                # Only adjust pipeline texts, skipping the first text
                if text in pipeline_texts and item != first_text_item:
                    new_x = coords[0] + delta_x
                    canvas.coords(item, new_x, coords[1])

#Check if "AA" is in the first row
def is_aa_in_first_row(canvas, screen_height, tolerance=5):
    """
    Check if the text "ΑΑ" is in the first row of the canvas.
    Adds tolerance to account for slight deviations in Y-coordinates.

    Parameters:
        tolerance (int): The acceptable deviation in Y-coordinate.

    Returns:
        bool: True if "ΑΑ" is found in the first row, False otherwise.
    """
    first_row_y = screen_height / 7.4482

    # Get all the items in the canvas
    items = canvas.find_all()

    # Iterate over all items and check for "ΑΑ" in the first row
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)

            # Check if the text is "ΑΑ" and within the tolerance range of the first row
            if text == "ΑΑ" and abs(coords[1] - first_row_y) <= tolerance:
                return True

    return False

# Delete texts that contain ΠΕ, ΑΕ, ΕΠ, ΠΜ, ΑΑ, X in the first row
def delete_specific_texts(canvas, screen_height):
    items = canvas.find_all()
    texts_to_delete = ["ΠΕ", "ΑΕ", "ΑΕ'", "ΕΠ", "ΠΜ", "ΑΑ", "Χ"]

    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Delete the text if it matches and has the first row's Y position
            if text in texts_to_delete and coords[1] == screen_height / 7.4482:
                canvas.delete(item)

# Move texts from second row to first row, adjusting their X and Y positions
def move_texts_up(canvas, screen_height, screen_width):
    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5

    items = canvas.find_all()
    texts_to_move = ["ΠΕ", "ΑΕ", "ΑΕ'", "ΕΠ", "ΠΜ", "ΑΑ", "Χ"]

    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            # Move text if it's in the second row (next Y position)
            if text in texts_to_move:
                new_x = coords[0] - screen_width / 38.4
                new_y = coords[1] - screen_height / 36
                canvas.coords(item, new_x, new_y)
            if text == "Χ" and coords[1] == screen_height / 7.4482 + screen_height / 36:
                if coords[1] > screen_height / 7.4482 + screen_height / 36:
                    # Modify the X position
                    new_x = coords[0] - screen_width / 38.4 - screen_width / 38.4
                    # Update the text position with the new X coordinate, keeping the Y the same
                    canvas.coords(item, new_x, coords[1])

def adjust_text_spacing_on_canvas(canvas, screen_width, screen_height):
    """
    Adjusts the x-spacing of texts in all rows of the canvas if the spacing exceeds a threshold.

    Parameters:
        canvas (tk.Canvas): The canvas containing the text items.
        screen_width (float): The width of the screen used for spacing calculations.
        screen_height (float): The height of the screen, used to calculate row positions.
    """
    max_distance = screen_width / 38.4 + 1  # Maximum allowed distance between texts
    target_texts = ("ΠΕ", "ΑΕ", "ΑΕ'", "Χ", "ΕΠ", "ΠΜ", "ΑΑ")  # Texts to check

    # Calculate row y-positions
    rows_y_positions = [
        screen_height / 7.4482,
        screen_height / 7.4482 + screen_height / 36,
        screen_height / 7.4482 + 2 * (screen_height / 36),
        screen_height / 7.4482 + 3 * (screen_height / 36),
        screen_height / 7.4482 + 5 * (screen_height / 36)
    ]

    # Iterate through all canvas items to get the text items
    for y in rows_y_positions:
        row_items = []

        # Go through all canvas items and collect text items that match the target texts
        for item in canvas.find_all():
            if canvas.type(item) == "text":
                item_text = canvas.itemcget(item, "text")
                item_x, item_y = canvas.coords(item)
                
                if abs(item_y - y) < 2 and item_text in target_texts:
                    row_items.append((item, item_x, item_y))

        # Sort the row items by their x-coordinates
        row_items.sort(key=lambda x: x[1])  # Sorting by x-coordinate

        # Adjust x-coordinates if spacing exceeds max_distance
        for i in range(len(row_items) - 1):
            left_item, left_x, y_pos = row_items[i]
            right_item, right_x, _ = row_items[i + 1]

            current_distance = right_x - left_x

            if current_distance > max_distance:
                # Move the right text closer to the left text
                new_x = left_x + screen_width / 38.4
                canvas.coords(right_item, new_x, y_pos)

#Βαθμίδες
def vathmides_nop(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5

    Instr_Cache = gui_vars.Instr_Cache
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    pe_flag = cycles.pe_flag
    ae_flag = cycles.ae_flag
    ep_flag = cycles.ep_flag
    pm_flag = cycles.pm_flag
    aa_flag = cycles.aa_flag

    if is_aa_in_first_row(canvas, screen_height):
        delete_specific_texts(canvas, screen_height)
        move_texts_up(canvas, screen_height, screen_width)
        position_x1 -= screen_width / 38.4
        position_y1 -= screen_height / 36
        position_x3 -= screen_width / 38.4
        position_x2 -= screen_width / 38.4
        position_y3 -= screen_height / 36
        position_y2 -= screen_height / 36
        position_x4 -= screen_width / 38.4
        position_x5 -= screen_width / 38.4
        position_y4 -= screen_height / 36
        position_y5 -= screen_height / 36

    if i == 0:
        pe_flag = -1
        ae_flag = -1
        ep_flag = -1
        pm_flag = -1
        aa_flag = -1

    if i >= 0:
        if i in bre_array_not:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        elif i in bre_index:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        else:
            if pe_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width/192)))
                position_x1 += screen_width / 38.4
                position_y1 += screen_height / 36

    if i >= 1:
        if i in bre_array_not or i-1 in bre_array_not:
            position_x2 += screen_width / 38.4
        elif i in bre_index or i-1 in bre_index:
            position_x2 += screen_width / 38.4
        else:
            if ae_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                position_x2 += screen_width / 38.4
                position_y2 += screen_height / 36

    if i >= 2:
        if i - 2 in bre_array_not or i-1 in bre_array_not:
            position_x3 += screen_width / 38.4
        elif i - 2 in bre_index or i-1 in bre_index:
            position_x3 += screen_width / 38.4
        else:
            if ep_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                position_x3 += screen_width / 38.4
                position_y3 += screen_height / 36

    if i >= 3:
        if i - 2 in bre_array_not or i - 3 in bre_array_not:
            position_x4 += screen_width / 38.4
        elif i - 2 in bre_index or i - 3 in bre_index:
            position_x4 += screen_width / 38.4
        else:
            if pm_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                position_x4 += screen_width / 38.4
                position_y4 += screen_height / 36

    if i >= 4:
        if i - 4 in bre_array_not or i - 3 in bre_array_not:
            position_x5 += screen_width / 38.4
        elif i - 4 in bre_index or i - 3 in bre_index:
            position_x5 += screen_width / 38.4
        else:
            if aa_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                position_x5 += screen_width / 38.4
                position_y5 += screen_height / 36

    adjust_pipeline_texts(canvas, screen_width, screen_height)
    adjust_text_spacing_on_canvas(canvas, screen_width, screen_height)
    check_and_move_pe_below_ae_if_needed(canvas, screen_width, screen_height)
    delete_texts_above_threshold(canvas, screen_height)
    
    if i == z - 1:
        position_x1 = screen_width/10.3783
        position_y1 = screen_height/7.4482
        position_x2 = screen_width/8.1702
        position_y2 = screen_height/7.4482
        position_x3 = screen_width/6.7368
        position_y3 = screen_height/7.4482
        position_x4 = screen_width/5.7313
        position_y4 = screen_height/7.4482
        position_x5 = screen_width/4.9870
        position_y5 = screen_height/7.4482

def vathmides_freeze(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5, index1, index2, index3, index4, index5, index

    Instr_Cache = gui_vars.Instr_Cache
    bre_array_not = cycles.bre_array_not
    bre_index = cycles.bre_index
    pe_flag = cycles.pe_flag
    ae_flag = cycles.ae_flag
    ep_flag = cycles.ep_flag
    pm_flag = cycles.pm_flag
    aa_flag = cycles.aa_flag

    if i == 0:
        index = 0

    if is_aa_in_first_row(canvas, screen_height):
        delete_specific_texts(canvas, screen_height)
        move_texts_up(canvas, screen_height, screen_width)
        position_x1 -= screen_width / 38.4
        position_y1 -= screen_height / 36
        position_x3 -= screen_width / 38.4
        position_x2 -= screen_width / 38.4
        position_y3 -= screen_height / 36
        position_y2 -= screen_height / 36
        position_x4 -= screen_width / 38.4
        position_x5 -= screen_width / 38.4
        position_y4 -= screen_height / 36
        position_y5 -= screen_height / 36

    if i >= 0:
        if i in bre_array_not:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
            pe_flag -= 1
        elif i in bre_index:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
            pe_flag -= 1
        elif i+1 in bre_index:
            canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width / 192)))
            position_x1 += screen_width / 38.4
            position_y1 += screen_height / 36
        elif i -1 in index3 or i in index3:
            position_x1 += screen_width / 38.4
        elif i in index5:
            position_x1 += screen_width / 38.4
        else:
            if pe_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width / 192)))
                position_x1 += screen_width / 38.4
                position_y1 += screen_height / 36

    if i >= 1:
        if i in bre_array_not or i-1 in bre_array_not:
            position_x2 += screen_width / 38.4
        elif i in bre_index or i-1 in bre_index:
            position_x2 += screen_width / 38.4
        elif i in index3:
            canvas.create_text(position_x2, position_y2, text="ΑΕ'", font=("Arial", int(screen_width/192)))
            position_x2 = position_x2 + screen_width/38.4
        elif i-1 in index3:
            canvas.create_text(position_x2, position_y2, text="Χ", font=("Arial", int(screen_width/192)))
            position_x2 = position_x2 + screen_width/38.4
        elif i in index5:
            canvas.create_text(position_x2, position_y2, text="ΑΕ'", font=("Arial", int(screen_width/192)))
            position_x2 = position_x2 + screen_width/38.4
        else:
            if ae_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                position_x2 = position_x2 + screen_width/38.4
                position_y2 = position_y2 + screen_height/36
    
    if i >= 2:
        if i - 2 in bre_array_not or i-1 in bre_array_not:
            position_x3 += screen_width / 38.4
        elif i - 2 in bre_index or i-1 in bre_index:
            position_x3 += screen_width / 38.4
        elif i-1 in index3 or i-2 in index3:
            position_x3 = position_x3 + screen_width/38.4
        elif i-1 in index5:
            position_x3 = position_x3 + screen_width/38.4
        else:
            if ep_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                position_x3 = position_x3 + screen_width/38.4
                position_y3 = position_y3 + screen_height/36
    
    if i >= 3:
        if i - 2 in bre_array_not or i - 3 in bre_array_not:
            position_x4 += screen_width / 38.4
        elif i - 2 in bre_index or i - 3 in bre_index:
            position_x4 += screen_width / 38.4
        elif i-2 in index3 or i-3 in index3:
            position_x4 = position_x4 + screen_width/38.4
        elif i-2 in index5:
            position_x4 = position_x4 + screen_width/38.4
        else:
            if pm_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                position_x4 = position_x4 + screen_width/38.4
                position_y4 = position_y4 + screen_height/36
    
    if i >= 4:
        if i - 4 in bre_array_not or i - 3 in bre_array_not:
            position_x5 += screen_width / 38.4
        elif i - 4 in bre_index or i - 3 in bre_index:
            position_x5 += screen_width / 38.4
        elif i-4 in index3 or i-3 in index3:
            position_x5 = position_x5 + screen_width/38.4 
        elif i-3 in index5:
            position_x5 = position_x5 + screen_width/38.4
        else:
            if aa_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                position_x5 = position_x5 + screen_width/38.4
                position_y5 = position_y5 + screen_height/36

    adjust_pipeline_texts(canvas, screen_width, screen_height)
    adjust_text_spacing_on_canvas(canvas, screen_width, screen_height)
    check_and_move_pe_below_ae_if_needed(canvas, screen_width, screen_height)
    delete_texts_above_threshold(canvas, screen_height)
    
    if i == z - 1:
        position_x1 = screen_width/10.3783
        position_y1 = screen_height/7.4482
        position_x2 = screen_width/8.1702
        position_y2 = screen_height/7.4482
        position_x3 = screen_width/6.7368
        position_y3 = screen_height/7.4482
        position_x4 = screen_width/5.7313
        position_y4 = screen_height/7.4482
        position_x5 = screen_width/4.9870
        position_y5 = screen_height/7.4482

#Βαθμίδες
def vathmides_bypassing_nop(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5, arrow, arrow1, arrow2, arrow3
    global index3, index5, index6

    Instr_Cache = gui_vars.Instr_Cache
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    index_bypass_cycle = dependencies.index_bypass_cycle
    index8 = dependencies.index8
    d_value = cycles.d_value
    bre_index_pred = dependencies.bre_index_pred
    pe_flag = cycles.pe_flag
    ae_flag = cycles.ae_flag
    ep_flag = cycles.ep_flag
    pm_flag = cycles.pm_flag
    aa_flag = cycles.aa_flag
    
    if is_aa_in_first_row(canvas, screen_height):
        delete_specific_texts(canvas, screen_height)
        move_texts_up(canvas, screen_height, screen_width)
        position_x1 -= screen_width / 38.4
        position_y1 -= screen_height / 36
        position_x3 -= screen_width / 38.4
        position_x2 -= screen_width / 38.4
        position_y3 -= screen_height / 36
        position_y2 -= screen_height / 36
        position_x4 -= screen_width / 38.4
        position_x5 -= screen_width / 38.4
        position_y4 -= screen_height / 36
        position_y5 -= screen_height / 36

    if i == 0:
        pe_flag = -1
        ae_flag = -1
        ep_flag = -1
        pm_flag = -1
        aa_flag = -1

    if arrow is not None:
        canvas.delete(arrow)
    if i in index8 and i == 3:
        x1_line = screen_width/6.5084
        y1_line = screen_height/7.4482
        x2_line = screen_width/5.8895
        y2_line = screen_height/6.1714
        arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the linw
    elif i in index8:
        if any(val2 > val1 == 4 for val1 in bre_index for val2 in index8):
            x1_line = screen_width/5.5652 + screen_width/38.4
            x2_line = screen_width/5.1063 + screen_width/38.4
            y1_line = screen_height/6.1714 - screen_height/36
            y2_line = screen_height/5.2682 - screen_height/36
            arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
        elif any(val2 - val1 == 5 for val1 in bre_index for val2 in index8) or any(val2 - val1 == 5 for val1 in bre_array_not for val2 in index8):
            x1_line = screen_width/5.5652 + 2*(screen_width/38.4)
            x2_line = screen_width/5.1063 + 2*(screen_width/38.4)
            y1_line = screen_height/6.1714
            y2_line = screen_height/5.2682
            arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
        elif any(val2 - val1 == 4 for val1 in bre_array_not for val2 in index8):
            x1_line = screen_width/5.5652 + (screen_width/38.4)
            x2_line = screen_width/5.1063 + (screen_width/38.4)
            y1_line = screen_height/6.1714 - screen_height/36
            y2_line = screen_height/5.2682 - screen_height/36
            arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
        else:
            x1_line = screen_width/5.5652
            x2_line = screen_width/5.1063
            y1_line = screen_height/6.1714
            y2_line = screen_height/5.2682
            arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    if arrow1 is not None:
        canvas.delete(arrow1)
    if i in index_bypass_cycle and i == 3:
        x1_line = position_x3-(screen_width / 48)
        y1_line = position_y3-(screen_height / 36)
        x2_line = position_x3-(screen_width / 216)
        y2_line = position_y3
        arrow1 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
   
    if arrow2 is not None:
        canvas.delete(arrow2)
    if i in index_bypass_cycle:
        x1_line = position_x3-(screen_width / 48)
        y1_line = position_y3-(screen_height / 36)
        x2_line = position_x3-(screen_width / 216)
        y2_line = position_y3
        arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    if arrow2 is not None:
            canvas.delete(arrow2)
    if i in index6:
        if any(val2 > val1 == 5 for val1 in bre_index for val2 in index6):
            x1_line = position_x3+2*(screen_width / 48)
            y1_line = position_y3-2*(screen_height / 36)
            x2_line = position_x3+2*(screen_width / 216)
            y2_line = position_y3
            arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
        else:
            x1_line = position_x3-(screen_width / 48)
            y1_line = position_y3-2*(screen_height / 36)
            x2_line = position_x3-(screen_width / 216)
            y2_line = position_y3
            arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line

    if i >= 0:
        if i in bre_array_not:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        elif i in bre_index:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        else:
            if pe_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width/192)))
                position_x1 += screen_width / 38.4
                position_y1 += screen_height / 36

    if i >= 1:
        if i in bre_array_not or i-1 in bre_array_not:
            position_x2 += screen_width / 38.4
        elif i in bre_index or i-1 in bre_index:
            position_x2 += screen_width / 38.4
        else:
            if ae_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                position_x2 += screen_width / 38.4
                position_y2 += screen_height / 36
 
    if i >= 2:
        if i - 2 in bre_array_not or i-1 in bre_array_not:
            position_x3 += screen_width / 38.4
        elif i - 2 in bre_index or i-1 in bre_index:
            position_x3 += screen_width / 38.4
        else:
            if ep_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                position_x3 += screen_width / 38.4
                position_y3 += screen_height / 36

    if i >= 3:
        if i - 2 in bre_array_not or i - 3 in bre_array_not:
            position_x4 += screen_width / 38.4
        elif i - 2 in bre_index or i - 3 in bre_index:
            position_x4 += screen_width / 38.4
        else:
            if pm_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                position_x4 += screen_width / 38.4
                position_y4 += screen_height / 36
    
    if i >= 4:
        if i - 4 in bre_array_not or i - 3 in bre_array_not:
            position_x5 += screen_width / 38.4
        elif i - 4 in bre_index or i - 3 in bre_index:
            position_x5 += screen_width / 38.4
        else:
            if aa_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                position_x5 += screen_width / 38.4
                position_y5 += screen_height / 36
                
    adjust_pipeline_texts(canvas, screen_width, screen_height)
    adjust_text_spacing_on_canvas(canvas, screen_width, screen_height)
    check_and_move_pe_below_ae_if_needed(canvas, screen_width, screen_height)
    delete_texts_above_threshold(canvas, screen_height)
    
    if i == z - 1:
        position_x1 = screen_width/10.3783
        position_y1 = screen_height/7.4482
        position_x2 = screen_width/8.1702
        position_y2 = screen_height/7.4482
        position_x3 = screen_width/6.7368
        position_y3 = screen_height/7.4482
        position_x4 = screen_width/5.7313
        position_y4 = screen_height/7.4482
        position_x5 = screen_width/4.9870
        position_y5 = screen_height/7.4482

def vathmides_bypassing_freeze(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5, index1, index2, index3, index4, index5, index8, index7
    global index, arrow, arrow2, arrow3, arrow4

    Instr_Cache = gui_vars.Instr_Cache
    bre_array_not = cycles.bre_array_not
    bre_index = cycles.bre_index
    pe_flag = cycles.pe_flag
    ae_flag = cycles.ae_flag
    ep_flag = cycles.ep_flag
    pm_flag = cycles.pm_flag
    aa_flag = cycles.aa_flag

    if i == 0:
        index = 0

    if is_aa_in_first_row(canvas, screen_height):
        delete_specific_texts(canvas, screen_height)
        move_texts_up(canvas, screen_height, screen_width)
        position_x1 -= screen_width / 38.4
        position_y1 -= screen_height / 36
        position_x3 -= screen_width / 38.4
        position_x2 -= screen_width / 38.4
        position_y3 -= screen_height / 36
        position_y2 -= screen_height / 36
        position_x4 -= screen_width / 38.4
        position_x5 -= screen_width / 38.4
        position_y4 -= screen_height / 36
        position_y5 -= screen_height / 36

    if arrow is not None:
        canvas.delete(arrow)
    if i in index8 and i == 3:
        x1_line = screen_width/6.5084
        y1_line = screen_height/7.4482
        x2_line = screen_width/5.8895
        y2_line = screen_height/6.1714
        arrow = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    else:
        if arrow2 is not None:
            canvas.delete(arrow2)
        if i in index8:
            if i-3 in index4:
                x1_line = screen_width/5.5652
                x2_line = screen_width/5.1063
                y1_line = screen_height/6.1714 - screen_height/36
                y2_line = screen_height/5.2682 - screen_height/36
                arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
            elif i-4 in index4:
                x1_line = screen_width/5.5652 + screen_width/38.4
                x2_line = screen_width/5.1063 + screen_width/38.4
                y1_line = screen_height/6.1714
                y2_line = screen_height/5.2682
                arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
            else:
                if any(val2 - val1 == 3 for val1 in bre_index for val2 in index8):
                    x1_line = screen_width/5.5652 + screen_width/38.4
                    y1_line = screen_height/6.1714 - screen_height/36
                    x2_line = screen_width/5.1063 + screen_width/38.4
                    y2_line = screen_height/5.2682 - screen_height/36
                    arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
                elif any(val2 - val1 == 4 for val1 in bre_index for val2 in index8):
                    x1_line = screen_width/5.5652 + (screen_width/38.4)
                    y1_line = screen_height/6.1714 - (screen_height/36)
                    x2_line = screen_width/5.1063 + (screen_width/38.4)
                    y2_line = screen_height/5.2682 - (screen_height/36)
                    arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
                elif any(val2 - val1 == 4 for val1 in bre_array_not for val2 in index8):
                    x1_line = screen_width/5.5652 + (screen_width/38.4)
                    y1_line = screen_height/6.1714 - (screen_height/36)
                    x2_line = screen_width/5.1063 + (screen_width/38.4)
                    y2_line = screen_height/5.2682 - (screen_height/36)
                    arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
                elif any(val2 - val1 == 5 for val1 in bre_array_not for val2 in index8):
                    x1_line = screen_width/5.5652 + 2*(screen_width/38.4)
                    y1_line = screen_height/6.1714
                    x2_line = screen_width/5.1063 + 2*(screen_width/38.4)
                    y2_line = screen_height/5.2682
                    arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
                else:
                    x1_line = screen_width/5.5652
                    y1_line = screen_height/6.1714
                    x2_line = screen_width/5.1063
                    y2_line = screen_height/5.2682
                    arrow2 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    if arrow3 is not None:
        canvas.delete(arrow3)
    if i-2 in index4:
        # Check if any value in array1 and array2 has a distance of 4
        if any(val2 - val1 == 4 for val1 in bre_array_not for val2 in index4) or any(val2 - val1 == 3 for val1 in bre_index for val2 in index4) or any(val2 - val1 == 5 for val1 in bre_array_not for val2 in index4):
            x1_line = screen_width/5.5652 + 2*(screen_width/38.4)
            y1_line = screen_height/7.4482 
            x2_line = screen_width/5.1063 + 2*(screen_width/38.4)
            y2_line = screen_height/6.1714
            arrow3 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
        else:
            x1_line = screen_width/5.5652
            y1_line = screen_height/7.4482
            x2_line = screen_width/5.1063
            y2_line = screen_height/6.1714
            arrow3 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    if arrow4 is not None:
        canvas.delete(arrow4)
    if i in index7:
        x1_line = position_x3-(screen_width / 48)
        y1_line = position_y3-2*(screen_height / 36)
        x2_line = position_x3-(screen_width / 216)
        y2_line = position_y3
        arrow4 = canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2, arrow="last") # Arrowhead at the end of the line
    
    if i >= 0:
        if i in bre_array_not:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        elif i in bre_index:
            position_y1 -= screen_height / 36
            canvas.create_text(position_x1, position_y1, text="Χ", font=("Arial", int(screen_width/192)))
            position_x1 += screen_width / 38.4
        elif i in index4:
            position_x1 += screen_width / 38.4
        else:
            if pe_flag > len(Instr_Cache):
                pass
            else:
                print("poutsa")
                canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width / 192)))
                position_x1 += screen_width / 38.4
                position_y1 += screen_height / 36
             
    if i >= 1:
        if i in bre_array_not or i-1 in bre_array_not:
            position_x2 += screen_width / 38.4
        elif i in bre_index or i-1 in bre_index:
            position_x2 += screen_width / 38.4
        elif i in index4:
            canvas.create_text(position_x2, position_y2, text="ΑΕ'", font=("Arial", int(screen_width/192)))
            position_x2 = position_x2 + screen_width/38.4
        else:
            if ae_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                position_x2 = position_x2 + screen_width/38.4
                position_y2 = position_y2 + screen_height/36

    if i >= 2:
        if i - 2 in bre_array_not or i-1 in bre_array_not:
            position_x3 += screen_width / 38.4
        elif i - 2 in bre_index or i-1 in bre_index:
            position_x3 += screen_width / 38.4
        elif i-1 in index4:
            position_x3 = position_x3 + screen_width/38.4
        else:
            if ep_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                position_x3 = position_x3 + screen_width/38.4
                position_y3 = position_y3 + screen_height/36
    
    if i >= 3:
        if i - 2 in bre_array_not or i - 3 in bre_array_not:
            position_x4 += screen_width / 38.4
        elif i - 2 in bre_index or i - 3 in bre_index:
            position_x4 += screen_width / 38.4
        elif i-2 in index4:
            position_x4 = position_x4 + screen_width/38.4
        else:
            if pm_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                position_x4 = position_x4 + screen_width/38.4
                position_y4 = position_y4 + screen_height/36

    if i >= 4:
        if i - 4 in bre_array_not or i - 3 in bre_array_not:
            position_x5 += screen_width / 38.4
        elif i - 4 in bre_index or i - 3 in bre_index:
            position_x5 += screen_width / 38.4
        elif i-3 in index4:
            position_x5 = position_x5 + screen_width/38.4
        else:
            if aa_flag > len(Instr_Cache):
                pass
            else:
                canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                position_x5 = position_x5 + screen_width/38.4
                position_y5 = position_y5 + screen_height/36

    adjust_pipeline_texts(canvas, screen_width, screen_height)
    adjust_text_spacing_on_canvas(canvas, screen_width, screen_height)
    check_and_move_pe_below_ae_if_needed(canvas, screen_width, screen_height)
    delete_texts_above_threshold(canvas, screen_height)

    if i == z - 1:
        position_x1 = screen_width/10.3783
        position_y1 = screen_height/7.4482
        position_x2 = screen_width/8.1702
        position_y2 = screen_height/7.4482
        position_x3 = screen_width/6.7368
        position_y3 = screen_height/7.4482
        position_x4 = screen_width/5.7313
        position_y4 = screen_height/7.4482
        position_x5 = screen_width/4.9870
        position_y5 = screen_height/7.4482