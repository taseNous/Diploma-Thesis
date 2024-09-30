from vars import index1, index2, index3, index4, index5, indexx, bp_index, freeze_array

from gui_vars import (position_x1, position_x2, position_x3, position_x4, position_x5,
                     position_y1, position_y2, position_y3, position_y4, position_y5)

from instr import Enquiry

import gui_vars

x_flag = 0
aee_flag = 0
pe_skip = 0
ae_skip = 0
ep_skip = 0
pm_skip = 0
aa_skip = 0

#Βαθμίδες
def vathmides(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5, freeze_array
    global ae_flag, ep_flag, pm_flag, aa_flag, pe_flag, pe_skip, ae_skip, ep_skip, pm_skip, aa_skip

    Instr_Cache = gui_vars.Instr_Cache

    pe_skip = 0
    ae_skip = 0
    ep_skip = 0
    pm_skip = 0
    aa_skip = 0

    if i == 0:
        pe_flag = -1
        ae_flag = -1
        ep_flag = -1
        pm_flag = -1
        aa_flag = -1

    if pe_flag >= len(Instr_Cache)-1:
        pe_skip = 1
    else:
        canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", 10))
        position_x1 = position_x1 + screen_width/38.4
        position_y1 = position_y1 + screen_height/36
        pe_flag = pe_flag + 1
            
    if i >= 1:
        if ae_flag >= len(Instr_Cache)-1:
            ae_skip = 1
        elif i >= 5:
            ae_flag = ae_flag + 1
        else:
            canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", 10))
            position_x2 = position_x2 + screen_width/38.4
            position_y2 = position_y2 + screen_height/36
            ae_flag = ae_flag + 1
            
    if i >= 2:
        if ep_flag >= len(Instr_Cache)-1:
            ep_skip = 1
        elif i >= 5:
            ep_flag = ep_flag  + 1
        else:
            canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", 10))
            position_x3 = position_x3 + screen_width/38.4
            position_y3 = position_y3 + screen_height/36
            ep_flag = ep_flag  + 1
                
    if i >= 3:
        if pm_flag >= len(Instr_Cache)-1:
            pm_skip = 1
        elif i >= 5:
            pm_flag = pm_flag + 1
        else:
            canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", 10))
            position_x4 = position_x4 + screen_width/38.4
            position_y4 = position_y4 + screen_height/36
            pm_flag = pm_flag + 1
                
    if i >= 4:
        if aa_flag >= len(Instr_Cache)-1:
            aa_skip = 1
        elif i >= 5:
            aa_flag = aa_flag + 1
        else:
            canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", 10))
            position_x5 = position_x5 + screen_width/38.4
            position_y5 = position_y5 + screen_height/36
            aa_flag = aa_flag + 1
            
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

def vathmides1(canvas, screen_width, screen_height, z, i):

    global position_x1, position_x2, position_x3, position_x4, position_x5, position_y1, position_y2, position_y3, position_y4, position_y5, index1, index2, index3, index4, index5, indexx
    global bp_index, ae_flag, x_flag, ep_flag, pm_flag, aa_flag, pe_flag, pe_skip, aee_flag, ae_skip, ep_skip, pm_skip, aa_skip

    Instr_Cache = gui_vars.Instr_Cache

    counterr = 5
    x_flag = 0
    aee_flag = 0
    pe_skip = 0
    ae_skip = 0
    ep_skip = 0
    pm_skip = 0
    aa_skip = 0

    if i == 0:
        pe_flag = -1
        ae_flag = -1
        ep_flag = -1
        pm_flag = -1
        aa_flag = -1

    if i >= 0:
        indexx = indexx + 1
        if Enquiry(index2):
            if i+1 in index3 or i+2 in index3:
                position_x1 = position_x1 + screen_width/38.4
                pe_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 1:
                    pe_skip = 1
                else:
                    if counterr <= 5:
                        canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width/192)))
                        position_x1 = position_x1 + screen_width/38.4
                        position_y1 = position_y1 + screen_height/36
                        counterr = counterr - 1
                        pe_flag = pe_flag + 1
        else:
            if i+1 in index5:
                position_x1 = position_x1 + screen_width/38.4
                pe_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index4):
                    pe_skip = 1
                else:
                    if counterr <= 5:
                        canvas.create_text(position_x1, position_y1, text="ΠΕ", font=("Arial", int(screen_width/192)))
                        position_x1 = position_x1 + screen_width/38.4
                        position_y1 = position_y1 + screen_height/36
                        counterr = counterr - 1
                        pe_flag = pe_flag + 1

    if i >= 1:
        indexx = indexx + 1
        if Enquiry(index2):
            if i-1 in index2:
                canvas.create_text(position_x2, position_y2, text="ΑΕ'", font=("Arial", int(screen_width/192)))
                position_x2 = position_x2 + screen_width/38.4
                aee_flag = 1
            elif i-2 in index2:
                if bp_index <= len(index1)-1:
                    if index1[bp_index] == "1":
                        canvas.create_text(position_x2, position_y2, text="Χ", font=("Arial", int(screen_width/192)))
                        position_x2 = position_x2 + screen_width/38.4
                        x_flag = 1
                bp_index = bp_index + 1
            else:
                if i >= len(Instr_Cache) + len(index2)+2:
                    ae_skip = 1
                else:
                    canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                    position_x2 = position_x2 + screen_width/38.4
                    position_y2 = position_y2 + screen_height/36
                    ae_flag = ae_flag + 1
        else:
            if i+1 in index5:
                canvas.create_text(position_x2, position_y2, text="ΑΕ'", font=("Arial", int(screen_width/192)))
                position_x2 = position_x2 + screen_width/38.4
                aee_flag = 1
            else:
                if i >= len(Instr_Cache) + len(index4) + 1:
                    ae_skip = 1
                else:
                    if i+1 in index5:
                        ae_skip = 1
                    else:
                        canvas.create_text(position_x2, position_y2, text="ΑΕ", font=("Arial", int(screen_width/192)))
                        position_x2 = position_x2 + screen_width/38.4
                        position_y2 = position_y2 + screen_height/36
                        ae_flag = ae_flag + 1

    bp_index = 0
    
    if i >= 2:
        indexx = indexx + 1
        if Enquiry(index2):
            if i+1 in index3 or i in index3:
                position_x3 = position_x3 + screen_width/38.4
                ep_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 3:
                        ep_skip = 1
                else:
                    canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                    position_x3 = position_x3 + screen_width/38.4
                    position_y3 = position_y3 + screen_height/36
                    ep_flag = ep_flag + 1
        else:
            if i in index5:
                position_x3 = position_x3 + screen_width/38.4
                ep_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 3:
                        ep_skip = 1
                else:
                    canvas.create_text(position_x3, position_y3, text="ΕΠ", font=("Arial", int(screen_width/192)))
                    position_x3 = position_x3 + screen_width/38.4
                    position_y3 = position_y3 + screen_height/36
                    ep_flag = ep_flag + 1
    
    if i >= 3:
        indexx = indexx + 1
        if Enquiry(index2):
            if i in index3 or i-1 in index3:
                position_x4 = position_x4 + screen_width/38.4
                pm_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 4:
                    pm_skip = 1
                else:
                    canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                    position_x4 = position_x4 + screen_width/38.4
                    position_y4 = position_y4 + screen_height/36
                    pm_flag = pm_flag + 1
        else:
            if i-1 in index5:
                position_x4 = position_x4 + screen_width/38.4
                pm_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 4:
                    pm_skip = 1
                else:
                    canvas.create_text(position_x4, position_y4, text="ΠΜ", font=("Arial", int(screen_width/192)))
                    position_x4 = position_x4 + screen_width/38.4
                    position_y4 = position_y4 + screen_height/36
                    pm_flag = pm_flag + 1

    if i >= 4:
        indexx = indexx + 1
        if Enquiry(index2):
            if i-2 in index3 or i-1 in index3:
                position_x5 = position_x5 + screen_width/38.4
                aa_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 5:
                    aa_skip = 1
                else:
                    canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                    position_x5 = position_x5 + screen_width/38.4
                    position_y5 = position_y5 + screen_height/36
                    aa_flag = aa_flag + 1
        else:
            if i-2 in index5:
                position_x5 = position_x5 + screen_width/38.4
                aa_skip = 1
            else:
                if i >= len(Instr_Cache) + len(index2) + 5:
                    aa_skip = 1
                else:
                    canvas.create_text(position_x5, position_y5, text="ΑΑ", font=("Arial", int(screen_width/192)))
                    position_x5 = position_x5 + screen_width/38.4
                    position_y5 = position_y5 + screen_height/36
                    aa_flag = aa_flag + 1

    indexx = 1

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