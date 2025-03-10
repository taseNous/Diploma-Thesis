import tkinter as tk, cycles, dependencies, gui_vars

from tkinter import messagebox
from vars import kPM, m

d_index = []
d_value = []
result1 = 0

def ALM(name, r1, r2, r3, d, i):

    global d_index, d_value, result1

    temp_reg1_add = cycles.temp_reg1_add
    temp_reg2_add = cycles.temp_reg2_add
    kpm_var = cycles.kpm_var
    depend_nop_array = dependencies.depend_nop_array
    index4 = dependencies.index4
    temp_reg_cycle_add = cycles.temp_reg_cycle_add

    if name == "ADD":  # ADD
        # if i in depend_nop_array or i in index4:
        if i-3 in temp_reg_cycle_add:
            index = temp_reg_cycle_add.index(i-2)
            value1 = temp_reg1_add[index]
            value2 = temp_reg2_add[index]
            result = hex(int(value1, 16) + int(value2, 16))[2:].upper()

        # Ensure the result is exactly 2 hex digits
        result = result.zfill(2)

        # Keep only the least significant 2 hex digits if result exceeds FF
        if len(result) > 2:
            result = result[-2:]

        if kpm_var == 2:
            r3[1] = result
        elif kpm_var == 1:
            kPM[1] = result
            result1 =kPM[1]

    elif name == "SUB":  # SUB
        if i in depend_nop_array or i in index4:
            result = int(temp_reg1_add[i-4], 16) - int(temp_reg2_add[i-4], 16)
        else:
            result = int(r1[1], 16) - int(r2[1], 16)

        # Ensure the result is not less than 0
        if result < 0:
            result = 0

        # Convert the result to hex and ensure it has 2 digits
        result = hex(result)[2:].upper().zfill(2)

        if kpm_var == 2:
            r3[1] = result
        elif kpm_var == 1:
            kPM[1] = result
            result1 =kPM[1]

    elif name == "AND":  # AND
        if i in depend_nop_array or i in index4:
            result = int(temp_reg1_add[i-4], 16) & int(temp_reg2_add[i-4], 16)
        else:
            result = int(r1[1], 16) & int(r2[1], 16)

        # Convert the result to hex and ensure it has 2 digits
        result = hex(result)[2:].upper().zfill(2)

        # Keep only the least significant 2 hex digits if result exceeds FF (unlikely for AND)
        if len(result) > 2:
            result = result[-2:]

        if kpm_var == 2:
            r3[1] = result
        elif kpm_var == 1:
            kPM[1] = result
            result1 =kPM[1]

    # elif name == "LOAD":  # LOAD
    #     success = False
    #     for y in range(16):
    #         x = m[y]
    #         if r2[1] == x[0]:
    #             r1[1] = x[1]
    #             success = True

    #     # If no matches were found in the LOAD operation, show an error and exit
    #     if not success:
    #         root = tk.Tk()
    #         root.withdraw()  # Hide the root window
    #         messagebox.showerror("Memory Error", "You have exceeded memory space")
    #         root.destroy()
    #         exit()

    # elif name == "STORE":  # STORE
    #     for y in range(16):
    #         x = m[y]
    #         if r2[1] == x[0]:
    #             x[1] = r1[1]