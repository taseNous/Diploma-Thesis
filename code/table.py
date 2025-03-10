from vars import (
                    m0_starter, m1_starter, m2_starter, m3_starter, m4_starter, m5_starter, m6_starter, m7_starter, m8_starter, m9_starter, m10_starter, m11_starter, m12_starter, 
                    m13_starter, m14_starter, m15_starter, m16_starter, m17_starter, m18_starter, m19_starter, m20_starter, m21_starter, m22_starter, m23_starter, m)

from vars import (r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start, r8_start, r9_start, r10_start, r11_start, r12_start, r13_start, r14_start, r15_start,
                        r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15)

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
    canvas.create_rectangle(screen_width/12, screen_height/15.4285, screen_width/3.75, screen_height/8.3076, outline="black", width=2)

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
        canvas.create_rectangle(screen_width/12, y1, screen_width/3.75, y2, outline="black", width=2)  # Row in "Περίοδος Σήματος Χρονισμού" column

    # Move the "Καταχωρητές" table to the right by 300 points
    x_offset = screen_width/14.7692  # Offset for the rightward shift

    # Πίνακας Καταχωρητών
    canvas.create_rectangle(screen_width/3.5, screen_height/26, screen_width/2.205 + x_offset, screen_height/15, outline="black", width=2)

    # Dimensions for the rows and columns
    row_height = screen_height/36  # Height of each row
    col_width = screen_width/17  # Width of each column

    if skip == 0:
        r0=r0_start
        r1=r1_start
        r2=r2_start
        r3=r3_start
        r4=r4_start
        r5=r5_start
        r6=r6_start
        r7=r7_start
        r8=r8_start
        r9=r9_start
        r10=r10_start
        r11=r11_start
        r12=r12_start
        r13=r13_start
        r14=r14_start
        r15=r15_start
        m0 = m0_starter
        m1 = m1_starter
        m2 = m2_starter
        m3 = m3_starter
        m4 = m4_starter
        m5 = m5_starter
        m6 = m6_starter
        m7 = m7_starter
        m8 = m8_starter
        m9 = m9_starter
        m10 = m10_starter
        m11 = m11_starter
        m12 = m12_starter
        m13 = m13_starter
        m14 = m14_starter
        m15 = m15_starter
        m16 = m16_starter
        m17 = m17_starter
        m18 = m18_starter
        m19 = m19_starter
        m20 = m20_starter
        m21 = m21_starter
        m22 = m22_starter
        m23 = m23_starter
    else:
        r0=cycles.r0
        r1=cycles.r1
        r2=cycles.r2
        r3=cycles.r3
        r4=cycles.r4
        r5=cycles.r5
        r6=cycles.r6
        r7=cycles.r7
        r8=cycles.r8
        r9=cycles.r9
        r10=cycles.r10
        r11=cycles.r11
        r12=cycles.r12
        r13=cycles.r13
        r14=cycles.r14
        r15=cycles.r15
        m0 = cycles.m0
        m1 = cycles.m1
        m2 = cycles.m2
        m3 = cycles.m3
        m4 = cycles.m4
        m5 = cycles.m5
        m6 = cycles.m6
        m7 = cycles.m7
        m8 = cycles.m8
        m9 = cycles.m9
        m10 = cycles.m10
        m11 = cycles.m11
        m12 = cycles.m12
        m13 = cycles.m13
        m14 = cycles.m14
        m15 = cycles.m15
        m16 = cycles.m16
        m17 = cycles.m17
        m18 = cycles.m18
        m19 = cycles.m19
        m20 = cycles.m20
        m21 = cycles.m21
        m22 = cycles.m22
        m23 = cycles.m23

    rows_data = {
        "r0": r0,
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "r4": r4,
        "r5": r5,
        "r6": r6,
        "r7": r7,
        "r8": r8,
        "r9": r9,
        "r10": r10,
        "r11": r11,
        "r12": r12,
        "r13": r13,
        "r14": r14,
        "r15": r15
    }

    m_data = {
        "m0" : m0,
        "m1" : m1,
        "m2" : m2,
        "m3" : m3,
        "m4" : m4,
        "m5" : m5,
        "m6" : m6,
        "m7" : m7,
        "m8" : m8,
        "m9" : m9,
        "m10" : m10,
        "m11" : m11,
        "m12" : m12,
        "m13" : m13,
        "m14" : m14,
        "m15" : m15,
        "m16" : m16,
        "m17" : m17,
        "m18" : m18,
        "m19" : m19,
        "m20" : m20,
        "m21" : m21,
        "m22" : m22,
        "m23" : m23
    }

    

    # Starting x-coordinates for each of the 4 columns
    x_offsets = [screen_width / 3.5, 
             screen_width / 3.5 + col_width * 2, 
             screen_width / 3.5 + col_width * 4, 
             screen_width / 3.5 + col_width * 6]

    # Define the headers and their positions
    header_labels = ["Καταχωρητής", "Αριθμός Αναφοράς \n     - Περιεχόμενο", "Καταχωρητής", "Αριθμός Αναφοράς \n     - Περιεχόμενο"]

    # Define x and y positions for the header row
    header_y1 = screen_height / 15  # Start y-position for the header row
    header_y2 = header_y1 + row_height  # End y-position for the header row

    # Draw header rectangles and add text for each header
    for col_index, header in enumerate(header_labels):
        header_x = x_offsets[col_index // 2] + (col_index % 2) * col_width  # Calculate x for each header cell
        canvas.create_rectangle(
            header_x, header_y1, header_x + col_width, header_y2,
            outline="black", width=2
        )
        canvas.create_text(
            header_x + col_width / 2, header_y1 + row_height / 2,
            text=header, font=("Arial", int(screen_width / 214), 'bold')
        )

    # Adjust the starting y-position for rows to be below the header row
    start_y_for_rows = header_y2  # Begin rows right after the header row

    # Loop to create rows and columns with labels and values
    for i, (label, values) in enumerate(rows_data.items()):
        # Calculate the column and row position
        column_index = i // 8  # Each column contains 8 rows
        row_index = i % 8  # Row within the current column

        # Calculate x and y coordinates for each cell
        x_offset = x_offsets[column_index]  # Start x-position of the current column
        y1 = start_y_for_rows + row_index * row_height  # Starting y-coordinate for each row in the column
        y2 = y1 + row_height  # Ending y-coordinate for each row

        # Draw rectangles for the label and values cells within each column
        canvas.create_rectangle(
            x_offset, y1, x_offset + col_width, y2,
            outline="black", width=2
        )  # Left cell (label)
        canvas.create_rectangle(
            x_offset + col_width, y1, x_offset + 2 * col_width, y2,
            outline="black", width=2
        )  # Right cell (values)

        # Add label in the left cell
        canvas.create_text(
            x_offset + col_width / 2, y1 + row_height / 2,
            text=label, font=("Arial", int(screen_width / 192))
        )

        # Add values in the right cell
        values_text = " - ".join(values[:2])  # Combine the list of values into a single string
        canvas.create_text(
            x_offset + col_width + col_width / 2, y1 + row_height / 2,
            text=values_text, font=("Arial", int(screen_width / 192))
        )


    #Καταχωρητές Γενικού Σκοπού
    canvas.create_text(screen_width/200 + x_offset, screen_height/20.5, text="Καταχωρητές Γενικού Σκοπού", font=("Arial", int(screen_width/192), 'bold'))

    # Πίνακας Μνήμης
    canvas.create_rectangle(screen_width/7.8 + x_offset, screen_height/40, screen_width/3.227 + x_offset, screen_height/18, outline="black", width=2)

    # Height of each row
    row_height = screen_height/36

    # Draw the first row (full width)
    first_row_y1 = screen_height/15.4285
    first_row_y2 = screen_height/15.4285 + row_height
    canvas.create_rectangle(screen_width/2.3132 + x_offset, first_row_y1, screen_width/1.5609 + x_offset, first_row_y2, outline="black", width=2)

    # Draw the second row with 4 columns
    second_row_y1 = first_row_y2
    second_row_y2 = screen_height/8.3076
    col_width = screen_width/22

    # Labels for the columns
    column_labels = ["Διεύθυνση", "Περιεχόμενο", "Διεύθυνση", "Περιεχόμενο"]
    start_y = screen_height/12

    # Define starting positions for the column label row
    label_y1 = start_y - row_height  # Set label row height above the memory table's start_y
    label_y2 = start_y  # Align with the top of the memory table


    # Draw rectangles and place column labels at the top of the memory table
    for i in range(4):
        col_x1 = screen_width/7.8 + i * col_width + x_offset
        col_x2 = col_x1 + col_width
        canvas.create_rectangle(col_x1, label_y1, col_x2, label_y2, outline="black", width=2)

        # Add the corresponding label inside each cell
        canvas.create_text((col_x1 + col_x2) / 2, (label_y1 + label_y2) / 2, text=column_labels[i], font=("Arial", int(screen_width / 192), 'bold'))

    # Title above the table
    canvas.create_text(screen_width / 4.5 + x_offset, start_y - row_height * 1.5, text="Μνήμη", font=("Arial", int(screen_width / 192), 'bold'))


    # Create 8 rows and 4 columns
    for i in range(12):
        start_y1 = screen_height/12
        y1 = start_y1 + i * row_height
        y2 = y1 + row_height
        for j in range(4):
            col_width1 = screen_width/22
            x1 = screen_width/7.8 + j * col_width + x_offset
            x2 = x1 + col_width1
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

            # Determine which memory value to place in the current cell
            m_data = i + (j // 2) * 12  # Calculate the index for the memory array
            value = m[m_data][j % 2]  # Select the first or second value based on the column

            # Add the memory value inside each cell
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=value, font=("Arial", int(screen_width/192)))

    skip = 1