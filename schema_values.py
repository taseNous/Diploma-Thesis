from gui_vars import (
    var1_kAE, var2_kAE, var3_kAE,
    var1_kEP, var2_kEP, var3_kEP,
    var1_kPM, var2_kPM, var3_kPM, var4_kPM,
    var1_kAA, var2_kAA, var3_kAA,
    var1_rf, var2_rf
)

from vars import kAE, kEP, kPM, kAA, Register_File

import cycles

def sch_values(canvas, screen_width, screen_height):

    var_counter1 = cycles.var_counter1
    var_counter2 = cycles.var_counter2
    var_counter3 = cycles.var_counter3
    var_counter4 = cycles.var_counter4
    var_counter5 = cycles.var_counter5

    if var_counter1 == 0:
        var1_kAE.set('r1')
        var2_kAE.set('r2')
        var3_kAE.set('r3')
    elif var_counter1 == 1:
        var1_kAE.set(kAE[1])
        var2_kAE.set(kAE[2])
        var3_kAE.set(kAE[3])
    if var_counter2 == 0:
        var1_kEP.set('(r1)')
        var2_kEP.set('(r2)')
        var3_kEP.set('κε')
    elif var_counter2 == 1:  
        var1_kEP.set(kEP[0])
        var2_kEP.set(kEP[1])
        var3_kEP.set(kEP[2])
    if var_counter3 == 0:
        var1_kPM.set('(r1)')
        var2_kPM.set('απ')
        var3_kPM.set('(r2)')
        var4_kPM.set('κε')
    elif var_counter3 == 1:
        var1_kPM.set(kPM[0])
        var2_kPM.set(kPM[1])
        var3_kPM.set(kPM[2])
        var4_kPM.set(kPM[3])
    if var_counter4 == 0:
        var1_kAA.set('δε')
        var2_kAA.set('κε')
        var3_kAA.set('απ')
    elif var_counter4 == 1:
        var1_kAA.set(kAA[0])
        var2_kAA.set(kAA[1])
        var3_kAA.set(kAA[2])
    if var_counter5 == 0:
        var1_rf.set('ΔΕ')
        var2_rf.set('δΕ')
    elif var_counter5 ==1:
        var1_rf.set(Register_File[0])
        var2_rf.set(Register_File[1])

    # Set the padding around the text
    padding_x = screen_width / 14
    padding_y = screen_height / 100
    
    # Determine the top-left and bottom-right coordinates of the rectangle
    x1 = screen_width / 1.6 - padding_x
    y1 = screen_height / 27 - padding_y
    x2 = screen_width / 1.6 + padding_x
    y2 = screen_height / 2.2 + padding_y
    
    # Draw the rectangle
    canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=1)

    # Text descriptions and associated variables
    text_info = [
        ("κΑΕ [r1, r2, r3]:", var1_kAE, screen_height/15),
        ("", var2_kAE, screen_height/10.691),
        ("", var3_kAE, screen_height/8.714),
        ("κΕΠ [(r1), (r2), κε]:", var1_kEP, screen_height/6.384),
        ("", var2_kEP, screen_height/5.623),
        ("", var3_kEP, screen_height/5),
        ("κΠΜ [(r1), απ, (r2), κε]:", var1_kPM, screen_height/4.1),
        ("", var2_kPM, screen_height/3.75),
        ("", var3_kPM, screen_height/3.476),
        ("", var4_kPM, screen_height/3.258),
        ("κΑΑ [δε, κε, απ]:", var1_kAA, screen_height/2.902),
        ("", var2_kAA, screen_height/2.754),
        ("", var3_kAA, screen_height/2.622),
        ("Καταχωρητές Γενικού Σκοπού [ΔΕ, δε]:", var1_rf, screen_height/2.4),
        ("", var2_rf, screen_height/2.3),
    ]

    # Header for the section
    canvas.create_text(
        screen_width/1.6, screen_height/27,
        text="Τιμές Καταχωρητών",
        font=("Arial", int(screen_width/160), "bold")
    )

    # Loop through the text_info list and create text elements on the canvas
    for description, var, position in text_info:
        if description:
            canvas.create_text(
                screen_width/1.6, position,
                text=description,
                font=("Arial", int(screen_width/160))
            )
        canvas.create_text(
            screen_width/1.6, position + screen_height/48,  # Adjust position slightly for the variable value
            text=var.get(),
            font=("Arial", int(screen_width/160))
        )