from instr import namestr
import cycles
from vars import r1, r2, r3, r4, none, choose
import gui_vars
import method

# Instr_Cache = cycles.Instr_Cache  # Assuming Instr_Cache is a list of Instruction objects
entolh_index = 0

def applytoLabel():
    global entolh_index

    Instr_Cache = gui_vars.Instr_Cache  # Assuming Instr_Cache is a list of Instruction objects

    if entolh_index > len(Instr_Cache) - 1:
        # print(f"Index {entolh_index} out of range.")
        return ""  # Return an empty string or handle the out-of-bounds case appropriately
    else:
        w = Instr_Cache[entolh_index]
        if w == "NOP":
            return w
        elif w.opcode in ["0000001", "0000010"]:
            r11 = namestr(w.r1, globals()) + ","
            r22 = "(" + namestr(w.r2, globals()) + ")"
            return f"{w.name} {r11} {r22}"
        elif w.opcode in ["0000011", "0000100", "0000101"]:
            r11 = namestr(w.r1, globals()) + ","
            r22 = namestr(w.r2, globals()) + ","
            r33 = namestr(w.r3, globals())
            return f"{w.name} {r11} {r22} {r33}"
        else:
            return w.name  # Default case if no match


def applytoLabel1(canvas, screen_width, screen_height, counter):
    global entolh_index

    choose = method.choose

    entolh_index = 0
    position_y = screen_height/7.4482

    if choose == 0:
        if counter > 5:
            entolh_index = entolh_index + counter - 5
        
    for i in range(counter):
        if i > 5:
            pass
        else:
            label_text = applytoLabel()
            if label_text == "":
                break  # Exit loop if out-of-bounds was encountered in applytoLabel
            canvas.create_text(screen_width/18.2857, position_y, text=label_text, font=("Arial", int(screen_width/192)))
            position_y += screen_height/36
            entolh_index += 1

    for i in range(counter):
        entolh_index -= 1
        position_y -= screen_height/36