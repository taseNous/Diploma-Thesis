import instr
from vars import dep_index_1, dep_index_2, sis1, sis2, sis3, index_nop, index1, index2, index3, index4, index5
import gui_vars

depend_nop_array = []

def depend_nop():
    
    global  dep_index_1, dep_index_2, sis1, sis2, sis3, depend_nop_array
    Instr_Cache = gui_vars.Instr_Cache

    dep_index_1 = 0
    dep_index_2 = 1

    #Αποθύκευση των αρχικών τιμών του po1 και po2
    depend_nop_array = []
    original_po1 = dep_index_1
    original_po2 = dep_index_2

    for i in range(len(Instr_Cache) - 1):
        p1 = Instr_Cache[dep_index_1]

        for y in range(len(Instr_Cache) - 1):
            if dep_index_2 >= len(Instr_Cache):
                pass
            elif sis3 == 2:
                pass
            else:
                p2 = Instr_Cache[dep_index_2]
                if p1 == "NOP" or p2 == "NOP":
                    pass
                elif p1.opcode == "0000001" and p2.opcode == "0000011":
                    if p1.r1 == p2.r1 or p1.r1 == p2.r2:
                        sis1 = i + 1

                        if y == 0:
                            sis2 = sis2 + 2
                            sis3 = 2
                        elif y == 1:
                            sis2 = sis2 + y
                            sis3 = y

                elif  p1.opcode == "0000011" and p2.opcode == "0000011":
                    if p1.r3 == p2.r1 or p1.r3 == p2.r2:
                        sis1 = i + 1

                        if y == 0:
                            sis2 = sis2 + 2
                            sis3 = 2
                        elif y == 1:
                            sis2 = sis2 + y
                            sis3 = y

                elif p1.opcode == "0000011" and p2.opcode == "0000001":
                    if p1.r3 == p2.r2:
                        sis1 = i + 1

                        if y == 0:
                            sis2 = sis2 + 2
                            sis3 = 2
                        elif y == 1:
                            sis2 = sis2 + y
                            sis3 = y

            dep_index_2 = dep_index_2 + 1

        sis3 = 0
        dep_index_2 = i + 2
        dep_index_1 = dep_index_1 + 1

    dep_index_1 = original_po1
    dep_index_2 = original_po2

    for i in range(len(Instr_Cache) - 1 + sis2):
        if dep_index_1 >= len(Instr_Cache) - 1:
            pass
        else:
            p1 = Instr_Cache[dep_index_1]

            for y in range(len(Instr_Cache) - 1 + sis2):
                if dep_index_2 >= len(Instr_Cache):
                    pass
                else:
                    p2 = Instr_Cache[dep_index_2]

                    if p1.opcode == "0000001" and p2.opcode == "0000011":
                        if p1.r1 == p2.r1 or p1.r1 == p2.r2:
                            if y == 0 :
                                sis3 = 2
                                depend_nop_array.append(i+5)
                            elif y == 1:
                                sis3 = y
                                depend_nop_array.append(i+6)

                    elif p1.opcode == "0000001" and p2.opcode == "0000001":
                        if p1.r1 == p2.r2:
                            if y == 0 :
                                sis3 = 2
                                depend_nop_array.append(i+5)
                            elif y == 1:
                                sis3 = y
                                depend_nop_array.append(i+6)

                    elif p1.opcode == "0000011" and p2.opcode == "0000011":
                        if p1.r3 == p2.r1 or p1.r3 == p2.r2:
                            if y == 0:
                                sis3 = 2
                                depend_nop_array.append(i+5)
                            elif y == 1:
                                depend_nop_array.append(i+6)
                                sis3 = y

                    elif p1.opcode == "0000011" and p2.opcode == "0000001":
                        if p1.r3 == p2.r2:
                            if y == 0:
                                sis3 = 2
                                depend_nop_array.append(i+5)
                            elif y == 1:
                                depend_nop_array.append(i+6)
                                sis3 = y

                    sis3 = 0
                    dep_index_2 = dep_index_2 + 1

            sis3 = 0
            dep_index_2 = i + 2
            dep_index_1 = dep_index_1 + 1

    for idx, tet in enumerate(Instr_Cache):
        if tet == "NOP":
            index_nop.append(idx)
    
    print(Instr_Cache)

#Freeze
def depend_freeze():

    global sis1, sis2, sis3, index1, index2, index3, index4, index5, dep_index_1, dep_index_2

    Instr_Cache = gui_vars.Instr_Cache

    dep_index_1 = 0
    dep_index_2 = 1

    for i in range(len(Instr_Cache) - 1):
        p1 = Instr_Cache[dep_index_1]
        for y in range(len(Instr_Cache) - 1):
            if dep_index_2 >= len(Instr_Cache):
                pass
            elif sis3 == 2:
                pass
            else:
                p2 = Instr_Cache[dep_index_2]
                if p1.r1 == p2.r1 or p1.r1 == p2.r2:
                    sis1 = i + 1
                    if y == 0:
                        sis2 = sis2 + 2
                        sis3 = 2
                    elif y == 1:
                        sis2 = sis2 + y
                        sis3 = y
            dep_index_2 = dep_index_2 + 1
        sis3 = 0
        dep_index_2 = i + 2
        dep_index_1 = dep_index_1 + 1

    dep_index_1 = 0
    dep_index_2 = 1
    for ip in range(len(Instr_Cache) - 1 + sis2):
        if dep_index_1 >= len(Instr_Cache) - 1:
            pass
        else:
            p1 = Instr_Cache[dep_index_1]
            for y in range(len(Instr_Cache) - 1 + sis2):
                if dep_index_2 >= len(Instr_Cache):
                    pass
                else:
                    p2 = Instr_Cache[dep_index_2]
                    if p1.opcode == "0000001" and p2.opcode == "0000011":
                        x = ip + y + 2 + len(index1)
                        if dep_index_2-dep_index_1 == 1:
                            sis1 = dep_index_2
                            sis4 = sis1 + 3
                            index2.append(sis1) #se poia entolh+1 einai to AE' kai X
                            index1.append("1")
                            index3.append(sis4) #se poio kyklo einai to X
                            print(index2)
                        if dep_index_2-dep_index_1 == 2:
                            sis1 = dep_index_2
                            sis4 = dep_index_2 + 2
                            index4.append(sis1)
                            index1.append("2")
                            index5.append(sis4) #se poio kyklo einai to AE'
                            print(index4)
                            print(index5)

                        if y == 0:
                            sis3 = 1

                        for w in range(1):
                            index1.append(x)
            
                    sis3 = 0
                    dep_index_2 = dep_index_2 + 1

        sis3 = 0
        dep_index_2 = ip + 2
        dep_index_1 = dep_index_1 + 1

    print(Instr_Cache)