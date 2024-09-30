from vars import counter_l, for_counter_l, choose
from gui_vars import position_x_l, Instr_Cache
import method

index = 0
skip_l = 0
loop_index = -1

def periodL():
    global index, skip_l

    if counter_l > len(Instr_Cache) + 4:
        pass
    else:
        x = "λ+" + str(index)
        return x

def periodL1(canvas, screen_width, screen_height, counter):
    global index, skip_l, position_x_l, loop_index

    choose = method.choose

    if choose == 0:
        if counter >=6:  
            position_x_l = screen_width/10.3783
            index = counter - 6
        elif counter < 6 and counter > 0:
            canvas.create_text(screen_width/10.3783, screen_height/9.3913, text="λ", font=("Arial", 10, 'bold'))
            position_x_l = screen_width/8.1702
            index = 0
    elif choose == 1:
        if counter >=9:  
            position_x_l = screen_width/10.3783
            index = counter - 6
        elif counter < 9 and counter > 0:
            canvas.create_text(screen_width/10.3783, screen_height/9.3913, text="λ", font=("Arial", 10, 'bold'))
            position_x_l = screen_width/8.1702
            index = 0

    if choose == 0:
        for i in range(counter-1):
            index = index + 1
            
            if i > 4:
                pass
            else:
                canvas.create_text(position_x_l, screen_height/9.3913, text=periodL(), font=("Arial", int(screen_width/192), 'bold'))
                position_x_l = position_x_l + screen_width/38.4
        
        for i in range(counter-1):
            index = index - 1
            if i >4:
                pass
            else:
                position_x_l = position_x_l - screen_width/38.4
        
    if choose == 1:
        for i in range(counter-1):
            index = index + 1
            
            if i > 8:
                pass
            else:
                canvas.create_text(position_x_l, screen_height/9.3913, text=periodL(), font=("Arial", int(screen_width/192), 'bold'))
                position_x_l = position_x_l + screen_width/38.4
        
        for i in range(counter-1):
            index = index - 1
            if i >4:
                pass
            else:
                position_x_l = position_x_l - screen_width/38.4