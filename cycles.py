from alm import ALM

from instr import namestr

from vars import (r0, r1, r2, r3, r4, r5, r6, r7, none, kAE, kEP, kPM, kAA, Data_Cache, Register_File,
                  pb, ap0, pa, br, pg1, pg2, pg3, al0, al1, dmd1, gmd1, dmd2, gmd2, gk1, gk2, gk3,
                  var_counter1, var_counter2, var_counter3, var_counter4, var_counter5, pepe_falg,
                  m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, temp_reg1, temp_reg2)

import grades
import vars
from gui_vars import Instr_Cache

def Clock_Cycles(x, y, i):

    global pb, ap0, pa, br, pg1, pg2, pg3, al0, al1, dmd1, gmd1, dmd2, gmd2, gk1, gk2, gk3 
    global var_counter1, var_counter2, var_counter3, var_counter4, var_counter5, ae_flag, x_flag, pe_flag, ep_flag, pm_flag, aa_flag, pepe_falg, ae_skip, aee_flag, ep_skip, pm_skip, aa_skip, temp_reg1, temp_reg2

    ae_flag = grades.ae_flag
    x_flag = grades.x_flag
    pe_flag = grades.pe_flag
    ep_flag = grades.ep_flag
    pm_flag = grades.pm_flag
    aa_flag = grades.aa_flag
    pe_skip = grades.pe_skip
    ae_skip = grades.ae_skip
    aee_flag = grades.aee_flag
    ep_skip = grades.ep_skip
    pm_skip = grades.pm_skip
    aa_skip = grades.aa_skip

    if i == 0:
        r0[1] = vars.r0_start[1]
        r1[1] = vars.r1_start[1]
        r2[1] = vars.r2_start[1]
        r3[1] = vars.r3_start[1]
        r4[1] = vars.r4_start[1]
        r5[1] = vars.r5_start[1]
        r6[1] = vars.r6_start[1]
        r7[1] = vars.r7_start[1]

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

    if x>0:
        if pe_skip == 1:
            var_counter1 = 0
            pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
            PE_print3 = "-----------------------Βαθμίδα ΠΕ\n"
            PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PE_print3)
            f.write(PE_print4)
            f.close()
            pe_skip = 0
        elif pe_flag >= 0:
            w1 = Instr_Cache[pe_flag]
            if w1.opcode == "0000000":
                var_counter1 = 0
                pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
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
            elif w1.opcode == "0000001" or w1.opcode == "0000010":
                var_counter1 = 1
                pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
                PE_print1 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", (" + namestr(w1.r2, globals()) + ")\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print1)
                f.close()
                kAE[0] = w1.opcode
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
            elif w1.opcode == "0000011":
                var_counter1 = 1
                pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
                PE_print5 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", " + namestr(w1.r2, globals()) + ", " + namestr(w1.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print5)
                f.close()
                kAE[0] = w1.opcode
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
            elif w1.opcode == "0000100":
                var_counter1 = 1
                pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
                PE_print5 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", " + namestr(w1.r2, globals()) + ", " + namestr(w1.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print5)
                f.close()
                kAE[0] = w1.opcode
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

            elif w1.opcode == "0000101":
                var_counter1 = 1
                pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 = dmd2 = gmd2 = gk1 = gk2 = gk3 = 2
                PE_print5 = "-----------------------Βαθμίδα ΠΕ: " + str(w1.name) + " " + namestr(w1.r1, globals()) + ", " + namestr(w1.r2, globals()) + ", " + namestr(w1.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PE_print5)
                f.close()
                kAE[0] = w1.opcode
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
            if w1.opcode == "0000001":
                kAE[1] = namestr(w1.r1, globals()) + "." + w1.r1[0]
                kAE[2] = namestr(w1.r2, globals()) + "." + w1.r2[0]
                kAE[3] = 0 
            elif w1.opcode == "0000010":
                kAE[1] = namestr(w1.r1, globals()) + "." + w1.r1[0]
                kAE[2] = namestr(w1.r2, globals()) + "." + w1.r2[0]
                kAE[3] = 0 
            elif w1.opcode == "0000011":
                kAE[1] = namestr(w1.r1, globals()) + "." + w1.r1[0]
                kAE[2] = namestr(w1.r2, globals()) + "." + w1.r2[0]
                kAE[3] = namestr(w1.r3, globals()) + "." + w1.r3[0]
            print("\n")
    if x>1:
        if ae_skip == 1:
            var_counter2 = 0
            pb = 2
            AE_print1 = "-----------------------Βαθμίδα ΑΕ\n"
            AE_print2 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AE_print1)
            f.write(AE_print2)
            f.close()
            ae_skip = 0
        elif ae_flag >=0:
            w2 = Instr_Cache[ae_flag]
            if aee_flag == 1:
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: ΑΕ' \nΑποκωδικοποίηση εντολής και έλεγχοι που χρειάζονται για να διαπιστωθεί ότι απαιτείται η ανάγνωση καταχωρητή που δεν έχει τα σωστά νέα δεδομένα" "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                aee_flag = 0
            elif x_flag == 1:
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: Χ \nΠάγωμα προσπέλασης νέας εντολής και ανάγνωσης των καταχωρητών γενικού σκοπού" "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AE_print3)
                f.close()
                x_flag = 0
            elif w2.opcode == "0000000":
                var_counter2 = 0
                pb = 0
                nop_print11 = "-----------------------Βαθμίδα ΑΕ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w2.opcode == "0000001":
                var_counter2 = 1
                pb = 0
                AE_print3 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", (" + namestr(w2.r2, globals()) + ")\n"
                AE_print4 = "Αποκωδικοποίηση της εντολής\n"
                AE_print5 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής\n"
                AE_print6 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print7 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print8 = "⬆️Αποθήκευση στο κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print9 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο " + namestr(w2.r1, globals()) + " της εντολής\n"
                AE_print10 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                kEP[0] = namestr(w2.r1, globals()) + "." + w2.r1[1]
                kEP[1] = namestr(w2.r2, globals()) + "." + w2.r2[1]
                kEP[2] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                temp_reg1.insert(i-1, w2.r1[1])
                temp_reg2.insert(i-1, w2.r2[1])
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
            elif w2.opcode == "0000010":
                var_counter2 = 1
                pb = 2
                AE_print11 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", (" + namestr(w2.r2, globals()) + ")\n"
                AE_print12 = "Αποκωδικοποίηση της εντολής\n"
                AE_print13 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής\n"
                AE_print14 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print15 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print16 = "⬆️Αποθήκευση στο κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print17 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο " + namestr(w2.r1, globals()) + " της εντολής\n"
                AE_print18 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                kEP[0] = namestr(w2.r1, globals()) + "." + w2.r1[1]
                kEP[1] = namestr(w2.r2, globals()) + "." + w2.r2[1]
                kEP[2] = namestr(w2.r1, globals()) + "." + w2.r1[0]
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
            elif w2.opcode == "0000011":
                var_counter2 = 1
                pb = 1
                AE_print19 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", " + namestr(w2.r2, globals()) + ", " + namestr(w2.r3, globals()) + "\n"
                AE_print20 = "Αποκωδικοποίηση της εντολής\n"
                AE_print21 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής\n"
                AE_print22 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print23 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print24 = "⬆️Αποθήκευση στο κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print25 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο " + namestr(w2.r1, globals()) + " της εντολής\n"
                AE_print26 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                kEP[0] = namestr(w2.r1, globals()) + "." + w2.r1[1]
                kEP[1] = namestr(w2.r2, globals()) + "." + w2.r2[1]
                kEP[2] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                temp_reg1.insert(i-1, w2.r1[1])
                temp_reg2.insert(i-1, w2.r2[1])
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
            elif w2.opcode == "0000100":
                var_counter2 = 1
                pb = 1
                AE_print19 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", " + namestr(w2.r2, globals()) + ", " + namestr(w2.r3, globals()) + "\n"
                AE_print20 = "Αποκωδικοποίηση της εντολής\n"
                AE_print21 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής\n"
                AE_print22 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print23 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print24 = "⬆️Αποθήκευση στο κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print25 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο " + namestr(w2.r1, globals()) + " της εντολής\n"
                AE_print26 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                kEP[0] = namestr(w2.r1, globals()) + "." + w2.r1[1]
                kEP[1] = namestr(w2.r2, globals()) + "." + w2.r2[1]
                kEP[2] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                temp_reg1.insert(i-1, w2.r1[1])
                temp_reg2.insert(i-1, w2.r2[1])
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
            elif w2.opcode == "0000101":
                var_counter2 = 1
                pb = 1
                AE_print19 = "-----------------------Βαθμίδα ΑΕ: " + str(w2.name) + " " + namestr(w2.r1, globals()) + ", " + namestr(w2.r2, globals()) + ", " + namestr(w2.r3, globals()) + "\n"
                AE_print20 = "Αποκωδικοποίηση της εντολής\n"
                AE_print21 = "Ανάγνωση των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολής\n"
                AE_print22 = "Υπολογισμός της τιμής ΜΠ+d\n"
                AE_print23 = "⬆️Αποθήκευση των σημάτων ελέγχου στον κΕΠ.\n"
                AE_print24 = "⬆️Αποθήκευση στο κΕΠ των περιεχομένων (" + namestr(w2.r1, globals()) + ") και ( " + namestr(w2.r2, globals()) + ") των καταχωρητών που δηλώνονται στα πεδία " + namestr(w2.r1, globals()) + " και " + namestr(w2.r2, globals()) + " της εντολήής\n"
                AE_print25 = "⬆️Αποθήκευση στον κΕΠ του αριθμού του καταχωρητή που δηλώνεται στο πεδίο " + namestr(w2.r1, globals()) + " της εντολής\n"
                AE_print26 = "⬆️Αποθήκευση της τιμής ΜΠ+d στον κΕΠ\n"
                kEP[0] = namestr(w2.r1, globals()) + "." + w2.r1[1]
                kEP[1] = namestr(w2.r2, globals()) + "." + w2.r2[1]
                kEP[2] = namestr(w2.r1, globals()) + "." + w2.r1[0]
                temp_reg1.insert(i-1, w2.r1[1])
                temp_reg2.insert(i-1, w2.r2[1])
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
    if x>2:
        if ep_skip == 1:
            var_counter3 = 0
            ap0 = pa = br = pg1 = al0 = al1 = dmd1 = gmd1 = gk1 = 2
            EP_print00 = "-----------------------Βαθμίδα ΕΠ\n"
            EP_print01 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(EP_print00)
            f.write(EP_print01)
            f.close()
            ep_skip = 0
        elif ep_flag >= 0:
            w3 = Instr_Cache[ep_flag]
            if ep_skip == 1:
                EP_print00 = "-----------------------Βαθμίδα ΕΠ\n"
                PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print00)
                f.write(PE_print4)
                f.close()
                ep_flag = 0
            if w3.opcode == "0000000":
                var_counter3 = 0
                ap0 = pa = br = pg1 = al0 = al1 = dmd1 = gmd1 = gk1 = 0
                nop_print11 = "-----------------------Βαθμίδα ΕΠ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w3.opcode == "0000001":
                var_counter3 = 1
                ap0 = pa = br = pg1 = gmd1 = 0
                al0 = al1 = 2
                dmd1 = gk1 = 1
                EP_print1 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", (" + namestr(w3.r2, globals()) + ")\n"
                EP_print2 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + ") και (" + namestr(w3.r2, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kPM[0] = kEP[0]
                kPM[2] = kEP[1]
                kPM[3] = kEP[2]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print1)
                f.write(EP_print2)
                f.close()
            elif w3.opcode == "0000010":
                var_counter3 = 1
                ap0 = pa = br = gmd1 = gk1 = 0
                pg1 = gmd1 = 1
                al0 = al1 = 2
                EP_print3 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", (" + namestr(w3.r2, globals()) + ")\n"
                EP_print4 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + ") και (" + namestr(w3.r2, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kPM[0] = kEP[0]
                kPM[2] = kEP[1]
                kPM[3] = kEP[2]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print3)
                f.write(EP_print4)
                f.close()
            elif w3.opcode == "0000011":
                var_counter3 = 1
                ap0 = pa = br = al0 = gmd1 = 0
                pg1 = al1 = gk1 = 1
                dmd1 = 2
                EP_print5 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", " + namestr(w3.r2, globals()) + ", " + namestr(w3.r3, globals()) + "\n"
                EP_print6 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + "), (" + namestr(w3.r2, globals()) + ") και (" + namestr(w3.r3, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kPM[0] = kEP[0]
                kPM[2] = kEP[1]
                kPM[3] = kEP[2]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print5)
                f.write(EP_print6)
                f.close()
            elif w3.opcode == "0000100":
                var_counter3 = 1
                ap0 = pa = br = al0 = gmd1 = 0
                pg1 = al1 = gk1 = 1
                dmd1 = 2
                EP_print5 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", " + namestr(w3.r2, globals()) + ", " + namestr(w3.r3, globals()) + "\n"
                EP_print6 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + "), (" + namestr(w3.r2, globals()) + ") και (" + namestr(w3.r3, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kPM[0] = kEP[0]
                kPM[2] = kEP[1]
                kPM[3] = kEP[2]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print5)
                f.write(EP_print6)
                f.close()
            elif w3.opcode == "0000101":
                var_counter3 = 1
                ap0 = pa = br = al0 = gmd1 = 0
                pg1 = al1 = gk1 = 1
                dmd1 = 2
                EP_print5 = "-----------------------Βαθμίδα ΕΠ: " + str(w3.name) + " " + namestr(w3.r1, globals()) + ", " + namestr(w3.r2, globals()) + ", " + namestr(w3.r3, globals()) + "\n"
                EP_print6 = "⬆️Αποθήκευση των (" +  namestr(w3.r1, globals()) + "), (" + namestr(w3.r2, globals()) + ") και (" + namestr(w3.r3, globals()) + ") από τον κΕΠ στον κΠΜ\n"
                kPM[0] = kEP[0]
                kPM[2] = kEP[1]
                kPM[3] = kEP[2]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(EP_print5)
                f.write(EP_print6)
                f.close()
    if x>3:
        if pm_skip == 1:
            var_counter4 = 0
            pg2 = dmd2= gmd2= gk2 = 2
            PM_print12 = "-----------------------Βαθμίδα ΠΜ\n"
            PM_print13 = "Δεν υπάρχουν άλλες εντολές.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(PM_print12)
            f.write(PM_print13)
            f.close()
            pm_skip = 0
        elif pm_flag >= 0:
            w4 = Instr_Cache[pm_flag]
            if pm_skip == 1:
                PM_print12 = "-----------------------Βαθμίδα ΠΜ\n"
                PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print12)
                f.write(PE_print4)
                f.close()
                pm_skip = 0
            if w4.opcode == "0000000":
                var_counter4 = 0
                pg2 = dmd2= gmd2= gk2 = 0
                nop_print11 = "-----------------------Βαθμίδα ΠΜ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w4.opcode == "0000001":
                var_counter4 = 1
                pg2 = gmd2= 0
                dmd2=gk2 = 1
                PM_print1 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", (" + namestr(w4.r2, globals()) + ")\n"
                PM_print2 = "Διαβάζεται το περιεχόμενο της θέσης μνήμης με διεύθυνση (" + namestr(w4.r2, globals()) + ")\n"
                Data_Cache[0] = kPM[0]
                Data_Cache[1] = kPM[2]
                PM_print3 = "⬆️Αποθήκευση του δεδομένου που διαβάστηκε στο πεδίο δε του κΑΑ\n"
                kAA[1] = kPM[3]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print1)
                f.write(PM_print2)
                f.write(PM_print3)
                f.close()
            elif w4.opcode == "0000010":
                var_counter4 = 1
                pg2 = gmd2= 1
                dmd2=gk2 = 0
                PM_print4 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", (" + namestr(w4.r2, globals()) + ")\n"
                PM_print5 = "Διαβάζεται το περιεχόμενο της θέσης μνήμης με διεύθυνση (" + namestr(w4.r2, globals()) + ")\n"
                Data_Cache[0] = kPM[0]
                Data_Cache[1] = kPM[2]
                PM_print6 = "⬆️Αποθήκευση του δεδομένου που διαβάστηκε στο πεδίο δε του κΑΑ\n"
                kAA[1] = kPM[3]
                ALM(w4.name, w4.r1, w4.r2, w4.r3, i)
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print4)
                f.write(PM_print5)
                f.write(PM_print6)
                f.close()
            elif w4.opcode == "0000011":
                var_counter4 = 1
                pg2 = gk2 = 1
                dmd2= 2
                gmd2= 0
                PM_print7 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", " + namestr(w4.r2, globals()) + ", " + namestr(w4.r3, globals()) + "\n"
                PM_print8 = "⬆️Μεταφορά αποτελέσματος απ από τον κΠΜ στον κΑΑ\n"
                kAA[1] = kPM[3]
                kAA[2] = kPM[1]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print7)
                f.write(PM_print8)
                f.close()
            elif w4.opcode == "0000100":
                var_counter4 = 1
                pg2 = gk2 = 1
                dmd2= 2
                gmd2= 0
                PM_print7 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", " + namestr(w4.r2, globals()) + ", " + namestr(w4.r3, globals()) + "\n"
                PM_print8 = "⬆️Μεταφορά αποτελέσματος απ από τον κΠΜ στον κΑΑ\n"
                kAA[1] = kPM[3]
                kAA[2] = kPM[1]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print7)
                f.write(PM_print8)
                f.close()
            elif w4.opcode == "0000101":
                var_counter4 = 1
                pg2 = gk2 = 1
                dmd2= 2
                gmd2= 0
                PM_print7 = "-----------------------Βαθμίδα ΠΜ: " + str(w4.name) + " " + namestr(w4.r1, globals()) + ", " + namestr(w4.r2, globals()) + ", " + namestr(w4.r3, globals()) + "\n"
                PM_print8 = "⬆️Μεταφορά αποτελέσματος απ από τον κΠΜ στον κΑΑ\n"
                kAA[1] = kPM[3]
                kAA[2] = kPM[1]
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(PM_print7)
                f.write(PM_print8)
                f.close()
    if x>4:
        if aa_skip == 1:
            var_counter5 = 0
            pg3 = gk3= 2
            AA_print11 = "-----------------------Βαθμίδα ΑΑ\n"
            AA_print12 = "Δεν υπάρχουν άλλες εντολές.\n"
            f = open("Log.txt", 'a', encoding="utf-8")
            f.write(AA_print11)
            f.write(AA_print12)
            f.close()
            aa_skip = 0
        elif aa_flag >= 0:
            if y+1 > len(Instr_Cache)-1:
                pass
            else:
                w6 = Instr_Cache[y+1]
                if w6 == "NOP":
                    pg3 = gk3= 0
            w5 = Instr_Cache[aa_flag]
            if aa_skip == 1:
                AA_print11 = "-----------------------Βαθμίδα ΑΑ\n"
                PE_print4 = "Καμία εντολή δε χρησιμοποιεί αυτή τη βαθμίδα\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print11)
                f.write(PE_print4)
                f.close()
                aa_skip = 0
            if w5.opcode == "0000000":
                var_counter5 = 0
                nop_print11 = "-----------------------Βαθμίδα ΑΑ: NOP\n"
                nop_print22 = "Δεν πραγματοποιείται καμία λειτουργία (NOP)\n"
                pg3 = gk3= 0
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(nop_print11)
                f.write(nop_print22)
                f.close()
            elif w5.opcode == "0000001":
                var_counter5 = 1
                pg3 = 0
                gk3= 1
                AA_print1 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", (" + namestr(w5.r2, globals()) + ")\n"
                AA_print2 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                Register_File[0] = kAA[0]
                Register_File[1] = kAA[1]
                ALM(w5.name, w5.r1, w5.r2, w5.r3, i)
                AA_print3 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print4 = "Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο " + namestr(w5.r2, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print1)
                f.write(AA_print2)
                f.write(AA_print3)
                f.write(AA_print4)
                f.close()
            elif w5.opcode == "0000010":
                var_counter5= 1
                pg3 = 2
                gk3= 0
                AA_print5 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", (" + namestr(w5.r2, globals()) + ")\n"
                AA_print6 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                # Register_File[0] = kAA[0]
                # Register_File[1] = kAA[1]
                AA_print7 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print8 = "Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο " + namestr(w5.r2, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print5)
                f.write(AA_print6)
                f.write(AA_print7)
                f.write(AA_print8)
                f.close()
            elif w5.opcode == "0000011":
                var_counter5 = 1
                pg3 = gk3= 1
                AA_print9 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", " + namestr(w5.r2, globals()) + ", " + namestr(w5.r3, globals()) + "\n"
                AA_print10 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                Register_File[0] = kAA[0]
                Register_File[1] = kAA[1]
                ALM(w5.name, w5.r1, w5.r2, w5.r3, i)
                AA_print11 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print12 = "Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο " + namestr(w5.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print9)
                f.write(AA_print10)
                f.write(AA_print11)
                f.write(AA_print12)
                f.close()
            elif w5.opcode == "0000100":
                var_counter5 = 1
                pg3 = gk3= 1
                AA_print9 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", " + namestr(w5.r2, globals()) + ", " + namestr(w5.r3, globals()) + "\n"
                AA_print10 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                Register_File[0] = kAA[0]
                Register_File[1] = kAA[1]
                ALM(w5.name, w5.r1, w5.r2, w5.r3, i)
                AA_print11 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print12 = "Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο " + namestr(w5.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print9)
                f.write(AA_print10)
                f.write(AA_print11)
                f.write(AA_print12)
                f.close()
            elif w5.opcode == "0000101":
                var_counter5 = 1
                pg3 = gk3= 1
                AA_print9 = "-----------------------Βαθμίδα ΑΑ: " + str(w5.name) + " " + namestr(w5.r1, globals()) + ", " + namestr(w5.r2, globals()) + ", " + namestr(w5.r3, globals()) + "\n"
                AA_print10 = "Το πεδίο δε του κΑΑ οδηγείται στην είσοδο δεδομένων της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                Register_File[0] = kAA[0]
                Register_File[1] = kAA[1]
                ALM(w5.name, w5.r1, w5.r2, w5.r3, i)
                AA_print11 = "Το πεδίο κε του κΑΑ οδηγεί στην είσοδο διεύθυνσης της πόρτας εγγραφής των καταχωρητών γενικού σκοπού\n"
                AA_print12 = "Το περιεχόμενο του πεδίου δε γράφεται στον καταχωρητή που δηλώνεται στο πεδίο " + namestr(w5.r3, globals()) + "\n"
                f = open("Log.txt", 'a', encoding="utf-8")
                f.write(AA_print9)
                f.write(AA_print10)
                f.write(AA_print11)
                f.write(AA_print12)
                f.close()