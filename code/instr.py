# Returns the name of an array as string
def namestr(obj, namespace):
    x = ''.join(map(str, [name for name in namespace if namespace[name] is obj]))
    return x

# Class for instruction creation
class Instruction:
    def __init__(self, name, opcode, r1, r2, r3, d):
        self.name = name
        self.opcode = opcode
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.d  = d