# Table with registers of pipelining in the top left canvas

import table_instructions, cycles

from gui_vars import (
    var1_kAE, var2_kAE, var3_kAE,
    var1_kEP, var2_kEP, var3_kEP,
    var1_kPM, var2_kPM, var3_kPM, var4_kPM,
    var1_kAA, var2_kAA, var3_kAA,
    var_kl, var_mp
)

from vars import kAE, kEP, kPM, kAA

def sch_values(canvas, screen_width, screen_height, i):

    var_counter1 = cycles.var_counter1
    var_counter2 = cycles.var_counter2
    var_counter3 = cycles.var_counter3
    var_counter4 = cycles.var_counter4
    entolh_index = table_instructions.entolh_index

    if i > 0:
        var_mp.set(entolh_index-1)
    else:
        var_mp.set('0')
    if var_counter1 == 0:
        var1_kAE.set('0')
        var2_kAE.set('0')
        var3_kAE.set('0')
        var_kl.set('0')
    elif var_counter1 == 1 and i >= 0:
        var1_kAE.set(kAE[1])
        var2_kAE.set(kAE[2])
        var3_kAE.set(kAE[3])
        var_kl.set(kAE[0])
    if var_counter2 == 0:
        var1_kEP.set('0')
        var2_kEP.set('0')
        var3_kEP.set('0')
    elif var_counter2 == 1 and i >= 0:  
        var1_kEP.set(kEP[0])
        var2_kEP.set(kEP[1])
        var3_kEP.set(kEP[2])
    if var_counter3 == 0:
        var1_kPM.set('0')
        var2_kPM.set('0')
        var3_kPM.set('0')
        var4_kPM.set('0')
    elif var_counter3 == 1 and i >= 0:
        var1_kPM.set(kPM[0])
        var2_kPM.set(kPM[1])
        var3_kPM.set(kPM[2])
        var4_kPM.set(kPM[3])
    if var_counter4 == 0:
        var1_kAA.set('0')
        var2_kAA.set('0')
        var3_kAA.set('0')
    elif var_counter4 == 1 and i >= 0:
        var1_kAA.set(kAA[0])
        var2_kAA.set(kAA[1])
        var3_kAA.set(kAA[2])

    # Set the padding around the text
    padding_x = screen_width / 14
    padding_y = screen_height / 100
    
    # Determine the top-left and bottom-right coordinates of the rectangle
    x1 = screen_width/1.536 - padding_x
    y1 = screen_height / 40 - padding_y
    x2 = screen_width/1.536 + padding_x
    y2 = screen_height / 2.25 + padding_y
    
    # Draw the rectangle
    canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=1)

    # Text descriptions and associated variables
    text_info = [
        ("Μετρητής Προγράμματος (ΜΠ):", var_mp, screen_height/15 - screen_height/72),
        ("κΑΕ [ΚΛ, κα1, κα2, κα3]:", var_kl, screen_height/15+screen_height/43.2),
        ("", var1_kAE, screen_height/15+screen_height/24),
        ("", var2_kAE, screen_height/10.691+screen_height/24),
        ("", var3_kAE, screen_height/8.714+screen_height/24),
        ("κΕΠ [(κα1), (κα2), κε]:", var1_kEP, screen_height/6.384+screen_height/24),
        ("", var2_kEP, screen_height/5.623+screen_height/24),
        ("", var3_kEP, screen_height/5+screen_height/24),
        ("κΠΜ [(κα1), απ, (κα2), κε]:", var1_kPM, screen_height/4.1+screen_height/24),
        ("", var2_kPM, screen_height/3.75+screen_height/24),
        ("", var3_kPM, screen_height/3.476+screen_height/24),
        ("", var4_kPM, screen_height/3.258+screen_height/24),
        ("κΑΑ [δε, κε, απ]:", var1_kAA, screen_height/2.902+screen_height/24),
        ("", var2_kAA, screen_height/2.754+screen_height/24),
        ("", var3_kAA, screen_height/2.622+screen_height/24)
    ]

    # Header for the section
    canvas.create_text(
        screen_width/1.536, screen_height/27 - screen_height/72,
        text="Τιμές Καταχωρητών",
        font=("Arial", int(screen_width/174), "bold")
    )

    # Loop through the text_info list and create text elements on the canvas
    for description, var, position in text_info:
        if description:
            canvas.create_text(
                screen_width/1.536, position,
                text=description,
                font=("Arial", int(screen_width/174))
            )
        canvas.create_text(
            screen_width/1.536, position + screen_height/48,  # Adjust position slightly for the variable value
            text=var.get(),
            font=("Arial", int(screen_width/174))
        )