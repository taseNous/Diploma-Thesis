import grades, vars, dependencies, alm, method

from alm import ALM

from instr import namestr

from vars import (d, none, kAE, kEP, kPM, kAA, Data_Cache,
                  pb, ap0, pa, br, pg1, pg2, pg3, al0, al1, dmd1, gmd1, dmd2, gmd2, gk1, gk2, gk3,
                  var_counter1, var_counter2, var_counter3, var_counter4, var_counter5, pepe_falg,
                  m, m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, 
                  temp_reg1_load, temp_reg2_load, temp_reg_cycle_add, temp_reg_cycle_load, temp_reg_cycle_store, temp_reg1_add, temp_reg2_add,
                  temp_reg1_store, temp_reg2_store, r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, temp_reg1_bre, temp_reg2_bre, temp_reg_bre)

from gui_vars import Instr_Cache

bre_skip = 0
index = 0
kpm_var = 0
t = 0
q = 0
v = 0
pm_load1 = 0
pm_load2 = 0
pm_store1 = 0
pm_store2 = 0
bypass_add_array = []
bre_index = []
bre_index_pred = []
bre_pos_index = []
bre_array_not = []
d_value = []
Instr_Cache1 = []
bypass_add_var = 0
bp_add_var = 0
pe_flag = 0
ae_flag = 0
ep_flag = 0
pm_flag = 0
aa_flag = 0

