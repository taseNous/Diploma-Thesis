#Επιστρέφει το όνομα ενός πίνακα σαν string
def namestr(obj, namespace):
    x = ''.join(map(str, [name for name in namespace if namespace[name] is obj]))
    return x

def Enquiry(lis1): 
    if len(lis1) == 0: 
        return 0
    else: 
        return 1

#Κλάση για δημιουργία εντολών
class Instruction:
    def __init__(self, name, opcode, r1, r2, r3, d):
        self.name = name
        self.opcode = opcode
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.d  = d