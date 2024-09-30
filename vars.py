none = None

ke = 0  #Καταχωρητής Εγγραφή
de = 0  #Δεδομένα, διαβάζονται από τη Κρυφή Μνήμη Δεδομένων
ap = 0  #Αποτέλεσμα πράξης (ADD, SUB, AND)
DE = 0  #Είσοδος Δεδομένων της πόρτας εγγραφής 
dE = 0 
Register_File = [DE, dE]    #Καταχωρητής Γενικού Σκοπού
opcode = R1 = R2 = R3 = 0   #Κωδικός Λειτουργίας, r1, r2, r3 (κΑΕ)
data = 0    #Είσοδος Δεδομένων (Κρυφή Μνήμη Δεδομένων)
address = 0 #Είσοδος Διεύθυνσης (Κρυφή Μνήμη Δεδομένων)
kAE = [opcode, R1, R2, R3]  #Καταχωρητής ΑΕ
kEP = [R1, R2, ke]  #Καταχωρητής ΕΠ
kPM = [R1, ap, R2, ke]  #Καταχωρητής ΠΜ
kAA = [de, ke, ap]  #Καταχωρητής ΑΑ
Data_Cache = [data, address]    #Κρυφή Μνήμη Δεδομένων

var_counter1 = var_counter2 = var_counter3 = var_counter4 = var_counter5 = 0

#Αρχικοποίησησ Καταχωρητών
r0 = ["000", "1"] 
r1 = ["001", "3"]
r2 = ["010", "5"]
r3 = ["011", "7"]
r4 = ["100", "1"] 
r5 = ["101", "3"]
r6 = ["110", "5"]
r7 = ["111", "7"]
r =  [r0, r1, r2, r3, r4, r5, r6, r7]

#Κράτα τις αρχικές τιμές
r0_start = ["000", "1"]
r1_start = ["001", "3"]
r2_start = ["010", "5"]
r3_start = ["011", "7"]
r4_start = ["100", "1"]
r5_start = ["101", "3"]
r6_start = ["110", "5"]
r7_start = ["111", "7"]

#Αρχικοποίηση Μνήμης
m0 = ["0", "1"]
m1 = ["1", "1"]
m2 = ["2", "2"]
m3 = ["3", "3"]
m4 = ["4", "4"]
m5 = ["5", "5"]
m6 = ["6", "6"]
m7 = ["7", "7"]
m8 = ["8", "8"]
m9 = ["9", "0"]
m10 = ["10", "0"]
m11 = ["11", "0"]
m12 = ["12", "0"]
m13 = ["13", "0"]
m14 = ["14", "0"]
m15 = ["15", "0"]
m16 = ["16", "0"]
m17 = ["17", "1"]
m18 = ["18", "1"]
m19 = ["19", "2"]
m20 = ["20", "3"]
m21 = ["21", "4"]
m22 = ["22", "5"]
m23 = ["23", "6"]
m24 = ["24", "7"]
m25 = ["25", "8"]
m26 = ["26", "0"]
m27 = ["27", "0"]
m28 = ["28", "0"]
m29 = ["29", "0"]
m30 = ["30", "0"]
m31 = ["31", "0"]
m = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25, m26, m27, m28, m29, m30, m31]

m1_starter = ["0", "9"]
m2_starter = ["1", "8"]
m3_starter = ["2", "7"]
m4_starter = ["3", "6"]
m5_starter = ["4", "5"]
m6_starter = ["5", "4"]
m7_starter = ["6", "3"]
m8_starter = ["7", "2"]
m9_starter = ["8", "1"]
m10_starter = ["9", "0"]
m11_starter = ["10", "0"]
m12_starter = ["11", "0"]
m13_starter = ["12", "0"]
m14_starter = ["13", "0"]
m15_starter = ["14", "0"]
m16_starter = ["15", "0"]

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

indexx = 1
bp_index = 0

counter = 0

pepe_falg = 0
aa_aa_flag = 0

freeze_array = []

choose = 1

start_test = 0

temp_reg1 = []
temp_reg2 = []

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