def Clock_Cycles(x, y, i):

    global pb, ap0, pa, br, pg1, pg2, pg3, al0, al1, dmd1, gmd1, dmd2, gmd2, gk1, gk2, gk3, index
    global var_counter1, var_counter2, var_counter3, var_counter4, var_counter5, ae_flag, x_flag, t, q, v, pm_load1, pm_load2, pm_store1, pm_store2
    global pe_flag, pe1_flag, ep_flag, pm_flag, aa_flag, pepe_falg, ae_skip, aee_flag, ep_skip, pm_skip, aa_skip, bre_skip, kpm_var, bypass_add_var, bp_add_var
    global temp_reg_cycle_add, temp_reg_cycle_load, temp_reg1_add, temp_reg2_add, temp_reg1_load, temp_reg2_load, temp_reg_cycle_store, temp_reg1_store, temp_reg2_store
    global r0_start, r1_start, r2_start, r3_start, r4_start, r5_start, r6_start, r7_start, r8_start, r9_start, r10_start, r11_start, r12_start, r13_start, r14_start, r15_start

    # ae_flag = grades.ae_flag
    x_flag = grades.x_flag
    # pe_flag = grades.pe_flag
    pe1_flag = grades.pe1_flag
    # ep_flag = grades.ep_flag
    # pm_flag = grades.pm_flag
    # aa_flag = grades.aa_flag
    pe_skip = grades.pe_skip
    ae_skip = grades.ae_skip
    aee_flag = grades.aee_flag
    ep_skip = grades.ep_skip
    pm_skip = grades.pm_skip
    aa_skip = grades.aa_skip
    depend_nop_array = dependencies.depend_nop_array
    index_bypass_cycle = dependencies.index_bypass_cycle
    index_bypass_cycle1 = dependencies.index_bypass_cycle1
    index_bypass_cycle2 = dependencies.index_bypass_cycle2
    index3 = dependencies.index3
    index4 = dependencies.index4
    index5 = dependencies.index5
    index6 = dependencies.index6
    index7 = dependencies.index7
    index8 = dependencies.index8
    choose_bre = method.choose_bre
    choose = method.choose

    if i == 0:
        temp_reg_cycle_add.clear()
        temp_reg_cycle_load.clear()
        temp_reg_cycle_store.clear()
        temp_reg1_load.clear()
        temp_reg2_load.clear()
        temp_reg1_add.clear()
        temp_reg2_add.clear()
        temp_reg1_store.clear()
        temp_reg2_store.clear()
        temp_reg2_bre.clear()
        temp_reg1_bre.clear()
        index3.clear()
        index4.clear()
        index5.clear()
        index6.clear()
        index7.clear()
        index8.clear()
        t = 0
        v = 0
        q = 0
        index = 0
        pm_load1 = 0
        pm_load2 = 0
        pm_store1 = 0
        pm_store2 = 0
        bypass_add_var = 0
        bp_add_var = 0
        bre_index.clear()
        bre_array_not.clear()
        Instr_Cache1.clear()
        pe_flag = 0
        ae_flag = 0
        ep_flag = 0
        pm_flag = 0
        aa_flag = 0
        bre_pos_index.clear()
        d_value.clear()

        r0[1] = vars.r0_start[1]
        r1[1] = vars.r1_start[1]
        r2[1] = vars.r2_start[1]
        r3[1] = vars.r3_start[1]
        r4[1] = vars.r4_start[1]
        r5[1] = vars.r5_start[1]
        r6[1] = vars.r6_start[1]
        r7[1] = vars.r7_start[1]
        r8[1] = vars.r8_start[1]
        r9[1] = vars.r9_start[1]
        r10[1] = vars.r10_start[1]
        r11[1] = vars.r11_start[1]
        r12[1] = vars.r12_start[1]
        r13[1] = vars.r13_start[1]
        r14[1] = vars.r14_start[1]
        r15[1] = vars.r15_start[1]

        m0[1] = vars.m0_starter[1]
        m1[1] = vars.m1_starter[1]
        m2[1] = vars.m2_starter[1]
        m3[1] = vars.m3_starter[1]
        m4[1] = vars.m4_starter[1]
        m5[1] = vars.m5_starter[1]
        m6[1] = vars.m6_starter[1]
        m7[1] = vars.m7_starter[1]
        m8[1] = vars.m8_starter[1]
        m9[1] = vars.m9_starter[1]
        m10[1] = vars.m10_starter[1]
        m11[1] = vars.m11_starter[1]
        m12[1] = vars.m12_starter[1]
        m13[1] = vars.m13_starter[1]
        m14[1] = vars.m14_starter[1]
        m15[1] = vars.m15_starter[1]
        m16[1] = vars.m16_starter[1]
        m17[1] = vars.m17_starter[1]
        m18[1] = vars.m18_starter[1]
        m19[1] = vars.m19_starter[1]
        m20[1] = vars.m20_starter[1]
        m21[1] = vars.m21_starter[1]
        m22[1] = vars.m22_starter[1]
        m23[1] = vars.m23_starter[1]

    def validate_and_convert_hex(value):
        """
        Validates if the input value is a valid 2-digit hexadecimal number.
        Converts invalid values to '00'.

        Parameters:
            value (str): The input value to validate.

        Returns:
            str: A valid 2-digit hex string (e.g., '00' for invalid values).
        """
        try:
            # Attempt to convert to an integer with base 16
            int_value = int(value, 16)
            # Ensure it's within the valid range for 2-digit hex (00-FF)
            if 0 <= int_value <= 255:
                return hex(int_value)[2:].upper().zfill(2)  # Convert back to 2-digit hex string
        except (ValueError, TypeError):
            # Handle invalid input
            print(f"Invalid hex value: {value}. Converting to 00.")
        return "00"  # Return '00' for invalid or unexpected values


    var_counter4 = var_counter3 = var_counter2 = var_counter1 = 0
    ap0 = pa  = pg3 = gk3 = 0
    ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
    al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
    br = pb = 0
    #ΑΑ
    print("d")
    # print(d_index)
    print(d_value)
    if x>4:
        # print(aa_flag)
        var_counter4 = 0
        if aa_flag >= len(Instr_Cache):
            var_counter4 = 0
            ap0 = pa  = pg3 = gk3 = 0
            PE_print3 = "-----------------------Βαθμίδα ΑΑ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            aa_flag +=1 
        elif i - 4 in bre_array_not or i - 3 in bre_array_not or i - 4 in bre_index or i - 3 in bre_index or i-4 in index3 or i-3 in index4 or i-3 in index3 or i-3 in index5:
            var_counter4 = 0
            ap0 = pa  = pg3 = gk3 = 0
            AA_print11 = "-----------------------Βαθμίδα ΑΑ\n"
            AA_print12 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AA_print11)
            f.write(AA_print12)
            f.close()
            # aa_skip = 0
        elif i-3 in bre_index_pred or i-2 in bre_index_pred:
            var_counter4 = 0
            ap0 = pa  = pg3 = gk3 = 0
            AA_print11 = "-----------------------Βαθμίδα ΑΑ\n"
            AA_print12 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AA_print11)
            f.write(AA_print12)
            f.close()
            aa_flag += 1
        else:
            if i-4 in bre_index_pred:
                aa_flag += d_value[index]
            if i-5 in bre_index:
                aa_flag += d_value[index]
                index += 1
            if y+1 > len(Instr_Cache)-1:
                pass
            else:
                w6 = Instr_Cache[y+1]
                if w6 == "NOP":
                    ap0 = pa  = pg3 = gk3 = 0
            w5 = Instr_Cache[aa_flag]
            if w5.opcode == "0000000":
                var_counter4 = 0
                ap0 = pa  = pg3 = gk3 = 0
                nop_print11 = "-----------------------Βαθμίδα ΑΑ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                pg3 = gk3= 0
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w5.opcode == "0010000":
                if i-3 in bre_index or i-4 in bre_index:
                    var_counter4 = ap0 = pa  = pg3 = gk3 = 0
                else:
                    var_counter4 = 1
                    pg3 = 0
                    gk3= 1
                AA_print1 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", (" + namestr(w5.r2, globals()) + ")\n"
                AA_print2 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                if i-3 in bre_index or i-4 in bre_index or i-2 in bre_index_pred or i-3 in bre_index_pred:
                    kAA[0] = 0
                    kAA[1] = 0
                    kAA[2] = 0
                else:
                    #evresh twn dedomenwn sth mnhmh
                    for y in range(16):
                        n = m[y]
                        if temp_reg2_load[pm_load2] == n[0]:
                            w5.r1[1] = hex(int(n[1], 16))[2:].upper().zfill(2)                    
                    pm_load2 += 1
                    kAA[0] = w5.r1[1]
                    kAA[1] = namestr(w5.r1, globals()) + "." + w5.r1[0]
                    kAA[2] = 0
                AA_print3 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print4 = "⬆⬇️Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο κε, δηλαδή στον καταχωρητή " + namestr(w5.r1, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print1)
                f.write(AA_print2)
                f.write(AA_print3)
                f.write(AA_print4)
                f.close()
            elif w5.opcode == "0100000":
                if i-3 in bre_index:
                    var_counter4 = ap0 = pa  = pg3 = gk3 = 0
                else:
                    var_counter4= 1
                    pg3 = 2
                    gk3= 0
                AA_print5 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", (" + namestr(w5.r2, globals()) + ")\n"
                AA_print6 = "Η εντολή δε χρησιμοποιεί τη βαθμίδα.\n"
                if i-3 in bre_index or i-4 in bre_index or i-2 in bre_index_pred or i-3 in bre_index_pred:
                    kAA[0] = 0
                    kAA[1] = 0
                    kAA[2] = 0
                else:
                    for y in range(16):
                        pp = m[y]
                        if temp_reg2_store[pm_store2] == pp[0]:
                            pp[1] = hex(int(temp_reg1_store[pm_store1], 16))[2:].upper().zfill(2)
                pm_store1 += 1
                pm_store2 += 1
                kAA[0] = 0
                kAA[1] = 0
                kAA[2] = 0
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print5)
                f.write(AA_print6)
                f.close()
            elif w5.opcode == "0000001" or w5.opcode == "0000010" or w5.opcode == "0000011":
                if i-3 in bre_index:
                    var_counter4 = ap0 = pa  = pg3 = gk3 = 0
                else:
                    var_counter4 = 1
                    pg3 = gk3= 1
                AA_print9 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", " + namestr(w5.r2, globals()) + ", " + namestr(w5.r3, globals()) + "\n"
                AA_print10 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                kAA[0] = 0
                kAA[1] = namestr(w5.r3, globals()) + "." + w5.r3[0]
                if i-3 in bre_index or i-4 in bre_index or i-2 in bre_index_pred or i-3 in bre_index_pred:
                    kAA[0] = 0
                    kAA[1] = 0
                    kAA[2] = 0
                else:
                    if i-2 in index_bypass_cycle or i-1 in index_bypass_cycle1 or i-1 in index_bypass_cycle2:
                        if w5.name == "ADD":
                            kAA[2] = hex(int(temp_reg1_add[v], 16)+int(temp_reg2_add[v], 16))[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                        elif w5.name == "SUB":
                            kAA[2] = hex(int(w5.r1[1], 16) - int(w5.r2[1], 16))[2:].upper().zfill(2)
                            kAA[2] = validate_and_convert_hex(kAA[2])
                            try:
                                if int(kPM[1]) < 0:
                                    kAA[2] = 0
                            except ValueError:
                                kAA[2] = hex(0)[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                        elif w5.name == "AND":
                            kAA[2] = hex(int(w5.r1[1], 16) & int(w5.r2[1], 16))[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                    else:
                        if w5.name == "ADD":
                            kAA[2] = hex(int(temp_reg1_add[v], 16)+int(temp_reg2_add[v], 16))[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                        elif w5.name == "SUB":
                            kAA[2] = hex(int(temp_reg1_add[v], 16)-int(temp_reg2_add[v], 16))[2:].upper().zfill(2)
                            kAA[2] = validate_and_convert_hex(kAA[2])
                            try:
                                if int(kPM[1]) < 0:
                                    kAA[2] = 0
                            except ValueError:
                                kAA[2] = hex(0)[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                        elif w5.name == "AND":
                            kAA[2] = hex(int(temp_reg1_add[v], 16)&int(temp_reg2_add[v], 16))[2:].upper().zfill(2)
                            w5.r3[1] = kAA[2]
                    v += 1
                AA_print11 = "Το πεδίο κε του κΑΑ οδηγείται στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print12 = "⬇️Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο κε, δηλαδή στον καταχωρητή " + namestr(w5.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print9)
                f.write(AA_print10)
                f.write(AA_print11)
                f.write(AA_print12)
                f.close()
            elif w5.opcode == "1110000":
                var_counter4 = 1
                pg3 = 2
                gk3 = 0
                AA_print9 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", " + namestr(w5.r2, globals()) + ", d" + "\n"
                AA_print10 = "Η εντολή δε χρησιμοποιεί τη βαθμίδα.\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print9)
                f.write(AA_print10)
                f.close()
                kAA[0] = 0
                kAA[1] = 0
                kAA[2] = 0
            aa_flag += 1
        
        if i-2 in bre_index_pred or i-3 in bre_index_pred:
            kAA[0] = 0
            kAA[1] = 0
            kAA[2] = 0

    #ΠΜ
    print("d")
    # print(d_index)
    print(d_value)
    if x>3:
        # var_counter4 = var_counter5 = 0
        var_counter3 = 0
        if pm_flag >= len(Instr_Cache):
            var_counter3 = 0
            ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
            PE_print3 = "-----------------------Βαθμίδα ΠΜ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            pm_flag +=1 
        elif i - 2 in bre_array_not or i - 3 in bre_array_not or i - 2 in bre_index or i - 3 in bre_index or i-2 in index3 or i-2 in index4 or i-3 in index3 or i-2 in index5:
            var_counter3 = 0
            ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
            PM_print12 = "-----------------------Βαθμίδα ΠΜ\n"
            PM_print13 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PM_print12)
            f.write(PM_print13)
            f.close()
            # pm_skip = 0
        elif i-1 in bre_index_pred or i-2 in bre_index_pred:
            var_counter3 = 0
            ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
            PM_print12 = "-----------------------Βαθμίδα ΠΜ\n"
            PM_print13 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PM_print12)
            f.write(PM_print13)
            f.close()
            pm_flag += 1
        else:
            if i-3 in bre_index_pred:
                pm_flag += d_value[index]
            if i-4 in bre_index:
                pm_flag += d_value[index]
            w4 = Instr_Cache[pm_flag]
            if w4.opcode == "0000000":
                var_counter3 = 0
                ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
                nop_print11 = "-----------------------Βαθμίδα ΠΜ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w4.opcode == "0010000":
                if i-2 in bre_index or i-3 in bre_index:
                    var_counter3 = ap0 = pa = pg2 = dmd2 = gmd2 = gk2 = 0
                else:
                    var_counter3 = 1
                    pg2 = gmd2= 0
                    dmd2=gk2 = 1
                PM_print1 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", (" + namestr(w4.r2, globals()) + ")\n"
                PM_print2 = "Διαβάζεται το περιεχόμενο της θέσης μνήμης με διεύθυνση (" + namestr(w4.r2, globals()) + ")\n"
                try:
                    kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg1_load[pm_load1], 16))[2:].upper().zfill(2)
                except IndexError:
                    kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg1_load[-1], 16))[2:].upper().zfill(2)

                kPM[1] = 0
                try:
                    kPM[2] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg2_load[pm_load2], 16))[2:].upper().zfill(2)
                except IndexError:
                    kPM[2] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg2_load[-1], 16))[2:].upper().zfill(2)

                pm_load1 += 1
                kPM[3] = namestr(w4.r1, globals()) + "." + w4.r1[0]
                PM_print3 = "⬆️Αποθήκευση του δεδομένου που διαβάστηκε στο πεδίο δε του κΑΑ\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print1)
                f.write(PM_print2)
                f.write(PM_print3)
                f.close()
            elif w4.opcode == "0100000":
                if i-2 in bre_index or i-3 in bre_index:
                    var_counter3 = ap0 = pa = pg2 = pg3 = dmd2 = gmd2 = gk2 = gk3 = 0
                else:
                    var_counter3 = 1
                    pg2 = gmd2= 1
                    dmd2=gk2 = 0
                PM_print4 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", (" + namestr(w4.r2, globals()) + ")\n"
                PM_print5 = "Διαβάζεται το περιεχόμενο του καταχωρητή (" + namestr(w4.r1, globals()) + ")\n"
                kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg1_store[pm_store1], 16))[2:].upper().zfill(2)
                kPM[1] = 0
                kPM[2] = "(" + namestr(w4.r2, globals()) + ")" + "." + hex(int(temp_reg2_store[pm_store2], 16))[2:].upper().zfill(2)
                kPM[3] = 0
                PM_print6 = "⬆️Αποθήκευση του περιεχομένου που διαβάστηκε στη θέση μνήμης με διεύθυνση το περιεχόμενο του καταχωρητή (" + namestr(w4.r2, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print4)
                f.write(PM_print5)
                f.write(PM_print6)
                f.close()
            elif w4.opcode == "0000001" or w4.opcode == "0000010" or w4.opcode == "0000011":
                if i-2 in bre_index or i-3 in bre_index:
                    var_counter3 = ap0 = pa = pg2 = pg3 = dmd2 = gmd2 = gk2 = gk3 = 0
                else:
                    var_counter3 = 1
                    pg2 = gk2 = 1
                    dmd2= 2
                    gmd2= 0
                PM_print7 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", " + namestr(w4.r2, globals()) + ", " + namestr(w4.r3, globals()) + "\n"
                PM_print8 = "⬆️Μεταφορά αποτελέσματος απ από τον κΠΜ στον κΑΑ\n"
                # print("temp")
                # print(temp_reg1_add)
                # print(temp_reg2_add)
                if w4.name == "ADD":
                    try:
                        kPM[1] = hex(int(temp_reg1_add[t], 16) + int(temp_reg2_add[t], 16))[2:].upper().zfill(2)
                    except IndexError:
                        kPM[-1] = hex(int(temp_reg1_add[-1], 16) + int(temp_reg2_add[-1], 16))[2:].upper().zfill(2)

                elif w4.name == "SUB":
                    try:
                        kPM[1] = hex(int(temp_reg1_add[t], 16) - int(temp_reg2_add[t], 16))[2:].upper().zfill(2)
                    except IndexError:
                        kPM[1] = hex(int(temp_reg1_add[-1], 16) - int(temp_reg2_add[-1], 16))[2:].upper().zfill(2)

                    try:
                        if int(kPM[1]) < 0:
                            kPM[1] = 0
                    except ValueError:
                        kPM[1] = hex(0)[2:].upper().zfill(2)
                elif w4.name == "AND":
                    kPM[1] = hex(int(temp_reg1_add[t], 16)&int(temp_reg2_add[t], 16))[2:].upper().zfill(2)
                try:
                    kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg1_add[t], 16))[2:].upper().zfill(2)
                except IndexError:
                    kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + hex(int(temp_reg1_add[-1], 16))[2:].upper().zfill(2)

                try:
                    kPM[2] = "(" + namestr(w4.r2, globals()) + ")" + "." + hex(int(temp_reg2_add[t], 16))[2:].upper().zfill(2)
                except IndexError:
                    kPM[2] = "(" + namestr(w4.r2, globals()) + ")" + "." + hex(int(temp_reg2_add[-1], 16))[2:].upper().zfill(2)

                t += 1
                kPM[3] = "(" + namestr(w4.r3, globals()) + ")" + "." + w4.r3[0]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print7)
                f.write(PM_print8)
                f.close()
            elif w4.opcode == "1110000":
                var_counter3 = 1
                pg2 = 2
                dmd2 = 2
                gmd2 = 0
                gk2 = 0
                PM_print7 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", " + namestr(w4.r2, globals()) + ", d" + "\n"
                PM_print8 = "⬆️Μεταφορά αποτελέσματος απ από τον κΠΜ στον κΑΑ\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print7)
                f.write(PM_print8)
                f.close()
                kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + w4.r1[1]
                kPM[1] = w4.r1[1]
                kPM[2] = "(" + namestr(w4.r2, globals()) + ")" + "." + w4.r2[1]
                kPM[3] = 0
            pm_flag += 1

        if i-1 in bre_index_pred or i-2 in bre_index_pred:
            kPM[0] = 0
            kPM[1] = 0
            kPM[2] = 0
            kPM[3] = 0

    #ΕΠ
    print("d")
    # print(d_index)
    print(d_value)
    if x>2:
        # var_counter3 = var_counter4 = var_counter5 = 0
        var_counter2 = 0
        if ep_flag >= len(Instr_Cache):
            al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
            var_counter2 = 0
            PE_print3 = "-----------------------Βαθμίδα ΕΠ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            ep_flag +=1 
        elif i - 2 in bre_array_not or i-1 in bre_array_not or i - 2 in bre_index or i-1 in bre_index or i-1 in index3 or i-2 in index3 or i-1 in index4 or i-1 in index5:
            var_counter2 = 0
            al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
            EP_print00 = "-----------------------Βαθμίδα ΕΠ\n"
            EP_print01 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(EP_print00)
            f.write(EP_print01)
            f.close()
            ep_skip = 0
            # ep_flag += 1
        elif i in bre_index_pred or i-1 in bre_index_pred:
            var_counter2 = 0
            al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
            EP_print00 = "-----------------------Βαθμίδα ΕΠ\n"
            EP_print01 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(EP_print00)
            f.write(EP_print01)
            f.close()
            ep_skip = 0
            ep_flag += 1
        else:
            if i-2 in bre_index_pred:
                ep_flag += d_value[index]
            if i-3 in bre_index:
                ep_flag += d_value[index]
            w3 = Instr_Cache[ep_flag]
            if w3.opcode == "0000000":
                var_counter2 = 0
                al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
                nop_print11 = "-----------------------Βαθμίδα ΕΠ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w3.opcode == "0010000":
                if i-1 in bre_index or i-2 in bre_index:
                    al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
                else:
                    var_counter2 = 1
                    ap0 = pa = pg1 = gmd1 = 0
                    al0 = al1 = 2
                    dmd1 = gk1 = 1
                EP_print1 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", (" + namestr(w3.r2, globals()) + ")\n"
                EP_print2 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + ") και (" + namestr(w3.r2, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kEP[0] = "(" + namestr(w3.r1, globals()) + ")" + "." + w3.r1[1]
                kEP[1] = "(" + namestr(w3.r2, globals()) + ")" + "." + w3.r2[1]
                kEP[2] = namestr(w3.r1, globals()) + "." + w3.r1[0]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print1)
                f.write(EP_print2)
                f.close()
            elif w3.opcode == "0100000":
                if i-1 in bre_index or i-2 in bre_index:
                    al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
                else:
                    var_counter2 = 1
                    ap0 = pa = gmd1 = gk1 = 0
                    pg1 = gmd1 = 1
                    al0 = al1 = 2
                EP_print3 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", (" + namestr(w3.r2, globals()) + ")\n"
                EP_print4 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + ") και (" + namestr(w3.r2, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kEP[0] = "(" + namestr(w3.r1, globals()) + ")" + "." + w3.r1[1]
                kEP[1] = "(" + namestr(w3.r2, globals()) + ")" + "." + w3.r2[1]
                kEP[2] = 0
                
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print3)
                f.write(EP_print4)
                f.close()
            elif w3.opcode == "0000001" or w3.opcode == "0000010" or w3.opcode == "0000011":
                if i-1 in bre_index or i-2 in bre_index:
                    al0 = al1 = gk1 = dmd1 = gmd1 = pg1 = 0
                else:
                    var_counter2 = 1
                    ap0 = pa = al0 = gmd1 = 0
                    pg1 = al1 = gk1 = 1
                    dmd1 = 2
                EP_print5 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", " + namestr(w3.r2, globals()) + ", " + namestr(w3.r3, globals()) + "\n"
                EP_print6 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + "), (" + namestr(w3.r2, globals()) + ") και (" + namestr(w3.r3, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kEP[0] = "(" + namestr(w3.r1, globals()) + ")" + "." + w3.r1[1]
                kEP[1] = "(" + namestr(w3.r2, globals()) + ")" + "." + w3.r2[1]
                kEP[2] = namestr(w3.r3, globals()) + "." + w3.r3[0]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print5)
                f.write(EP_print6)
                f.close()
            elif w3.opcode == "1110000":
                var_counter2 = 1
                bre_skip = 1
                al1 = 0
                al0 = 1
                ap0 = pa = br = 2
                pg1 = 2
                dmd1 = 2
                gmd1 = 0
                gk1 = 0
                EP_print5 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", " + namestr(w3.r2, globals()) + ", d" + "\n"
                EP_print6 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + "), (" + namestr(w3.r2, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kEP[0] = "(" + namestr(w3.r1, globals()) + ")" + "." + w3.r1[1]
                kEP[1] = "(" + namestr(w3.r2, globals()) + ")" + "." + w3.r2[1]
                kEP[2] = 0
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print5)
                f.write(EP_print6)
                f.close()
            ep_flag += 1

        if i in bre_index_pred or i-1 in bre_index_pred:
            kEP[0] = 0
            kEP[1] = 0
            kEP[2] = 0

    #ΑΕ
    # print("ae_flag")
    # print(ae_flag)
    if x>1:
        var_counter1 = 0
        # var_counter2 = var_counter3 = var_counter4 = var_counter5 = 0
        if ae_flag >= len(Instr_Cache):
            br = pb = 0
            var_counter1 = 0
            PE_print3 = "-----------------------Βαθμίδα ΑΕ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            ae_flag +=1 

        elif i in bre_array_not or i-1 in bre_array_not:
            var_counter1 = 0
            # ae_flag += 1
            br = pb = 0
            AE_print1 = "-----------------------Βαθμίδα ΑΕ\n"
            AE_print2 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AE_print1)
            f.write(AE_print2)
            f.close()
            # ae_skip = 0
        
        elif i-1 in bre_index or i in bre_index or i in bre_index_pred:
            var_counter1 = 0
            # ae_flag += 1
            br = pb = 0
            AE_print1 = "-----------------------Βαθμίδα ΑΕ\n"
            AE_print2 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AE_print1)
            f.write(AE_print2)
            f.close()
            # ae_skip = 0
        else:
            if i-1 in bre_index_pred:
                ae_flag += d_value[index]
            w2 = Instr_Cache[ae_flag]
            if i-1 in index3 or i-2 in index3 or i-1 in index5 or i-1 in index4:
                pass
            else:
                Instr_Cache1.append({"name": w2.name, "opcode": w2.opcode, "r1": w2.r1, "r2": w2.r2, "r3": w2.r3})
                if choose == 1:
                    dependencies.depend_nop(i, q)
                if choose == 2:
                    dependencies.depend_freeze(i, q)
                if choose == 3:
                    dependencies.depend_bypassing_nop(i, q)
                if choose == 4:
                    dependencies.depend_bypassing_freeze(i, q)
            if i in index3 or i in index5 or i in index4:
                var_counter1 = 1
                # ae_flag += 1
                # w2 = Instr_Cache[ae_flag]
                br = pb = 0
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: ΑΕ' \nΑποκωδικοποίηση εντολής και έλεγχοι εξάρτησης." "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                # aee_flag = 0
                if w2.opcode == "0010000":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = 0 
                    kAE[0] = w2.opcode
                elif w2.opcode == "0100000":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = 0 
                    kAE[0] = w2.opcode
                elif w2.opcode == "0000001" or w2.opcode == "0000010" or w2.opcode == "0000011":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = namestr(w2.r3, globals()) + "." + w2.r3[0]
                    kAE[0] = w2.opcode
                # ae_flag -= 1
            elif i-1 in index3:
                var_counter1 = 1
                # ae_flag += 1
                # w2 = Instr_Cache[ae_flag]
                br = pb = 0
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: Χ \nΠάγωμα προσπέλασης νέας εντολής και ανάγνωσης των καταχωρητών γενικού σκοπού" "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                # x_flag = 0
                if w2.opcode == "0010000":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = 0 
                    kAE[0] = w2.opcode
                elif w2.opcode == "0100000":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = 0 
                    kAE[0] = w2.opcode
                elif w2.opcode == "0000001" or w2.opcode == "0000010" or w2.opcode == "0000011":
                    kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                    kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                    kAE[3] = namestr(w2.r3, globals()) + "." + w2.r3[0]
                    kAE[0] = w2.opcode
                    
                # ae_flag -= 1
            elif w2.opcode == "0000000":
                var_counter1 = 0
                br = pb = 0
                nop_print11 = "-----------------------Βαθμίδα ΑΕ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
                q += 1
                ae_flag += 1
            elif w2.opcode == "0010000":
                var_counter1 = 1
                br = pb = 0
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", (" + namestr(w2.r2, globals()) + ")\n"
                AE_print4 = "Αποκωδικοποίηση της εντολής\n"
                AE_print5 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής και έλεγχοι εξάρτησης τύπου ΑΜΕ\n"
                AE_print6 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print7 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print8 = "⬆️Αποθήκευση στον κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print9 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο α1 της εντολής\n"
                AE_print10 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                temp_reg_cycle_load.append(i)
                temp_reg1_load.append(w2.r1[1])
                temp_reg2_load.append(w2.r2[1])
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.write(AE_print4)
                f.write(AE_print5)
                f.write(AE_print6)
                f.write(AE_print7)
                f.write(AE_print8)
                f.write(AE_print9)
                f.write(AE_print10)
                f.close()
                # Instr_Cache1.append({"name": w2.name, "opcode": w2.opcode, "r1": w2.r1, "r2": w2.r2})
                # dependencies.depend_freeze(i, q)
                q += 1
                ae_flag += 1
            elif w2.opcode == "0100000":
                var_counter1 = 1
                br = pb = 0
                if i - 2 in bre_index or i - 3 in bre_index:
                    pb = 0
                else:
                    pb = 2
                AE_print11 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", (" + namestr(w2.r2, globals()) + ")\n"
                AE_print12 = "Αποκωδικοποίηση της εντολής\n"
                AE_print13 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής και έλεγχοι εξάρτησης τύπου ΑΜΕ\n"
                AE_print14 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print15 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print16 = "⬆️Αποθήκευση στον κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print17 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο α1 της εντολής\n"
                AE_print18 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                temp_reg_cycle_store.append(i)
                temp_reg1_store.append(w2.r1[1])
                temp_reg2_store.append(w2.r2[1])
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print11)
                f.write(AE_print12)
                f.write(AE_print13)
                f.write(AE_print14)
                f.write(AE_print15)
                f.write(AE_print16)
                f.write(AE_print17)
                f.write(AE_print18)
                f.close()
                # Instr_Cache1.append({"name": w2.name, "opcode": w2.opcode, "r1": w2.r1, "r2": w2.r2})
                # dependencies.depend_freeze(i, q)
                q += 1
                ae_flag += 1
            elif w2.opcode == "0000001" or w2.opcode == "0000010" or w2.opcode == "0000011":
                var_counter1 = 1
                br = pb = 0
                if i - 2 in bre_index or i - 3 in bre_index:
                    pb = 0
                else:
                    pb = 1
                AE_print19 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", " + namestr(w2.r2, globals()) + ", " + namestr(w2.r3, globals()) + "\n"
                AE_print20 = "Αποκωδικοποίηση της εντολής\n"
                AE_print21 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής και έλεγχοι εξάρτησης τύπου ΑΜΕ\n"
                AE_print22 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print23 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print24 = "⬆️Αποθήκευση στον κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print25 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο α1 της εντολής\n"
                AE_print26 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                temp_reg_cycle_add.append(i)
                print("temp_1")
                print("temp_2")
                temp_reg1_add.append(w2.r1[1])
                temp_reg2_add.append(w2.r2[1])

                print("temp")
                print(temp_reg1_add)
                print(temp_reg2_add)
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print19)
                f.write(AE_print20)
                f.write(AE_print21)
                f.write(AE_print22)
                f.write(AE_print23)
                f.write(AE_print24)
                f.write(AE_print25)
                f.write(AE_print26)
                f.close()
                # Instr_Cache1.append({"name": w2.name, "opcode": w2.opcode, "r1": w2.r1, "r2": w2.r2, "r3": w2.r3})
                # dependencies.depend_freeze(i, q)
                q += 1
                ae_flag += 1
            elif w2.opcode == "1110000":
                if int(w2.r1[1], 16) - int(w2.r2[1], 16) == 0:
                    # d_index.clear()
                    bre_pos_index.append(i)
                    # if i == bre_pos_index[0]:
                    #     d_value.clear()
                    # d_index.append(i)
                    # d_index = list(set(d_index))
                    d_value.append(int("".join(w2.d)))
                    # d_value = d_value[:len(d_index)]
                    print("d")
                    # print(d_index)
                    print(d_value)
                temp_reg_bre.append(i)
                temp_reg1_bre.append(w2.r1[1])
                temp_reg2_bre.append(w2.r2[1])
                if choose_bre == 1:
                    if int(w2.r1[1], 16) - int(w2.r2[1], 16) == 0:
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                        ae_flag += d_value[index]
                        # ep_flag += 1
                        # pm_flag += 1
                        # aa_flag += 1
                    elif int(w2.r1[1], 16) - int(w2.r2[1], 16) != 0:
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(w2.r1[1], 16) - int(w2.r2[1], 16) == 0:
                        sis2 = i+2
                        bre_index_pred.append(sis2)
                        print("bre_index_pred")
                        print(bre_index_pred)
                var_counter1 = 1
                # ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                if i - 2 in bre_index or i - 3 in bre_index:
                    pb = 0
                    br = 0
                else:
                    pb = 2
                    br = 1
                AE_print19 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", " + namestr(w2.r2, globals()) + ", d" + "\n"
                AE_print20 = "Αποκωδικοποίηση της εντολής\n"
                AE_print21 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής και έλεγχοι εξάρτησης τύπου ΑΜΕ\n"
                AE_print22 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print23 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print24 = "⬆️Αποθήκευση στον κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print25 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο α1 της εντολής\n"
                AE_print26 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                
                # print("peos")
                # print(w2.r1)
                # print(w2.r2)
                
                # ALM(w2.name, w2.r1, w2.r2, w2.r3, w2.d, i)
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print19)
                f.write(AE_print20)
                f.write(AE_print21)
                f.write(AE_print22)
                f.write(AE_print23)
                f.write(AE_print24)
                f.write(AE_print25)
                f.write(AE_print26)
                f.close()
                # Instr_Cache1.append({"name": w2.name, "opcode": w2.opcode, "r1": w2.r1, "r2": w2.r2})
                # dependencies.depend_freeze(i, q)
                q += 1
                ae_flag += 1
            if w2.opcode == "0010000":
                kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                kAE[3] = 0 
                kAE[0] = w2.opcode
            elif w2.opcode == "0100000":
                kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                kAE[3] = 0 
                kAE[0] = w2.opcode
            elif w2.opcode == "0000001" or w2.opcode == "0000010" or w2.opcode == "0000011":
                kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                kAE[3] = namestr(w2.r3, globals()) + "." + w2.r3[0]
                kAE[0] = w2.opcode
            elif w2.opcode == "1110000":
                kAE[1] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                kAE[2] = namestr(w2.r2, globals()) + "." + w2.r2[0]
                kAE[3] = d
                kAE[0] = w2.opcode
            if i in bre_index_pred:
                kAE[1] = 0
                kAE[2] = 0
                kAE[3] = 0
                kAE[0] = 0

    #ΠΕ
    print("pe_flag")
    print(pe_flag)
    if x>0:
        # var_counter1 = var_counter2 = var_counter3 = var_counter4 = var_counter5 = 0
        # if i in bre_array_not:
        #     pe_flag -= 1
        if pe_flag >= len(Instr_Cache):
            
            PE_print3 = "-----------------------Βαθμίδα ΠΕ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            pe_flag +=1 
        
        elif i -1 in index3 or i in index3 or i in index5 or i in index4:
            # var_counter1 = 0
            # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
            PE_print3 = "-----------------------Βαθμίδα ΠΕ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
        elif i-1 in bre_index:
            w1 = Instr_Cache[pe_flag]
            var_counter1 = 0
            pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
            PE_print1 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", (" + namestr(w1.r2, globals()) + ")\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print1)
            f.close()
            PE_print2 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
            PE_print3 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print2)
            f.write(PE_print3)
            f.close()
            PE_print3 = "⬆️Αποθήκευση της εντολής που προσκομίστηκε στον κΑΕ\n"
            PE_print4 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            print("poutsa")
            pe_flag += 1
        elif i-1 in bre_array_not:
            w1 = Instr_Cache[pe_flag]
            var_counter1 = 0
            pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
            PE_print1 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", (" + namestr(w1.r2, globals()) + ")\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print1)
            f.close()
            PE_print2 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
            PE_print3 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print2)
            f.write(PE_print3)
            f.close()
            PE_print3 = "⬆️Αποθήκευση της εντολής που προσκομίστηκε στον κΑΕ\n"
            PE_print4 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            pe_flag += 1
        else:
            w1 = Instr_Cache[pe_flag]
            if i+1 in bre_index_pred:
                pe_flag += d_value[index]
            if i in bre_index:
                pe_flag += d_value[index]
                
                var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                AE_print3 = "-----------------------Βαθμίδα ΠΕ: Χ \nΠάγωμα προσπέλασης νέας εντολής και ανάγνωσης των καταχωρητών γενικού σκοπού" "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                # x_flag = 0
            elif i in bre_array_not:
                print("peous")
                pe_flag -= 1
                var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                AE_print3 = "-----------------------Βαθμίδα ΠΕ: Χ \nΠάγωμα προσπέλασης νέας εντολής και ανάγνωσης των καταχωρητών γενικού σκοπού" "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                # x_flag = 0
                # pe_flag += 1
            elif w1.opcode == "0000000":
                # var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                nop_print11 = "-----------------------Βαθμίδα ΠΕ: NOP\n"
                nop_print22 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
                nop_print23 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
                nop_print24 = "⬆️Αποθήκευση της εντολής που προσκομίστηκε στον κΑΕ\n"
                nop_print25 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.write(nop_print23)
                f.write(nop_print24)
                f.write(nop_print25)
                f.close()
                pe_flag += 1
            elif w1.opcode == "0100000" or w1.opcode == "0010000":
                # var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                PE_print1 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", (" + namestr(w1.r2, globals()) + ")\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print1)
                f.close()
                PE_print2 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
                PE_print3 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print2)
                f.write(PE_print3)
                f.close()
                PE_print3 = "⬆️Αποθήκευση της εντολής που προσκομίστηκε στον κΑΕ\n"
                PE_print4 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print3)
                f.write(PE_print4)
                f.close()
                # Instr_Cache1.append({"name": w1.name, "opcode": w1.opcode, "r1": w1.r1, "r2": w1.r2})
                # dependencies.depend_freeze(i, q)
                print("poooooo")
                pe_flag += 1
            elif w1.opcode == "0000001" or w1.opcode == "0000010" or w1.opcode == "0000011":
                # var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                PE_print5 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", " + namestr(w1.r2, globals()) + ", " + namestr(w1.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print5)
                f.close()
                # kAE[0] = w1.opcode
                PE_print2 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
                PE_print3 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print2)
                f.write(PE_print3)
                f.close()
                PE_print3 = "⬆️Αποθήκευση της τιμής που προσκομίστηκε στον κΑΕ\n"
                PE_print4 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print3)
                f.write(PE_print4)
                f.close()
                # Instr_Cache1.append({"name": w1.name, "opcode": w1.opcode, "r1": w1.r1, "r2": w1.r2, "r3": w1.r3})
                # dependencies.depend_freeze(i, q)
                pe_flag += 1
            elif w1.opcode == "1110000":
                # var_counter1 = 0
                # pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 0
                PE_print5 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", " + namestr(w1.r2, globals()) + ", " + "d" + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print5)
                f.close()
                PE_print2 = "Προσκόμιση εντολής από την Κρυφή Μνήμη Εντολών\n"
                PE_print3 = "Υπολογισμός της τιμής Μετρητής Προγράμματος + 1 (ΜΠ+1)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print2)
                f.write(PE_print3)
                f.close()
                PE_print3 = "⬆️Αποθήκευση της τιμής που προσκομίστηκε στον κΑΕ\n"
                PE_print4 = "⬆️Αποθήκευση στον ΜΠ της τιμής ΜΠ+1\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print3)
                f.write(PE_print4)
                f.close()
                # Instr_Cache1.append({"name": w1.name, "opcode": w1.opcode, "r1": w1.r1, "r2": w1.r2})
                # dependencies.depend_freeze(i, q)
                # q += 1
                pe_flag += 1
            
            print("\n")

    if i in depend_nop_array:
        w2 = Instr_Cache[aa_flag-1]
        try:
            w1 = Instr_Cache[ae_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r1[1])
            elif w1.name =="LOAD":
                if w2.r1 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r1[1])
            elif w1.name == "STORE":
                if w2.r1 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r1[1])
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    dependencies.depend_bre_pred(i)
        if w2.name in ["ADD", "SUB", "AND"]:
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r3[1])
            elif w1.name =="LOAD":
                if w2.r3 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r3[1])
            elif w1.name == "STORE":
                if w2.r3 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r3[1])
            elif w1.name == "BRE":
                if w2.r3 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r3[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()

    if i in index_bypass_cycle:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[pm_flag-1]
        if w2.r3 == w1.r1:
            kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + str(kPM[1])
        if w2.r3 == w1.r2:
            kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + str(kPM[1])

    if i+1 in index_bypass_cycle1:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.r3 == w1.r1:
            w1.r1[1] = w2.r3[1]
        if w2.r3 == w1.r2:
            w1.r2[1] = w2.r3[1]

    if i-1 in index_bypass_cycle:
        try:
            w4 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w4 = Instr_Cache[-1]  # Defaults to the last element
        w5 = Instr_Cache[aa_flag-1]
        w4.r1[1] = validate_and_convert_hex(w4.r1[1])
        w4.r2[1] = validate_and_convert_hex(w4.r2[1])
        if w4.name == "ADD":
            kPM[1] = hex(int(w4.r1[1], 16) + int(w4.r2[1], 16))[2:].upper().zfill(2)
        elif w4.name == "SUB":
            kPM[1] = hex(int(w4.r1[1], 16) - int(w4.r2[1], 16))[2:].upper().zfill(2)
            try:
                if int(kPM[1]) < 0:
                    kPM[1] = 0
            except ValueError:
                kPM[1] = hex(0)[2:].upper().zfill(2)
            
        elif w4.name == "AND":
            kPM[1] = hex(int(w4.r1[1], 16) & int(w4.r2[1], 16))[2:].upper().zfill(2)

        if w5.r3 == w4.r1:
            kPM[0] = "(" + namestr(w4.r1, globals()) + ")" + "." + w5.r3[1]
        if w5.r3 == w4.r2:
            kPM[2] = "(" + namestr(w4.r2, globals()) + ")" + "." + w5.r3[1]

    if i in index_bypass_cycle1:
        try:
            w4 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w4 = Instr_Cache[-1]  # Defaults to the last element

        w5 = Instr_Cache[aa_flag-1]
        w4.r1[1] = validate_and_convert_hex(w4.r1[1])
        w4.r2[1] = validate_and_convert_hex(w4.r2[1])
        if w4.name == "ADD":
            kPM[1] = hex(int(w4.r1[1], 16) + int(w4.r2[1], 16))[2:].upper().zfill(2)
        elif w4.name == "SUB":
            kPM[1] = hex(int(w4.r1[1], 16) - int(w4.r2[1], 16))[2:].upper().zfill(2)
            try:
                if int(kPM[1]) < 0:
                    kPM[1] = 0
            except ValueError:
                kPM[1] = hex(0)[2:].upper().zfill(2)
            
        elif w4.name == "AND":
            kPM[1] = hex(int(w4.r1[1], 16) & int(w4.r2[1], 16))[2:].upper().zfill(2)

        try:
            w1 = Instr_Cache[pm_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.r3 == w1.r1:
            kPM[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r3[1]
        if w2.r3 == w1.r2:
            kPM[2] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r3[1]
    
    if i+1 in index_bypass_cycle1:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.r3 == w1.r1:
            kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r3[1]
        if w2.r3 == w1.r2:
            kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r3[1]

    if i in index_bypass_cycle2:
        try:
            w1 = Instr_Cache[ae_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r1[1])
            elif w1.name =="LOAD":
                if w2.r1 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r1[1])
            elif w1.name == "STORE":
                if w2.r1 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r1[1])
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()  
        if w2.name in ["ADD", "SUB", "AND"]:
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r3[1])
            elif w1.name =="LOAD":
                if w2.r3 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r3[1])
            elif w1.name == "STORE":
                if w2.r3 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r3[1])
            elif w1.name == "BRE":
                # print("poutsa")
                if w2.r3 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r3[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop() 

    if i in index6:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        print("peos")
        print(w1.name)
        print(ep_flag)
        if w2.name == "LOAD":
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r1[1]
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r1[1])
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r1[1]
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()

    if i-2 in index3:
        try:
            w1 = Instr_Cache[ae_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r1[1])
            elif w1.name =="LOAD":
                if w2.r1 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r1[1])
            elif w1.name == "STORE":
                if w2.r1 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r1[1])
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()
        if w2.name in ["ADD", "SUB", "AND"]:
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r3[1])
            elif w1.name =="LOAD":
                if w2.r3 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r3[1])
            elif w1.name == "STORE":
                if w2.r3 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg1_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r3[1])
            elif w1.name == "BRE":
                if w2.r3 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r3[1])
                    print("temp_reg2_bre")
                    print(temp_reg2_bre)
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()

    if i-1 in index5:
        try:
            w1 = Instr_Cache[ae_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r1[1])
            elif w1.name =="LOAD":
                if w2.r1 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r1[1])
            elif w1.name == "STORE":
                if w2.r1 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r1[1])
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                        
        if w2.name in ["ADD", "SUB", "AND"]:
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r3[1])
            elif w1.name =="LOAD":
                if w2.r3 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r3[1])
            elif w1.name == "STORE":
                if w2.r3 == w1.r1:
                    if temp_reg1_store:
                        temp_reg1_store.pop()
                    temp_reg1_store.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_store:
                        temp_reg2_store.pop()
                    temp_reg2_store.append(w2.r3[1])
            elif w1.name == "BRE" and ae_skip == 1:
                if w2.r3 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r3[1])
                if w2.r3 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r3[1])
                    print("temp_reg2_bre")
                    print(temp_reg2_bre)
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i+1)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i+1)
                        print("bre_array_not")
                        print(bre_array_not)
                        # print("poutsa")

    if i-2 in index4:
        try:
            w1 = Instr_Cache[ae_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop(t-1)
                    temp_reg1_add.insert(t, w2.r1[1])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop(t-1)
                    temp_reg2_add.insert(t, w2.r1[1])
                    kEP[1] = "(" + namestr(w2.r1, globals()) + ")" + "." + w2.r1[1]
            elif w1.name == "BRE":
                if w2.r1 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.append(w2.r1[1])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                if w2.r1 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(w2.r1[1])
                    kEP[1] = "(" + namestr(w2.r1, globals()) + ")" + "." + w2.r1[1]
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i)
                        index -= 1
                        pe_flag += d_value[index]
                        ae_flag += d_value[index]
                        # ep_flag += d_value[index]
                        # pm_flag += d_value[index]
                        # aa_flag += d_value[index]
                        d_value.append(int("".join(w1.d)))
                        print("d")
                        print(d_value)
                        print("bre_index")
                        print(bre_index)
                    elif int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop()

    if i in index7:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element
        w2 = Instr_Cache[aa_flag-1]
        if w2.name == "LOAD": 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r1 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop(t)
                    temp_reg1_add.insert(t, w2.r1[1])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                if w2.r1 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop(t)
                    temp_reg2_add.insert(t, w2.r1[1])
                    kEP[1] = "(" + namestr(w2.r1, globals()) + ")" + "." + w2.r1[1]
        if w2.name in ["ADD", "SUB", "AND"]: 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop(t)
                    temp_reg1_add.insert(t, w2.r3[1])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + w2.r1[1]
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(w2.r3[1])
                    kEP[1] = "(" + namestr(w2.r1, globals()) + ")" + "." + w2.r1[1]
        if w2.name == "LOAD": 
            if w1.name == "LOAD":
                if w2.r1 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r1[1])
                    kEP[0] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r1[1]
        if w2.name in ["ADD", "SUB", "AND"]: 
            if w1.name == "LOAD":
                if w2.r3 == w1.r2:
                    if temp_reg2_load:
                        temp_reg2_load.pop()
                    temp_reg2_load.append(w2.r3[1])
                    kEP[0] = "(" + namestr(w1.r2, globals()) + ")" + "." + w2.r1[1]

    if i in index8:
        try:
            w1 = Instr_Cache[ep_flag - 1]
        except IndexError:
            w1 = Instr_Cache[-1]  # Defaults to the last element

        w2 = Instr_Cache[pm_flag-1]
        if w2.name in ["ADD"]: 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop(t)
                    temp_reg1_add.insert(t, hex(int(w2.r1[1], 16) + int(w2.r2[1], 16))[2:].upper().zfill(2))
                    kEP[0] = "(" + namestr(w2.r1, globals()) + ")" + "." + hex(int(w2.r1[1], 16) + int(w2.r2[1], 16))[2:].upper().zfill(2)
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(hex(int(temp_reg1_add[v-1], 16) + int(temp_reg2_add[v-1], 16))[2:].upper().zfill(2))
                    print(temp_reg1_add)
                    print(temp_reg2_add)
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + hex(int(temp_reg1_add[v-1], 16)+int(temp_reg2_add[v-1], 16))[2:].upper().zfill(2)
            elif w1.name == "BRE":
                if w2.r3 == w1.r1:
                    if temp_reg1_bre:
                        temp_reg1_bre.pop()
                    temp_reg1_bre.insert(t, hex(int(w2.r1[1], 16) + int(w2.r2[1], 16))[2:].upper().zfill(2))
                    kEP[0] = "(" + namestr(w2.r1, globals()) + ")" + "." + hex(int(w2.r1[1], 16) + int(w2.r2[1], 16))[2:].upper().zfill(2)
                if w2.r3 == w1.r2:
                    if temp_reg2_bre:
                        temp_reg2_bre.pop()
                    temp_reg2_bre.append(hex(int(temp_reg1_add[v-1], 16) + int(temp_reg2_add[v-1], 16))[2:].upper().zfill(2))
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + hex(int(temp_reg1_add[v-1], 16)+int(temp_reg2_add[v-1], 16))[2:].upper().zfill(2)
                    print("temp_reg2_bre")
                    print(temp_reg2_bre)
                if choose_bre == 1:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) == 0:
                        if bre_index:
                            bre_index.pop()
                        if bre_array_not:
                            bre_array_not.pop()
                        bre_index.append(i)
                        print("bre_index")
                        print(bre_index)
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_array_not:
                            bre_array_not.pop()
                        if bre_index:
                            bre_index.pop()
                        bre_array_not.append(i)
                        print("bre_array_not")
                        print(bre_array_not)
                elif choose_bre == 2:
                    if int(temp_reg1_bre[-1], 16) - int(temp_reg2_bre[-1], 16) != 0:
                        if bre_index_pred:
                            bre_index_pred.pop(0)
        elif w2.name in ["SUB"]: 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(hex(int(w2.r1[1], 16) - int(w2.r2[1], 16))[2:].upper().zfill(2))
                    temp_reg1_add[-1] = validate_and_convert_hex(temp_reg1_add[-1])
                    kEP[0] = hex(int(w2.r1[1], 16) - int(w2.r2[1], 16))[2:].upper().zfill(2)
                    kEP[0] = validate_and_convert_hex(kEP[0])
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + kEP[0]
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(hex(int(w2.r1[1], 16) - int(w2.r2[1], 16))[2:].upper().zfill(2))
                    temp_reg2_add[-1] = validate_and_convert_hex(temp_reg2_add[-1])
                    kEP[1] = hex(int(w2.r1[1], 16) - int(w2.r2[1], 16))[2:].upper().zfill(2)
                    kEP[1] = validate_and_convert_hex(kEP[1])
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + kEP[1]
        if w2.name in ["AND"]: 
            if w1.name in ["ADD", "SUB", "AND"]:
                if w2.r3 == w1.r1:
                    if temp_reg1_add:
                        temp_reg1_add.pop()
                    temp_reg1_add.append(hex(int(w2.r1[1], 16) & int(w2.r2[1], 16))[2:].upper().zfill(2))
                    kEP[0] = "(" + namestr(w1.r1, globals()) + ")" + "." + hex(int(w2.r1[1], 16) & int(w2.r2[1], 16))[2:].upper().zfill(2)
                if w2.r3 == w1.r2:
                    if temp_reg2_add:
                        temp_reg2_add.pop()
                    temp_reg2_add.append(hex(int(w2.r1[1], 16) & int(w2.r2[1], 16))[2:].upper().zfill(2))
                    kEP[1] = "(" + namestr(w1.r2, globals()) + ")" + "." + hex(int(w2.r1[1], 16) & int(w2.r2[1], 16))[2:].upper().zfill(2)

    # ae_skip = 0
    # x_flag = 0
    # aee_flag = 0