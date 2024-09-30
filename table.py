from vars import r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m

import cycles
skip = 0

def create_simple_canvas(canvas, screen_width, screen_height):

    global skip

    # Πίνακας "Εντολή"
    x1, y1 = screen_width/27, screen_height /7.7142
    x2, y2 = screen_width/5, screen_height /5.4
    canvas.create_rectangle(screen_width/38.4, screen_height/15.4285, screen_width/12, screen_height/8.3076, outline="black", width=2)

    # Πίνακας "Περίοδος Σήματος Χρονισμού"
    x1, y1 = screen_width/5, screen_height/7.7142
    x2, y2 = screen_width/2.5, screen_height/5.4
    canvas.create_rectangle(screen_width/12, screen_height/15.4285, screen_width/3.1475, screen_height/8.3076, outline="black", width=2)

    #"εντολή"
    canvas.create_text(screen_width/18.2857, screen_height/10.8, text="εντολή", font=("Arial", int(screen_width/192), 'bold'))

    #"περίοδος σήματος χρονισμού"
    canvas.create_text(screen_width/5.8181, screen_height/12.7058, text="περίοδος σήματος χρονισμού", font=("Arial", int(screen_width/192), 'bold'))

    #Starting position for the rows
    start_y = screen_height/8.3076  # Starting y-coordinate for the first row
    row_height = screen_height/36  # Height of each row

    #Δημιουργία 5 γραμμών
    for i in range(5):
        y1 = start_y + i * row_height
        y2 = y1 + row_height
        canvas.create_rectangle(screen_width/38.4, y1, screen_width/12, y2, outline="black", width=2)  # Row in "Εντολή" column
        canvas.create_rectangle(screen_width/12, y1, screen_width/3.1475, y2, outline="black", width=2)  # Row in "Περίοδος Σήματος Χρονισμού" column

    # Move the "Καταχωρητές" table to the right by 300 points
    x_offset = screen_width/14.7692  # Offset for the rightward shift

    # Πίνακας Καταχωρητών
    canvas.create_rectangle(screen_width/3.2 + x_offset, screen_height/15.4285, screen_width/2.4615 + x_offset, screen_height/8.3076, outline="black", width=2)

    # Dimensions for the rows and columns
    row_height = screen_height/36  # Height of each row
    col_width = screen_width/21.3333  # Width of each column

    if skip == 0:
        r0=r0_start
        r1=r1_start
        r2=r2_start
        r3=r3_start
        r4=r4_start
        r5=r5_start
        r6=r6_start
        r7=r7_start
    else:
        r0=cycles.r0
        r1=cycles.r1
        r2=cycles.r2
        r3=cycles.r3
        r4=cycles.r4
        r5=cycles.r5
        r6=cycles.r6
        r7=cycles.r7

    rows_data = {
        "r0": r0,
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "r4": r4,
        "r5": r5,
        "r6": r6,
        "r7": r7
    }

    # Loop to create rows and columns with labels and values
    for i, (label, values) in enumerate(rows_data.items()):
        y1 = screen_height/8.3076 + i * row_height  # Starting y-coordinate for each row
        y2 = y1 + row_height  # Ending y-coordinate for each row

        # Draw rectangles for each column in the row
        canvas.create_rectangle(screen_width/3.2 + x_offset, y1, screen_width/3.2 + col_width + x_offset, y2, outline="black", width=2)  # Left column
        canvas.create_rectangle(screen_width/3.2 + col_width + x_offset, y1, screen_width/2.4615 + x_offset, y2, outline="black", width=2)  # Right column

        # Add label in the left column
        canvas.create_text(screen_width/3.2 + col_width/2 + x_offset, y1 + row_height/2, text=label, font=("Arial", int(screen_width/192)))

        # Add values in the right column
        values_text = " - ".join(values)  # Combine the list of values into a string
        canvas.create_text(screen_width/3.2 + col_width + col_width/2 + x_offset, y1 + row_height/2, text=values_text, font=("Arial", int(screen_width/192)))


    #"Καταχωρητές Γενικού Σκοπού"
    canvas.create_text(screen_width/2.7826 + x_offset, screen_height/10.8, text="  Καταχωρητές \nΓενικού Σκοπού", font=("Arial", int(screen_width/192), 'bold'))

    # Move the "Πίνακας Μνήμης" table to the right by 300 points
    # Πίνακας Μνήμης
    canvas.create_rectangle(screen_width/2.3132 + x_offset, screen_height/15.4285, screen_width/1.5609 + x_offset, screen_height/8.3076, outline="black", width=2)

    # Height of each row
    row_height = screen_height/36

    # Draw the first row (full width)
    first_row_y1 = screen_height/15.4285
    first_row_y2 = screen_height/15.4285 + row_height
    canvas.create_rectangle(screen_width/2.3132 + x_offset, first_row_y1, screen_width/1.5609 + x_offset, first_row_y2, outline="black", width=2)

    # Draw the second row with 4 columns
    second_row_y1 = first_row_y2
    second_row_y2 = screen_height/8.3076
    col_width = screen_width/19.2

    # Labels for the columns
    column_labels = ["Διεύθυνση", "Περιεχόμενο", "Διεύθυνση", "Περιεχόμενο"]

    for i in range(4):
        col_x1 = screen_width/2.3132 + i * col_width + x_offset
        col_x2 = col_x1 + col_width
        canvas.create_rectangle(col_x1, second_row_y1, col_x2, second_row_y2, outline="black", width=2)

        # Add the corresponding label inside each cell
        canvas.create_text((col_x1 + col_x2)/2, (second_row_y1 + second_row_y2)/2, text=column_labels[i], font=("Arial", int(screen_width/192), 'bold'))


    # Set the starting point for the new memory table below the existing one
    start_y = screen_height/8.3076  # 20 pixels below the existing table

    canvas.create_text(screen_width/1.8640 + x_offset, screen_height/12.7058, text="Μνήμη", font=("Arial", int(screen_width / 192), 'bold'))

    # Create 8 rows and 4 columns
    for i in range(8):
        y1 = start_y + i * row_height
        y2 = y1 + row_height
        for j in range(4):
            x1 = screen_width/2.3132 + j * col_width + x_offset
            x2 = x1 + col_width
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

            # Determine which memory value to place in the current cell
            mem_index = i + (j // 2) * 8  # Calculate the index for the memory array
            value = m[mem_index][j % 2]  # Select the first or second value based on the column

            # Add the memory value inside each cell
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=value, font=("Arial", int(screen_width/192)))

    skip = 1