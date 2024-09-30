from vars import kPM, m
import cycles
import dependencies

def ALM(name, r1, r2, r3, i):

    temp_reg1 = cycles.temp_reg1
    temp_reg2 = cycles.temp_reg2
    depend_nop_array = dependencies.depend_nop_array

    if name == "ADD": #ADD
        if i in depend_nop_array:
            result = int(temp_reg1[i-4]) + int(temp_reg2[i-4])
        else:
            result = int(r1[1]) + int(r2[1])
        r3[1] = str(result)
        kPM[1] = r3[1]
    elif name == "SUB": #SUB
        if i in depend_nop_array:
            result = int(temp_reg1[i-4]) - int(temp_reg2[i-4])
        else:
            result = int(r1[1]) - int(r2[1])
        r3[1] = str(result)
        kPM[1] = r3[1]
    elif name == "AND": #AND
        if i in depend_nop_array:
            result = int(temp_reg1[i-4][1]) & int(temp_reg2[i-4][1])
        else:
            result = int(r1[1]) & int(r2[1])
        if result < 0:
            result = 0
        r3[1] = str(result)
        kPM[1] = r3[1]
    elif name == "LOAD": #LOAD
        for y in range(16):
            x = m[y]
            if i in depend_nop_array:
                if temp_reg2[i-4] == x[0]:
                    temp_reg1[i-4] = x[1]
                    r1[1] = temp_reg1[i-4]
            else:
                if r2[1] == x[0]:
                    r1[1] = x[1]
    elif name == "STORE": #STORE
        for y in range(16):
            x = m[y]
            if r2[1] == x[0]:
                x[1] = r1[1]
    else:
        pass