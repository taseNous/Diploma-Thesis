import cycles

#ΠολυπλέκτηςΑ
def pipeline (canvas, screen_width, screen_height):
    
    pb = cycles.pb
    ap0 = cycles.ap0
    pa = cycles.pa
    br = cycles.br
    pg1 = cycles.pg1
    pg2 = cycles.pg2
    pg3 = cycles.pg3
    al0 = cycles.al0
    al1 = cycles.al1
    dmd1 = cycles.dmd1
    gmd1 = cycles.gmd1
    dmd2 = cycles.dmd2
    gmd2 = cycles.gmd2
    gk1 = cycles.gk1
    gk2 = cycles.gk2
    gk3 = cycles.gk3

    canvas.create_line(screen_width/14.75, screen_height/4.2, screen_width/14.75, screen_height/3.79)
    canvas.create_line(screen_width/19.2, screen_height/4.5, screen_width/19.2, screen_height/3.6)
    canvas.create_line(screen_width/19.2, screen_height/4.5, screen_width/14.75, screen_height/4.2)
    canvas.create_line(screen_width/19.2, screen_height/3.6, screen_width/14.75, screen_height/3.79)
    canvas.create_text(screen_width/15.6, screen_height/4, text="A", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/17.7, screen_height/4.1, text="1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/17.7, screen_height/3.9, text="0", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/24, screen_height/4.32, text="δδ", font=("Arial", int(screen_width/215)))
    #Γραμμή_ΠολυπλέκτηςΑ_ΜΠ
    canvas.create_line(screen_width/14.7, screen_height/4, screen_width/12.8, screen_height/4, arrow="last")
    #Γραμμή_ΠολυπλέκτηςΑ_κΑΕ
    canvas.create_line(screen_width/14.01, screen_height/4, screen_width/14.01, screen_height/2.138)
    canvas.create_line(screen_width/14.01, screen_height/2.138, screen_width/6, screen_height/2.138, arrow="last")
    #ΜΠ
    canvas.create_text(screen_width/11.63, screen_height/4, text="ΜΠ", font=("Arial", int(screen_width/215)))
    canvas.create_rectangle(screen_width/12.8, screen_height/4.7, screen_width/10.6, screen_height/3.48)
    #Γραμμή_ΜΠ_Κρυφή Μνήμη Δεδομένων
    canvas.create_line(screen_width/9.6, screen_height/3.6, screen_width/8.727, screen_height/3.6, arrow="last")
    #ΑθροιστήςΑ
    canvas.create_rectangle(screen_width/8, screen_height/2.84, screen_width/7.05, screen_height/2.34)
    canvas.create_text(screen_width/7.47, screen_height/2.57, text="A", font=("Arial", int(screen_width/215)))
    canvas.create_line(screen_width/8.93, screen_height/2.4, screen_width/8, screen_height/2.4, arrow="last")
    canvas.create_text(screen_width/9, screen_height/2.4, text="1", font=("Arial", int(screen_width/215)))
    #Γραμμή_ΜΠ_ΑθροιστήςΑ
    canvas.create_line(screen_width/10.549, screen_height/4, screen_width/9.6, screen_height/4)
    canvas.create_line(screen_width/9.6, screen_height/4, screen_width/9.6, screen_height/2.7)
    canvas.create_line(screen_width/9.6, screen_height/2.7, screen_width/8, screen_height/2.7, arrow="last")
    #Γραμμή_ΑθροιστήςΑ_ΠολυπλέκτηςΑ
    canvas.create_line(screen_width/7.05, screen_height/2.57, screen_width/6.5, screen_height/2.57)
    canvas.create_line(screen_width/6.5, screen_height/2.57, screen_width/6.5, screen_height/2.25)
    canvas.create_line(screen_width/23, screen_height/2.25, screen_width/6.5, screen_height/2.25)
    canvas.create_line(screen_width/23, screen_height/3.9, screen_width/23, screen_height/2.25)
    canvas.create_line(screen_width/23, screen_height/3.9, screen_width/19, screen_height/3.9, arrow="last")
    #Κρυφή Μνήμη Εντολών
    canvas.create_text(screen_width/7.38, screen_height/4.07, text="Κρυφή Μνήμη\n Εντολών", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.52, screen_height/3.6, text="είσοδος\nδιεύθυνσης", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/8.17, screen_height/4.67, text="αν", font=("Arial", int(screen_width/215)))
    canvas.create_rectangle(screen_width/8.7, screen_height/4.9, screen_width/6.4, screen_height/3.375)
    #κΑΕ
    canvas.create_rectangle(screen_width/6, screen_height/4.9, screen_width/5.6, screen_height/2.07)
    canvas.create_text(screen_width/5.783, screen_height/4.235, text="r1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/3.789, text="r2", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/2.734, text="r3", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/2.273, text="d", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/2.138, text="μπ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/2.018, text="κΑΕ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.783, screen_height/4.595, text="ΚΛ", font=("Arial", int(screen_width/215)))
    #Πολυπλέκτης Β
    canvas.create_line(screen_width/5.12, screen_height/3.08, screen_width/5.12, screen_height/2.63)
    canvas.create_line(screen_width/4.74, screen_height/2.97, screen_width/4.74, screen_height/2.72)
    canvas.create_line(screen_width/5.12, screen_height/3.08, screen_width/4.74, screen_height/2.97)
    canvas.create_line(screen_width/5.12, screen_height/2.63, screen_width/4.74, screen_height/2.72)
    canvas.create_text(screen_width/4.836, screen_height/2.827, text="B", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.987, screen_height/2.755, text="1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.987, screen_height/2.926, text="0", font=("Arial", int(screen_width/215)))
    #Γραμμή_Κρυφή Μνήμη Δεδομένων_κΑΕ
    canvas.create_line(screen_width/6.4, screen_height/3.661, screen_width/6, screen_height/3.661, arrow="last")
    #Γραμμή_κΑΕ_ΠολυπλέκτηςΒ
    canvas.create_line(screen_width/5.408, screen_height/4.235, screen_width/5.408, screen_height/2.926)
    canvas.create_line(screen_width/5.408, screen_height/2.926, screen_width/5.12, screen_height/2.926, arrow="last")
    canvas.create_line(screen_width/5.565, screen_height/2.755, screen_width/5.12, screen_height/2.755, arrow="last")
    #Γραμμή_ΠολυπλέκτηςΒ_κΕΠ
    canvas.create_line(screen_width/4.74, screen_height/2.827, screen_width/3.622, screen_height/2.827, arrow="last")
    canvas.create_text(screen_width/4.571, screen_height/2.918, text="κε", font=("Arial", int(screen_width/215)))
    #Καταχωρητές
    canvas.create_rectangle(screen_width/4.57, screen_height/4.9, screen_width/3.918, screen_height/3.17)
    canvas.create_text(screen_width/4.413, screen_height/4.235, text="δΑ1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.413, screen_height/3.789, text="δΑ2", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.413, screen_height/3.483, text="δΕ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.219, screen_height/3.272, text="Καταχωρητές", font=("Arial", int(screen_width/240)))
    canvas.create_text(screen_width/4.042, screen_height/4.075, text="ΔΑ1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.042, screen_height/3.661, text="ΔΑ2", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.363, screen_height/4.655, text="εε", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.085, screen_height/4.655, text="ΔΕ", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΑΕ_Καταχωρητές
    canvas.create_line(screen_width/5.597, screen_height/4.235, screen_width/4.571, screen_height/4.235, arrow="last")
    canvas.create_line(screen_width/5.597, screen_height/3.789, screen_width/4.571, screen_height/3.789, arrow="last")
    #Επέκταση Προσήμου
    canvas.create_rectangle(screen_width/5.26, screen_height/2.37, screen_width/4.26, screen_height/2.18)
    canvas.create_text(screen_width/4.705, screen_height/2.273, text="επέκταση\nπροσήμου", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΑΕ_Επέκταση
    canvas.create_line(screen_width/5.597, screen_height/2.273, screen_width/5.26, screen_height/2.273, arrow="last")
    #Γραμμή_Επέκταση_ΑθροιστήςΒ
    canvas.create_line(screen_width/4.26, screen_height/2.273, screen_width/4.042, screen_height/2.273, arrow="last")
    #Αθροιστής Β
    canvas.create_rectangle(screen_width/4.04, screen_height/2.4, screen_width/3.82, screen_height/2.03)
    canvas.create_text(screen_width/3.918, screen_height/2.204, text="B", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΑΕ_ΑθροιστήςΒ
    canvas.create_line(screen_width/5.647, screen_height/2.138, screen_width/4.042, screen_height/2.138, arrow="last")
    canvas.create_text(screen_width/4.682, screen_height/2.076, text="μπ", font=("Arial", int(screen_width/215)))
    #Γραμμή_ΑθροιστήςΒ_κΕΠ
    canvas.create_line(screen_width/3.801, screen_height/2.204, screen_width/3.622, screen_height/2.204, arrow="last")
    canvas.create_text(screen_width/3.713, screen_height/2.273, text="δδ", font=("Arial", int(screen_width/215)))
    #κΕΠ
    canvas.create_rectangle(screen_width/3.63, screen_height/12, screen_width/3.42, screen_height/2.07)
    canvas.create_text(screen_width/3.522, screen_height/4.075, text="(r1)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.522, screen_height/3.661, text="(r2)", font=("Arial", int(screen_width/215)))
    if br == 0:
        canvas.create_text(screen_width/3.522, screen_height/10.588, text="Br", font=("Arial", int(screen_width/215)), fill="red")
    elif br == 1:
        canvas.create_text(screen_width/3.522, screen_height/10.588, text="Br", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/10.588, text="Br", font=("Arial", int(screen_width/215)))
    if pg1 == 0:
        canvas.create_text(screen_width/3.522, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="red")
    elif pg1 == 1:
        canvas.create_text(screen_width/3.522, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.522, screen_height/2.827, text="κε", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.522, screen_height/2.204, text="δδ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.522, screen_height/2.018, text="κΕΠ", font=("Arial", int(screen_width/215)))
    if al1 == 0:
        canvas.create_text(screen_width/3.522, screen_height/4.864, text="ΑΛ1", font=("Arial", int(screen_width/215)), fill="red")
    elif al1 == 1:
        canvas.create_text(screen_width/3.522, screen_height/4.864, text="ΑΛ1", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/4.864, text="ΑΛ1", font=("Arial", int(screen_width/215)))
    if al0 == 0:
        canvas.create_text(screen_width/3.522, screen_height/5.346, text="ΑΛ0", font=("Arial", int(screen_width/215)), fill="red")
    elif al0 == 1:
        canvas.create_text(screen_width/3.522, screen_height/5.346, text="ΑΛ0", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/5.346, text="ΑΛ0", font=("Arial", int(screen_width/215)))
    if dmd1 == 0:
        canvas.create_text(screen_width/3.522, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)), fill="red")
    elif dmd1 == 1:
        canvas.create_text(screen_width/3.522, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)))
    if gmd1 == 0:
        canvas.create_text(screen_width/3.522, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)), fill="red")
    elif gmd1 == 1:
        canvas.create_text(screen_width/3.522, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)))
    if gk1 == 0:
        canvas.create_text(screen_width/3.522, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="red")
    elif gk1 == 1:
        canvas.create_text(screen_width/3.522, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/3.522, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)))
    #Γραμμή_Καταχωρητές_κΕΠ
    canvas.create_line(screen_width/3.918, screen_height/4.075, screen_width/3.622, screen_height/4.075, arrow="last")
    canvas.create_line(screen_width/3.918, screen_height/3.661, screen_width/3.622, screen_height/3.661, arrow="last")
    canvas.create_text(screen_width/3.764, screen_height/4.32, text="(r1)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.764, screen_height/3.857, text="(r2)", font=("Arial", int(screen_width/215)))
    #ΑΛΜ
    canvas.create_rectangle(screen_width/3.2, screen_height/4.59, screen_width/2.95, screen_height/3.32)
    canvas.create_text(screen_width/3.072, screen_height/3.857, text="ΑΛΜ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.887, screen_height/3.857, text="απ", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΕΠ_ΑΛΜ
    canvas.create_line(screen_width/3.428, screen_height/4.075, screen_width/3.2, screen_height/4.075, arrow="last")
    canvas.create_line(screen_width/3.428, screen_height/3.661, screen_width/3.2, screen_height/3.661, arrow="last")
    #Γραμμή_κΕΠ_ΠολυπλέκτηςΑ
    canvas.create_line(screen_width/3.428, screen_height/2.204, screen_width/3.31, screen_height/2.204)
    canvas.create_line(screen_width/3.31, screen_height/2.204, screen_width/3.31, screen_height/1.928)
    canvas.create_line(screen_width/32, screen_height/1.928, screen_width/3.31, screen_height/1.928)
    canvas.create_line(screen_width/32, screen_height/4.075, screen_width/32, screen_height/1.928)
    canvas.create_line(screen_width/32, screen_height/4.075, screen_width/19.2, screen_height/4.075, arrow="last")
    #κΠΜ
    canvas.create_rectangle(screen_width/2.82, screen_height/12, screen_width/2.69, screen_height/2.16)
    canvas.create_text(screen_width/2.754, screen_height/3.724, text="απ", font=("Arial", int(screen_width/215)))
    if pg2 == 0:
        canvas.create_text(screen_width/2.754, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="red")
    elif pg2 == 1:
        canvas.create_text(screen_width/2.754, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.754, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.754, screen_height/4.8, text="(r1)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.754, screen_height/3.272, text="(r2)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.754, screen_height/2.827, text="κε", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.754, screen_height/2.097, text="κΠΜ", font=("Arial", int(screen_width/215)))
    if dmd2 == 0:
        canvas.create_text(screen_width/2.754, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)), fill="red")
    elif dmd2 == 1:
        canvas.create_text(screen_width/2.754, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.754, screen_height/6.666, text="δΜΔ", font=("Arial", int(screen_width/215)))
    if gmd2 == 0:
        canvas.create_text(screen_width/2.754, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)), fill="red")
    elif gmd2 == 1:
        canvas.create_text(screen_width/2.754, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.754, screen_height/7.605, text="γΜΔ", font=("Arial", int(screen_width/215)))
    if gk2 == 0:
        canvas.create_text(screen_width/2.754, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="red")
    elif gk2 == 1:
        canvas.create_text(screen_width/2.754, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.754, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)))
    #Γραμμή_ΑΛΜ_κΠΜ
    canvas.create_line(screen_width/2.953, screen_height/3.661, screen_width/2.823, screen_height/3.661, arrow="last")
    #Γραμμή_κΕΠ_κΠΜ
    canvas.create_line(screen_width/3.31, screen_height/4.8, screen_width/3.31, screen_height/4.075)
    canvas.create_line(screen_width/3.31, screen_height/4.8, screen_width/2.823, screen_height/4.8, arrow="last")
    canvas.create_line(screen_width/3.31, screen_height/3.661, screen_width/3.31, screen_height/3.272)
    canvas.create_line(screen_width/3.31, screen_height/3.272, screen_width/2.823, screen_height/3.272, arrow="last")
    canvas.create_line(screen_width/3.428, screen_height/2.827, screen_width/2.823, screen_height/2.827, arrow="last")
    #Κρυφή Μνήμη Δεδομένων
    canvas.create_rectangle(screen_width/2.46, screen_height/5.6, screen_width/2.2, screen_height/3.085)
    canvas.create_text(screen_width/2.327, screen_height/4, text="Κρυφή\nΜνήμη\nΔεδομένων", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.327, screen_height/4.8, text="είσοδος\nδεδομένων", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.327, screen_height/3.272, text="είσοδος\nδιεύθυνσης", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.4, screen_height/5.268, text="αν", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.258, screen_height/5.268, text="εε", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΠΜ_Κρυφή Μνήμη Δεδομένων
    canvas.create_line(screen_width/2.685, screen_height/4.8, screen_width/2.461, screen_height/4.8, arrow="last")
    canvas.create_line(screen_width/2.685, screen_height/3.272, screen_width/2.461, screen_height/3.272, arrow="last")
    canvas.create_text(screen_width/2.635, screen_height/5.142, text="(r1)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.635, screen_height/3.428, text="(r2)", font=("Arial", int(screen_width/215)))
    #κΑΑ
    canvas.create_rectangle(screen_width/2.13, screen_height/12, screen_width/2.05, screen_height/2.18)
    canvas.create_text(screen_width/2.091, screen_height/2.117, text="κΑΑ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.091, screen_height/2.4, text="απ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.091, screen_height/2.827, text="κε", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.091, screen_height/4.075, text="δε", font=("Arial", int(screen_width/215)))
    if pg3 == 0:
        canvas.create_text(screen_width/2.091, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="red")
    elif pg3 == 1:
        canvas.create_text(screen_width/2.091, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.091, screen_height/5.934, text="πΓ", font=("Arial", int(screen_width/215)))
    if gk3 == 0:
        canvas.create_text(screen_width/2.091, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="red")
    elif gk3 == 1:
        canvas.create_text(screen_width/2.091, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.091, screen_height/8.852, text="γΚ", font=("Arial", int(screen_width/215)))
    #Γραμμή_Κρυφή Μνήμη Δεδομένων_κΑΑ
    canvas.create_line(screen_width/2.199, screen_height/4.075, screen_width/2.126, screen_height/4.075, arrow="last")
    canvas.create_text(screen_width/2.169, screen_height/4.32, text="δε", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΠΜ_κΑΑ
    canvas.create_line(screen_width/2.685, screen_height/3.724, screen_width/2.585, screen_height/3.724)
    canvas.create_line(screen_width/2.585, screen_height/3.724, screen_width/2.585, screen_height/2.4)
    canvas.create_line(screen_width/2.585, screen_height/2.4, screen_width/2.133, screen_height/2.4, arrow="last")
    canvas.create_line(screen_width/2.685, screen_height/2.827, screen_width/2.133, screen_height/2.827, arrow="last")
    #Πολυπλέκτης Γ
    canvas.create_line(screen_width/1.979, screen_height/4.5, screen_width/1.979, screen_height/3.48)
    canvas.create_line(screen_width/1.92, screen_height/4.15, screen_width/1.92, screen_height/3.72)
    canvas.create_line(screen_width/1.979, screen_height/4.5, screen_width/1.92, screen_height/4.15)
    canvas.create_line(screen_width/1.979, screen_height/3.48, screen_width/1.92, screen_height/3.72)
    canvas.create_text(screen_width/1.959, screen_height/4.075, text="0", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/1.959, screen_height/3.724, text="1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/1.933, screen_height/3.927, text="Γ", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΑΑ_ΠολυπλέκτηςΓ
    canvas.create_line(screen_width/2.049, screen_height/4.075, screen_width/1.979, screen_height/4.075, arrow="last")
    canvas.create_line(screen_width/2.049, screen_height/2.4, screen_width/2.004, screen_height/2.4)
    canvas.create_line(screen_width/2.004, screen_height/3.698, screen_width/2.004, screen_height/2.4)
    canvas.create_line(screen_width/2.004, screen_height/3.698, screen_width/1.979, screen_height/3.698, arrow="last")
    canvas.create_text(screen_width/2.021, screen_height/4.32, text="δε", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/1.979, screen_height/3.085, text="απ", font=("Arial", int(screen_width/215)))
    if pg3 == 0:
        canvas.create_text(screen_width/2.021, screen_height/6.352, text="πΓ", font=("Arial", int(screen_width/215)), fill="red")
    elif pg3 == 1:
        canvas.create_text(screen_width/2.021, screen_height/6.352, text="πΓ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.021, screen_height/6.352, text="πΓ", font=("Arial", int(screen_width/215)))
    #Γραμμή_κΑΑ_Καταχωρητές
    canvas.create_line(screen_width/2.046, screen_height/2.827, screen_width/1.837, screen_height/2.827)
    canvas.create_line(screen_width/1.837, screen_height/54, screen_width/1.837, screen_height/2.827)
    canvas.create_line(screen_width/4.8, screen_height/54, screen_width/1.837, screen_height/54)
    canvas.create_line(screen_width/4.8, screen_height/54, screen_width/4.8, screen_height/3.483)
    canvas.create_line(screen_width/4.8, screen_height/3.483, screen_width/4.571, screen_height/3.483, arrow="last")
    #Γραμμή_ΠολυπλέλτηςΓ_Καταχωρητές
    canvas.create_line(screen_width/1.92, screen_height/3.927, screen_width/1.882, screen_height/3.927)
    canvas.create_line(screen_width/1.882, screen_height/27, screen_width/1.882, screen_height/3.927)
    canvas.create_line(screen_width/4.085, screen_height/27, screen_width/1.882, screen_height/27)
    canvas.create_line(screen_width/4.085, screen_height/27, screen_width/4.085, screen_height/4.909, arrow="last")
    #Γραμμή Βαθμιδών
    canvas.create_line(screen_width/32, screen_height/1.8, screen_width/5.783, screen_height/1.8, arrow="both")
    canvas.create_line(screen_width/5.783, screen_height/1.8, screen_width/3.522, screen_height/1.8, arrow="both")
    canvas.create_line(screen_width/3.522, screen_height/1.8, screen_width/2.754, screen_height/1.8, arrow="both")
    canvas.create_line(screen_width/2.754, screen_height/1.8, screen_width/2.091, screen_height/1.8, arrow="both")
    canvas.create_line(screen_width/2.091, screen_height/1.8, screen_width/1.828, screen_height/1.8, arrow="both")
    canvas.create_text(screen_width/9.846, screen_height/1.846, text="ΠΕ (Βαθμίδα 1)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.363, screen_height/1.846, text="ΑΕ (Βαθμίδα 2)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/3.096, screen_height/1.846, text="ΕΠ (Βαθμίδα 3)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/2.385, screen_height/1.846, text="ΠΜ (Βαθμίδα 4)", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/1.949, screen_height/1.846, text="ΑΑ (Βαθμίδα 5)", font=("Arial", int(screen_width/215)))
    #Μονάδα Ελέγχου
    canvas.create_oval(screen_width/18, screen_height/36, screen_width/9, screen_height/7.2)
    canvas.create_text(screen_width/12, screen_height/12, text="Μονάδα Ελέγχου", font=("Arial", int(screen_width/215)))
    canvas.create_line(screen_width/12.387, screen_height/36, screen_width/8.347, screen_height/36, arrow="last")
    canvas.create_line(screen_width/9.846, screen_height/24, screen_width/8.347, screen_height/24, arrow="last")
    canvas.create_line(screen_width/9.365, screen_height/18, screen_width/8.347, screen_height/18, arrow="last")
    canvas.create_line(screen_width/9.142, screen_height/14.4, screen_width/8.347, screen_height/14.4, arrow="last")
    canvas.create_line(screen_width/9.014, screen_height/12, screen_width/8.347, screen_height/12, arrow="last")
    canvas.create_line(screen_width/9.142, screen_height/10.285, screen_width/8.347, screen_height/10.285, arrow="last")
    canvas.create_line(screen_width/9.365, screen_height/9, screen_width/8.347, screen_height/9, arrow="last")
    canvas.create_line(screen_width/9.846, screen_height/8, screen_width/8.347, screen_height/8, arrow="last")
    canvas.create_text(screen_width/7.836, screen_height/36, text="Br", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/24, text="δΜΔ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/18, text="γΜΔ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/14.4, text="πΓ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/12, text="ΑΛ0", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/10.285, text="ΑΛ1", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/9, text="γΚ", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/7.836, screen_height/8, text="πΒ", font=("Arial", int(screen_width/215)))
    #Γραμμ΄ή_κΑΕ_Μονάδα Ελέγχου
    canvas.create_line(screen_width/5.597, screen_height/4.595, screen_width/5.333, screen_height/4.595)
    canvas.create_line(screen_width/5.333, screen_height/7.2, screen_width/5.333, screen_height/4.595)
    canvas.create_line(screen_width/5.333, screen_height/7.2, screen_width/11.162, screen_height/7.2, arrow="last")
    canvas.create_text(screen_width/5.818, screen_height/6.545, text="ΚΛ", font=("Arial", int(screen_width/215)))
    #AND Πύλη
    canvas.create_arc(screen_width/3.31, screen_height/18, screen_width/3.096, screen_height/13.5, start=90, extent=180)
    canvas.create_line(screen_width/3.416, screen_height/10.588, screen_width/3.096, screen_height/10.588)
    canvas.create_line(screen_width/3.096, screen_height/14.4, screen_width/3.096, screen_height/10.588)
    canvas.create_line(screen_width/3.096, screen_height/14.4, screen_width/3.2, screen_height/14.4, arrow="last")
    canvas.create_line(screen_width/2.949, screen_height/4.5, screen_width/2.9, screen_height/4.5)
    canvas.create_line(screen_width/2.9, screen_height/16.615, screen_width/2.9, screen_height/4.5)
    canvas.create_line(screen_width/2.9, screen_height/16.615, screen_width/3.2, screen_height/16.615, arrow="last")
    if ap0 == 0:
        canvas.create_text(screen_width/2.823, screen_height/15.428, text="απ0", font=("Arial", int(screen_width/215)), fill="red")
    elif ap0 == 1:
        canvas.create_text(screen_width/2.823, screen_height/15.428, text="απ0", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/2.823, screen_height/15.428, text="απ0", font=("Arial", int(screen_width/215)))
    #Αριθμοί
    canvas.create_text(screen_width/10, screen_height/4.2, text="32", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/8.347, screen_height/1.963, text="32", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/6.736, screen_height/2.634, text="32", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/5.439, screen_height/2.347, text="17", font=("Arial", int(screen_width/215)))
    canvas.create_text(screen_width/4.146, screen_height/2.347, text="32", font=("Arial", int(screen_width/215)))
    #Διακεκομμένες Γραμμές
    canvas.create_line(screen_width/3.416, screen_height/8.852, screen_width/2.823, screen_height/8.852, dash=(1,1), arrow="last") #κΕΠ_γΚ
    canvas.create_line(screen_width/3.416, screen_height/7.605, screen_width/2.823, screen_height/7.605, dash=(1,1), arrow="last") #κΕΠ_γΜΔ
    canvas.create_line(screen_width/3.416, screen_height/6.666, screen_width/2.823, screen_height/6.666, dash=(1,1), arrow="last") #κΕΠ_δΜΔ
    canvas.create_line(screen_width/3.416, screen_height/5.934, screen_width/2.823, screen_height/5.934, dash=(1,1), arrow="last") #κΕΠ_πΓ
    canvas.create_line(screen_width/3.416, screen_height/5.346, screen_width/3, screen_height/5.346, dash=(1,1)) #κΕΠ_ΑΛΟ
    canvas.create_line(screen_width/3, screen_height/5.346, screen_width/3, screen_height/4.595, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/3.416, screen_height/4.864, screen_width/3.147, screen_height/4.864, dash=(1,1)) #κΕΠ_ΑΛ1
    canvas.create_line(screen_width/3.147, screen_height/4.864, screen_width/3.147, screen_height/4.595, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/2.685, screen_height/8.852, screen_width/2.133, screen_height/8.852, dash=(1,1), arrow="last") #κΠΜ_γΚ
    canvas.create_line(screen_width/2.685, screen_height/5.934, screen_width/2.133, screen_height/5.934, dash=(1,1), arrow="last") #κΠΜ_πΓ
    canvas.create_line(screen_width/2.685, screen_height/7.605, screen_width/2.258, screen_height/7.605, dash=(1,1)) #κΠΜ_γΜΔ
    canvas.create_line(screen_width/2.258, screen_height/7.605, screen_width/2.258, screen_height/5.684, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/2.685, screen_height/6.666, screen_width/2.4, screen_height/6.666, dash=(1,1)) #κΠΜ_δΜΔ
    canvas.create_line(screen_width/2.4, screen_height/6.666, screen_width/2.4, screen_height/5.684, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/2.042, screen_height/5.934, screen_width/1.949, screen_height/5.934, dash=(1,1)) #κΑΑ_πΓ
    canvas.create_line(screen_width/1.949, screen_height/5.934, screen_width/1.949, screen_height/4.32, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/2.042, screen_height/8.852, screen_width/2, screen_height/8.852, dash=(1,1)) #κΑΑ_γΚ
    canvas.create_line(screen_width/2, screen_height/21.6, screen_width/2, screen_height/8.852, dash=(1,1))
    canvas.create_line(screen_width/4.363, screen_height/21.6, screen_width/2, screen_height/21.6, dash=(1,1))
    canvas.create_line(screen_width/4.363, screen_height/21.6, screen_width/4.363, screen_height/4.909, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/3.84, screen_height/15.428, screen_width/3.31, screen_height/15.428, dash=(1,1)) #AND_ΠολυπλέκτηςΑ
    canvas.create_line(screen_width/3.84, screen_height/15.428, screen_width/3.84, screen_height/5.4, dash=(1,1))
    canvas.create_line(screen_width/16.695, screen_height/5.4, screen_width/3.84, screen_height/5.4, dash=(1,1))
    canvas.create_line(screen_width/16.695, screen_height/5.4, screen_width/16.695, screen_height/4.372, dash=(1,1), arrow="last")
    canvas.create_line(screen_width/4.91, screen_height/6, screen_width/4.91, screen_height/3.025, dash=(1,1), arrow="last") #πΒ_ΠολυπλέκτηςΒ
    canvas.create_line(screen_width/8.17, screen_height/6, screen_width/8.17, screen_height/4.909, dash=(1,1), arrow="last") #Κρυφή Μνήμη Εντολών_1
    canvas.create_text(screen_width/8.17, screen_height/6.171, text="1", font=("Arial", int(screen_width/215)))
    if pb == 0:
        canvas.create_text(screen_width/4.987, screen_height/6.171, text="πΒ", font=("Arial", int(screen_width/215)), fill="red")
    elif pb == 1:
        canvas.create_text(screen_width/4.987, screen_height/6.171, text="πΒ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/4.987, screen_height/6.171, text="πΒ", font=("Arial", int(screen_width/215)))
    if pa == 0:
        canvas.create_text(screen_width/19.2, screen_height/5.142, text="πΑ", font=("Arial", int(screen_width/215)), fill="red")
    elif pa == 1:
        canvas.create_text(screen_width/19.2, screen_height/5.142, text="πΑ", font=("Arial", int(screen_width/215)), fill="green")
    else:
        canvas.create_text(screen_width/19.2, screen_height/5.142, text="πΑ", font=("Arial", int(screen_width/215)))