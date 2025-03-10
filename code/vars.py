none = None

ke = 0  #Καταχωρητής Εγγραφή
de = 0  #Δεδομένα, διαβάζονται από τη Κρυφή Μνήμη Δεδομένων
ap = 0  #Αποτέλεσμα πράξης (ADD, SUB, AND)
DE = 0  #Είσοδος Δεδομένων της πόρτας εγγραφής 
dE = 0 
opcode = R1 = R2 = R3 = 0   #Κωδικός Λειτουργίας, r1, r2, r3 (κΑΕ)
data = 0    #Είσοδος Δεδομένων (Κρυφή Μνήμη Δεδομένων)
address = 0 #Είσοδος Διεύθυνσης (Κρυφή Μνήμη Δεδομένων)
kAE = [opcode, R1, R2, R3]  #Καταχωρητής ΑΕ
kEP = [R1, R2, ke]  #Καταχωρητής ΕΠ
kPM = [R1, ap, R2, ke]  #Καταχωρητής ΠΜ
kAA = [de, ke, ap]  #Καταχωρητής ΑΑ
Data_Cache = [data, address]    #Κρυφή Μνήμη Δεδομένων

var_counter1 = var_counter2 = var_counter3 = var_counter4 = var_counter5 = 0

d = 2

#Αρχικοποίησησ Καταχωρητών
r0 = ["0000", "00", "r0"] 
r1 = ["0001", "00", "r1"]
r2 = ["0010", "00", "r2"]
r3 = ["0011", "00", "r3"]
r4 = ["0100", "00", "r4"] 
r5 = ["0101", "00", "r5"]
r6 = ["0110", "00", "r6"]
r7 = ["0111", "00", "r7"]
r8 = ["1000", "00", "r8"] 
r9 = ["1001", "00", "r9"]
r10 = ["1010", "00", "r10"]
r11 = ["1011", "00", "r11"]
r12 = ["1100", "00", "r12"] 
r13 = ["1101", "00", "r13"]
r14 = ["1110", "00", "r14"]
r15 = ["1111", "00", "r15"]
r =  [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]

#Κράτα τις αρχικές τιμές
r0_start = ["0000", "00"]
r1_start = ["0001", "00"]
r2_start = ["0010", "00"]
r3_start = ["0011", "00"]
r4_start = ["0100", "00"]
r5_start = ["0101", "00"]
r6_start = ["0110", "00"]
r7_start = ["0111", "00"]
r8_start = ["1000", "00"]
r9_start = ["1001", "00"]
r10_start = ["1010", "00"]
r11_start = ["1011", "00"]
r12_start = ["1100", "00"]
r13_start = ["1101", "00"]
r14_start = ["1110", "00"]
r15_start = ["1111", "00"]
r_start = [r0_start, r1_start ,r2_start, r3_start, r4_start, r5_start ,r6_start, r7_start, r8_start, r9_start ,r10_start, r11_start, r12_start, r13_start ,r14_start, r15_start]

#Αρχικοποίηση Μνήμης
m0 = ["00", "00", "m0"]
m1 = ["01", "00", "m1"]
m2 = ["02", "00", "m2"]
m3 = ["03", "00", "m3"]
m4 = ["04", "00", "m4"]
m5 = ["05", "00", "m5"]
m6 = ["06", "00", "m6"]
m7 = ["07", "00", "m7"]
m8 = ["08", "00", "m8"]
m9 = ["09", "00", "m9"]
m10 = ["0A", "00", "m10"]
m11 = ["0B", "00", "m11"]
m12 = ["0C", "00", "m12"]
m13 = ["0D", "00", "m13"]
m14 = ["0E", "00", "m14"]
m15 = ["0F", "00", "m15"]
m16 = ["10", "00", "m16"]
m17 = ["11", "00", "m17"]
m18 = ["12", "00", "m18"]
m19 = ["13", "00", "m19"]
m20 = ["14", "00", "m20"]
m21 = ["15", "00", "m21"]
m22 = ["16", "00", "m22"]
m23 = ["17", "00", "m23"]
m = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23]

m0_starter = ["00", "00"]
m1_starter = ["01", "00"]
m2_starter = ["02", "00"]
m3_starter = ["03", "00"]
m4_starter = ["04", "00"]
m5_starter = ["05", "00"]
m6_starter = ["06", "00"]
m7_starter = ["07", "00"]
m8_starter = ["08", "00"]
m9_starter = ["09", "00"]
m10_starter = ["0A", "00"]
m11_starter = ["0B", "00"]
m12_starter = ["0C", "00"]
m13_starter = ["0D", "00"]
m14_starter = ["0E", "00"]
m15_starter = ["0F", "00"]
m16_starter = ["10", "00"]
m17_starter = ["11", "00"]
m18_starter = ["12", "00"]
m19_starter = ["13", "00"]
m20_starter = ["14", "00"]
m21_starter = ["15", "00"]
m22_starter = ["16", "00"]
m23_starter = ["17", "00"]

#Τιμές Σημάτων Ελέγχου
pb = ap0 = pa = br = pg1 = pg2 = pg3 = al0 = al1 = dmd1 = gmd1 =dmd2 = gmd2 = gk1 = gk2 = gk3 = 2

counter_l = -1
for_counter_l = 0

dep_index_1 = 0
dep_index_2 = 1

sis1 = -1
sis2 = sis3 = 0
choose_nop = 0

index_nop = []
index1 = []
index2 = []
index3 = []
index4 = []
index5 = []
index6 = []
index7 = []
index8 = []
index_bypass_instr = []
index_bypass_cycle = []
index_bypass_cycle1 = []
index_bypass_cycle2 = []

bp_index = 0

counter = 0

pepe_falg = 0
aa_aa_flag = 0

freeze_array = []

start_test = 0

temp_reg_cycle_add = []
temp_reg1_add = []
temp_reg2_add = []
temp_reg_cycle_load = []
temp_reg1_load = []
temp_reg2_load = []
temp_reg_cycle_store = []
temp_reg1_store  = []
temp_reg2_store  = []
temp_reg_bre = []
temp_reg1_bre = []
temp_reg2_bre = []

ae_flag = -1
x_flag = 0
ep_flag = 0
pm_flag = 0
aa_flag = 0
pe_flag = -1
pe_skip = 0
aee_flag = 0
ae_skip = 0
ep_skip = 0
pm_skip = 0
aa_skip = 0

instr_move = -1