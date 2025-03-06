import gui_vars, table_instructions, cycles, method

from vars import index1, index2, index3, index4, index5, index6, index7, index8, index_bypass_instr, index_bypass_cycle, index_bypass_cycle1, index_bypass_cycle2

from gui_vars import current_y

depend_nop_array = []
bre_array = []
bre_index_pred = []
Instr_Cache1 = []

p11 = 0
p22 = 1
p33 = 3
time = -10
index = 0
skip = 0

def find_positions_by_name(array, target_name):
    """
    Finds all positions of objects with a specific name in the array.

    Args:
        array (list): The list of Instruction objects.
        target_name (str): The name to find.

    Returns:
        list: A list of indices where objects with the target name are found.
    """
    positions = []
    for index, instruction in enumerate(array):
        if instruction.name == target_name:
            positions.append(index)
    return positions


def delete_elements(array1, i, d):
    """
    Deletes elements from the array based on the index i and the value d.

    Args:
        array1 (list): The array of elements.
        i (int): The index in the array to start from.
        d (int): Determines how many elements to delete starting from index i + 1.

    Returns:
        list: The updated array after deletion.
    """
    if d > 1:  # No deletion occurs when d == 1
        # Calculate the range of elements to delete
        start_index = i + 1
        end_index = start_index + (d - 1)
        # Remove the elements in the range [start_index, end_index)
        del array1[start_index:end_index]
    return array1

def delete_elements1(array1, i, d):
    """
    Deletes elements from the array starting from index i + 3, based on the value d.

    Args:
        array1 (list): The array of elements.
        i (int): The index in the array to calculate the deletion start point.
        d (int): Determines how many elements to delete starting from index i + 3.

    Returns:
        list: The updated array after deletion.
    """
    if d > 0:  # Only delete if d > 0
        # Calculate the range of elements to delete
        start_index = i + 3  # Start deleting from i + 3
        end_index = start_index + (d-1)  # Delete d elements starting from start_index
        # Remove the elements in the range [start_index, end_index)
        del array1[start_index:end_index]
    return array1

#Check if "AA" is in the first row
def is_aa_in_first_row(canvas, screen_height):
    items = canvas.find_all()
    for item in items:
        if canvas.type(item) == "text":
            text = canvas.itemcget(item, "text")
            coords = canvas.coords(item)
            if text == "ΑΑ" and coords[1] == screen_height / 7.4482:
                return True
    return False

def depend_nop(i, q):
    
    global p11, p22, p33, time, Instr_Cache1
    Instr_Cache = gui_vars.Instr_Cache

    do_p3 = 0

    choose_bre = method.choose_bre
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    bre_index_pred = cycles.bre_index_pred

    if i == 0:
        index1.clear()
        index3.clear()
        index4.clear()
        index5.clear()
        index6.clear()
        index7.clear()
        index8.clear()
        depend_nop_array.clear()
        bre_array_not.clear()
        bre_index.clear()
        bre_index_pred.clear()
        Instr_Cache1 = Instr_Cache[:]
        positions = []
        positions = find_positions_by_name(Instr_Cache1, "BRE")
        if positions:
            if choose_bre == 1:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
            elif choose_bre == 2:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements1(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
        for w in Instr_Cache1:
            print(w.name)

        
    p11 = i
    p33 = i+3
    time = -10

    if p11 > len(Instr_Cache1)-1:
        pass
    else:
        p1 = Instr_Cache1[p11]

    if p33 > len(Instr_Cache1)-1:
        pass
    else:
        p3 = Instr_Cache1[p33]
        do_p3 = 1

    sis2 = 0

    if do_p3 == 1:
        if p1.opcode == "0010000" and p3.opcode in ["0000001", "0000010", "0000011"]:
            if p1.r1 == p3.r1 or p1.r1 == p3.r2:
                sis2 = p11+4
                depend_nop_array.append(sis2)
        if p1.opcode in ["0000001", "0000010", "0000011"] and p3.opcode in ["0000001", "0000010", "0000011"]:
            if p1.r3 == p3.r1 or p1.r3 == p3.r2:
                sis2 = p11+4
                depend_nop_array.append(sis2)  
        if p1.opcode == "0010000" and p3.opcode == "0010000":
            if p1.r1 == p3.r2:
                sis2 = p11+4
                depend_nop_array.append(sis2)  
        if p1.opcode in ["0000001", "0000010", "0000011"] and p3.opcode == "0010000":
            if p1.r3 == p3.r1:
                sis2 = p11+4
                depend_nop_array.append(sis2) 
        if p1.opcode in ["0000001", "0000010", "0000011"] and p3.opcode == "0100000":
            if p1.r3 == p3.r2 or p1.r3 == p3.r1:
                sis2 = p11+4
                depend_nop_array.append(sis2) 
        if p1.opcode == "0010000" and p3.opcode == "0100000":
            if p1.r1 == p3.r2 or p1.r1 == p3.r1:
                sis2 = p11+4
                depend_nop_array.append(sis2)
        if p1.opcode == "0010000" and p3.opcode == "1110000":
            if p1.r1 == p3.r2 or p1.r1 == p3.r1:
                sis2 = p11+4
                depend_nop_array.append(sis2)
                print("depend_nop_array")
        if p1.opcode in ["0000001", "0000010", "0000011"] and p3.opcode == "1110000":
            if p1.r3 == p3.r2 or p1.r3 == p3.r1:
                sis2 = p11+4
                depend_nop_array.append(sis2)
                print("depend_nop_array")
                print(depend_nop_array)

def depend_freeze(i, q):

    global p11, p22, p33, p44, time, current_y, index, skip, Instr_Cache1
    Instr_Cache = gui_vars.Instr_Cache
    d_value = cycles.d_value
    entolh_index = table_instructions.entolh_index

    def check_and_remove_difference_of_0(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if value1 - value2 == 0 or abs(value1 - value2) == 1:
                    array1.remove(value1)
                    return  # Exit after processing the first match

    def check_and_process_arrays(array1, array2):
        """
        Check if the arrays have values with a distance of 1.
        Remove the smaller value and reduce the bigger value by 1.
        """
        for value1 in array1:
            for value2 in array2:
                if abs(value1 - value2) == 1 or value1 == value2:
                    # Remove the smaller value
                    # if value1 <= value2:
                    indexxx = array1.index(value1)
                    array1.remove(value1)
                    # array1[indexxx:] = [x - 1 for x in array1[indexxx:]]
                    indexxxx = array2.index(value2)
                    # array2[indexxxx] -= 1
                    # else:
                    #     array2.remove(value2)
                    #     array1[array1.index(value1)] -= 1
                    return  # Exit after processing the first pair with distance 1

    
    def adjust_arrays1(array1, array2):
        """
        Adjust two arrays such that:
        1. If a value in array1 is 1 less or 1 greater than a value in array2, the value in array1 is removed.
        2. Each value in array2 is reduced by 1.
        """
        # Reduce all values in array2 by 1
        # array2 = [x - 1 for x in array2]
        
        i = 0
        while i < len(array1):
            match_found = False
            for j in range(len(array2)):
                if array1[i] - array2[j] == 1 or array1[i] - array2[j] == 0:  # Check for a difference of 1
                    array1.pop(i)  # Remove the value from array1
                    match_found = True
                    # break  # Exit the inner loop to recheck array1 from the same index
                # elif array1[i] - array2[j] == 2:
                #     array1[i] += 1
                    break
            if not match_found:
                i += 1  # Only increment if no value was removed in this pass

        return array1, array2
    
    def adjust_arrays2(array1, array2):
        """
        Adjust two arrays such that:
        1. If a value in array1 is 1 less or 1 greater than a value in array2, the value in array1 is removed.
        2. Each value in array2 is reduced by 1.
        """
        # Reduce all values in array2 by 1
        
        i = 0
        while i < len(array1):
            match_found = False
            for j in range(len(array2)):
                if array1[i] - array2[j] == 1 or array1[i] - array2[j] == 0 or array1[i] - array2[j] == 2:  # Check for a difference of 1
                    array1.pop(i)  # Remove the value from array1
                    # array1[i] -= 1
                    match_found = True
                    break  # Exit the inner loop to recheck array1 from the same index
            if not match_found:
                i += 1  # Only increment if no value was removed in this pass

        return array1, array2
    
    def adjust_arrays22(array1, array2):
        """
        Adjust two arrays such that:
        1. If a value in array1 is 1 less or 1 greater than a value in array2, the value in array1 is removed.
        2. Each value in array2 is reduced by 1.
        """
        # Reduce all values in array2 by 1
        
        i = 0
        while i < len(array1):
            match_found = False
            for j in range(len(array2)):
                if array1[i] - array2[j] == 2:  # Check for a difference of 1
                    array1.pop(i)  # Remove the value from array1
                    match_found = True
                    break  # Exit the inner loop to recheck array1 from the same index
            if not match_found:
                i += 1  # Only increment if no value was removed in this pass

        return array1, array2

    def adjust_array(arr):
        for i in range(len(arr) - 1):
            # Check if the difference between consecutive elements is 2
            if arr[i + 1] - arr[i] == 2:
                # Increase the second element by 1
                arr[i + 1] += 1
            elif arr[i + 1] - arr[i] == 1:
                # Increase the second element by 1
                arr[i + 1] += 2
        return arr

    global Instr_Cache1

    choose_bre = method.choose_bre
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    bre_index_pred = cycles.bre_index_pred
    Instr_Cache2 = cycles.Instr_Cache1

    if q == 0:
        index_bypass_instr.clear()
        index_bypass_cycle.clear()
        index1.clear()
        index3.clear()
        index4.clear()
        index5.clear()
        index6.clear()
        index7.clear()
        index8.clear()
        # bre_index.clear()
        # bre_array_not.clear()
        # bre_index_pred.clear()
        index = 0
        Instr_Cache1 = Instr_Cache[:]
        positions = []
        positions = find_positions_by_name(Instr_Cache1, "BRE")
        if positions:
            if choose_bre == 1:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
            elif choose_bre == 2:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements1(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
        # for w in Instr_Cache1:
        #     print(w.name)

    do_p1 = 0
    do_p2 = 0
    do_p3 = 0
    do_p4 = 0

    p11 = i
    p22 = i+1
    p33 = i+2
    p44 = i+3
    time = -10

    print("p11")
    print(p11)
    

    if q > 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        p4 = Instr_Cache2[q-3]
        do_p4 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    elif q == 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])
            

    elif q == 1:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    print("q")
    print(q)
    if q > 0:
        print(p1["name"])
        print(p1["r1"])

    sis1 = 0
    sis2 = 0
        
    if do_p1 == 1 and do_p2 == 1:
        if p1["opcode"] == "0010000" and p2["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r2"][2] == p2["r3"][2]:
                print("tasos")
                sis1 = p11
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2+ 2*len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # print("index3")
                # print(index3)
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p2["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"][2] == p2["r3"][2] or p1["r2"][2] == p2["r3"][2]:
                print("poutsa")
                # print(i)
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # adjust_arrays(index5, index3)
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p2["opcode"] == "0010000":
            if p1["r1"][2] == p2["r1"][2] or p1["r2"][2] == p2["r1"][2]:
                sis1 = p11
                sis2 = i

                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1 
                # # if index3:
                # #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # adjust_arrays(index5, index3)
        if p1["opcode"] == "0010000" and p2["opcode"] == "0010000":
            if p1["r2"][2] == p2["r1"][2]:
                sis1 = p11+1
                sis2 = i
                print("q")
                print(q)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # adjust_arrays(index5, index3)
        if p1["opcode"] == "0100000" and p2["opcode"] == "0010000":
            if p1["r1"][2] == p2["r1"][2] or p1["r2"][2] == p2["r1"][2]:
                sis1 = p11+1
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # adjust_arrays(index5, index3)
        if p2["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "0100000":
            if p1["r1"][2] == p2["r3"][2] or p1["r2"][2] == p2["r3"][2]:
                sis1 = p11+1
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
        if p2["opcode"] == "0010000" and p1["opcode"] == "1110000":
            if p1["r1"] == p2["r1"] or p1["r2"] == p2["r1"]:
                print("tasos")
                sis1 = p11
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2+ len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                # print("index3")
                # print(index3)
        if p2["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"][2] == p2["r3"][2] or p1["r2"][2] == p2["r3"][2]:
                sis1 = p11+1
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                #     skip = 1
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                index1.append("1")
                index3.append(sis2) #se poio kyklo einai to X
                
    # sis1 = 0
    # sis2 = 0

    if do_p3 == 1:
        if p1["opcode"] == "0010000" and p3["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r2"][2] == p3["r3"][2] or p1["r2"][2] == p3["r3"][2]:
                sis1 = p11
                sis2 = i
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if skip == 0:
                #     if bre_index:
                #         sis2 = sis2 + 2*len(bre_index) - 1
                #         skip = 1
                
                # if bre_index_pred:
                #     sis2 = sis2 - len(bre_index_pred)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p3["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"][2] == p3["r3"][2] or p1["r2"][2] == p3["r3"][2]:
                sis1 = p11
                sis2 = i
                # if index5:
                #     sis2 = sis2 + len(index5)
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
                # adjust_arrays(index5, index3)
        if p1["opcode"] == "0010000" and p3["opcode"] == "0010000":
            if p1["r2"][2] == p3["r1"][2]:
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
                # adjust_arrays(index5, index3)
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p3["opcode"] == "0010000":
            if p1["r1"][2] == p3["r1"][2] or p1["r2"][2] == p3["r1"][2]:
                sis1 = p11
                sis2 = i
                
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if skip == 0:
                # if bre_index:
                #     # print("tasos")
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
                # adjust_arrays(index5, index3)
                # print("index5")
                # print(index5)
        if p3["opcode"] == "0010000" and p1["opcode"] == "0100000":
            if p1["r1"] == p3["r1"] or p1["r2"] == p3["r1"]: 
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
                # adjust_arrays(index5, index3)
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "0100000":
            if p1["r1"] == p3["r3"] or p1["r2"] == p3["r3"]: 
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"] == p3["r3"] or p1["r2"] == p3["r3"]: 
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
        if p3["opcode"] == "0010000" and p1["opcode"] == "1110000":
            if p1["r1"] == p3["r1"] or p1["r2"] == p3["r1"]: 
                sis1 = p11
                sis2 = i
                # if index3:
                #     sis2 = sis2 + 2*len(index3)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                #     skip = 1
                # if index5:
                #     sis2 = sis2 + len(index5)
                # index4.append(sis1)
                index1.append("2")
                index5.append(sis2) #se poio kyklo einai to AE'
                # adjust_arrays(index5, index3)

    # if do_p4 == 1:
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0010000"]:
    #         if p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0010000"]:
    #         if p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0100000"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0100000"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode == "0010000" and p4.opcode == "1110000":
    #         if p1.r1 == p4.r2 or p1.r1 == p4.r1:
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode == "1110000":
    #         if p1.r3 == p4.r2 or p1.r3 == p4.r1:
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)

    adjust_arrays1(index3, bre_index)
    adjust_array(index3)
    adjust_arrays1(index5, bre_index)
    adjust_arrays2(index5, bre_index)
    adjust_arrays22(index5, bre_array_not)
    check_and_process_arrays(index5, index3)
    check_and_remove_difference_of_0(index3, bre_index_pred)
    check_and_remove_difference_of_0(index5, bre_index_pred)

    # if index3:
    #     if index3[-1] > len(Instr_Cache) + 4 + 2*len(index3) + len(index5) + 2*len(bre_index):
    #         index3.remove([-1])

    print("index3")
    print(index3)
    print("index5")
    print(index5)
    print("bre_index")
    print(bre_index)

def depend_bypassing_nop(i, q):

    global p11, p22, p33, time, Instr_Cache1
    Instr_Cache = gui_vars.Instr_Cache

    def check_and_remove_difference_of_2(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if abs(value1 - value2) == 2:
                    array2.remove(value2)
                    return  # Exit after processing the first match
                
    def check_and_remove_difference_of_4(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if value2 - value1 == 4:
                    array2.remove(value2)
                    return  # Exit after processing the first match
                
    def check_and_remove_difference_of_4(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if abs(value1 - value2) == 4:
                    array2.remove(value2)
                    return  # Exit after processing the first match

    choose_bre = method.choose_bre
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    bre_index_pred = cycles.bre_index_pred
    Instr_Cache2 = cycles.Instr_Cache1

    do_p1 = 0
    do_p2 = 0
    do_p3 = 0
    do_p4 = 0

    if q == 0:
        index_bypass_instr.clear()
        index_bypass_cycle.clear()
        index_bypass_cycle1.clear()
        index_bypass_cycle2.clear()
        index1.clear()
        index3.clear()
        index4.clear()
        index5.clear()
        index6.clear()
        index7.clear()
        index8.clear()
        # bre_index.clear()
        # bre_array_not.clear()
        # bre_index_pred.clear()
        Instr_Cache1 = Instr_Cache[:]
        positions = []
        positions = find_positions_by_name(Instr_Cache1, "BRE")
        if positions:
            if choose_bre == 1:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
            elif choose_bre == 2:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements1(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
        # for w in Instr_Cache1:
        #     print(w.name)
        
    p11 = i
    p22 = i+1
    p33 = i+2
    p44 = i+3
    time = -10

    if q > 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        p4 = Instr_Cache2[q-3]
        do_p4 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    elif q == 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])
            

    elif q == 1:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    sis1 = 0
    sis2 = 0

    if do_p1 == 1 and do_p2 == 1:
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p2["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"] == p2["r3"] or p1["r2"] == p1["r3"]:
                sis1 = p11
                sis2 = i+1
                index_bypass_instr.append(p11)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                index8.append(sis2) # se poio kyklo ginetai h paroxetefsh
                for value in index8[:]:
                    if any(value == item + 3 for item in bre_index):
                        index8.remove(value)
                for value in index8[:]:
                    if any(value == item + 2 for item in bre_index_pred):
                        index8.remove(value)
                print("index8")
                print(index8)
        if p2["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"] == p2["r3"] or p1["r2"] == p2["r3"]:
                sis1 = p11
                sis2 = i+1
                index_bypass_instr.append(p11)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                index8.append(sis2) # se poio kyklo ginetai h paroxetefsh
                for value in index8[:]:
                    if any(value == item + 3 for item in bre_index):
                        index8.remove(value)
                for value in index8[:]:
                    if any(value == item + 2 for item in bre_index_pred):
                        index8.remove(value)
                print("index8")
                print(index8)

    if do_p1 == 1 and do_p3 == 1:
        if p3["opcode"] == "0010000" and p1["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"] == p3["r1"] or p1["r2"] == p3["r1"]:
                sis1 = p11
                sis2 = i+1
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                index6.append(sis2)
                print("index6")
                print(index6)
                for value in index6[:]:
                    if any(value == item + 3 for item in bre_index):
                        index6.remove(value)
                for value in index6[:]:
                    if any(value == item + 2 for item in bre_index_pred):
                        index6.remove(value)
        if p3["opcode"] == "0010000" and p1["opcode"] == "1110000":
            if p1["r1"] == p3["r1"] or p1["r2"] == p1["r1"]:
                sis1 = p11
                sis2 = i+1
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index) - 1
                index6.append(sis2)
                for value in index6[:]:
                    if any(value == item + 3 for item in bre_index):
                        index6.remove(value)
                for value in index6[:]:
                    if any(value == item + 2 for item in bre_index_pred):
                        index6.remove(value)
        # if p1.opcode in ["0000001", "0000010", "0000011"] and p2.opcode in ["0000001", "0000010", "0000011"]:
        #     if p1.r3 == p2.r1 or p1.r3 == p2.r2:
        #         sis1 = p11
        #         sis2 = sis1 + 3
        #         index_bypass_instr.append(p11)
        #         index_bypass_cycle.append(sis2) # se poio kyklo ginetai h paroxetefsh

    if do_p3 == 1:
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"] == p3["r3"] or p1["r2"] == p3["r3"]:
                sis1 = p11+2
                sis2 = i+3
                index_bypass_cycle1.append(sis2)
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"] == p1["r3"] or p1["r2"] == p3["r3"]:
                sis1 = p11+2
                sis2 = p11+5
                index_bypass_cycle1.append(sis2)

    # if do_p4 == 1:
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0010000"]:
    #         if p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0010000"]:
    #         if p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0100000"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0100000"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode == "1110000":
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode == "1110000":
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)

    print("bypass")
    print(index_bypass_cycle)
    check_and_remove_difference_of_2(bre_index, index_bypass_cycle)
    check_and_remove_difference_of_2(bre_index_pred, index_bypass_cycle)
    check_and_remove_difference_of_4(bre_index, index6)       

def depend_bypassing_freeze(i, q):

    global p11, p22, p33, time, Instr_Cache1
    Instr_Cache = gui_vars.Instr_Cache

    do_p1 = 0
    do_p2 = 0
    do_p3 = 0
    do_p4 = 0

    def check_and_remove_difference_of_2(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if value2 - value1 == 2:
                    array2.remove(value2)
                    return  # Exit after processing the first match
                
    def check_and_remove_difference_of_0(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if abs(value1 - value2) == 0 or abs(value1 - value2) == 1:
                    array2.remove(value2)
                    return  # Exit after processing the first match

    def check_and_remove_difference_of_3(array1, array2):
        """
        Check if any value in array1 and array2 have a difference of 3.
        If found, remove the value from array2.
        """
        for value1 in array1:
            for value2 in array2:
                if abs(value1 - value2) == 3:
                    array2.remove(value2)
                    return  # Exit after processing the first match

    choose_bre = method.choose_bre
    bre_index = cycles.bre_index
    bre_array_not = cycles.bre_array_not
    bre_index_pred = cycles.bre_index_pred
    Instr_Cache2 = cycles.Instr_Cache1

    if q == 0:
        index_bypass_instr.clear()
        index_bypass_cycle.clear()
        index1.clear()
        index3.clear()
        index4.clear()
        index5.clear()
        index6.clear()
        index7.clear()
        index8.clear()
        # bre_index.clear()
        # bre_array_not.clear()
        # bre_index_pred.clear()
        Instr_Cache1 = Instr_Cache[:]
        positions = []
        positions = find_positions_by_name(Instr_Cache1, "BRE")
        if positions:
            if choose_bre == 1:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
            elif choose_bre == 2:
                for pos_index in reversed(range(len(positions))):
                    re = Instr_Cache1[positions[pos_index]]
                    if int(re.r1[1], 16) - int(re.r2[1], 16) == 0:
                        delete_elements1(Instr_Cache1, positions[pos_index], int(re.d))
                    else:
                        pass
        # for w in Instr_Cache1:
        #     print(w.name)
        
    p11 = i
    p22 = i+1
    p33 = i+2
    p44 = i+3
    time = -10

    print("p11")
    print(p11)

    if q > 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        p4 = Instr_Cache2[q-3]
        do_p4 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    elif q == 2:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        p3 = Instr_Cache2[q-2]
        do_p3 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])
            

    elif q == 1:
        p1 = Instr_Cache2[q]
        do_p1 = 1
        p2 = Instr_Cache2[q-1]
        do_p2 = 1
        for w in Instr_Cache2:
            print(w["name"])
            print(w["r1"])
            print(w["r2"])

    sis1 = 0
    sis2 = 0

    if do_p1 == 1 and do_p2 == 1:
        if p2["opcode"] == "0010000" and p1["opcode"] in ["0000001", "0000010", "0000011", "1110000"]:
            if p1["r1"] == p2["r1"] or p1["r2"] == p2["r1"]:
                sis1 = p11 + 4
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # # if bre_index_pred:
                # #     sis2 = sis2 + 2*len(bre_index_pred)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                # if index4:
                #     sis2 = sis2 + len(index4)
                index1.append(sis1) # se poio kyklo ginetai h paroxetefsh
                index4.append(sis2) # se poio kyklo einai to AE'
                # check_and_remove_difference_of_2(bre_index, index4)
                print("index4")
                print(index4)
        if p2["opcode"] == "0010000" and p1["opcode"] == "1110000":
            if p1["r1"] == p2["r1"] or p1["r2"] == p2["r1"]:
                sis1 = p11 + 4
                sis2 = i
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index_pred:
                #     sis2 = sis2 + 2*len(bre_index_pred)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                # if index4:
                #     sis2 = sis2 + len(index4)
                index1.append(sis1) # se poio kyklo ginetai h paroxetefsh
                index4.append(sis2) # se poio kyklo einai to AE'
                # check_and_remove_difference_of_2(bre_index, index4)
                print("index4")
                print(index4)
                
        if p1["opcode"] in ["0000001", "0000010", "0000011"] and p2["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"] == p2["r3"] or p1["r2"] == p2["r3"]:
                sis1 = p11 + 4
                sis2 = i+1
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                # if bre_index_pred:
                #     sis2 = sis2 + 2*len(bre_index_pred)
                # if index4:
                #     sis2 = sis2 + len(index4)
                index1.append(sis1) # se poio kyklo ginetai h paroxetefsh
                index8.append(sis2) # se poio kyklo einai to AE'
                print("index8")
                print(index8)
                check_and_remove_difference_of_3(bre_index, index8)
        if p2["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"] == p2["r3"] or p1["r2"] == p2["r3"]:
                sis1 = p11 + 4
                sis2 = i+1
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                # # if bre_index_pred:
                # #     sis2 = sis2 + 2*len(bre_index_pred)
                # if index4:
                #     sis2 = sis2 + len(index4)
                index1.append(sis1) # se poio kyklo ginetai h paroxetefsh
                index8.append(sis2) # se poio kyklo einai to AE'
                print("index8")
                print(index8)
                check_and_remove_difference_of_3(bre_index, index8)

    if do_p3 == 1:
        if p3["opcode"] == "0010000" and p1["opcode"] in ["0000001", "0000010", "0000011", "1110000"]:
            if p1["r1"] == p3["r1"] or p1["r2"] == p3["r1"]:
                sis1 = p11 + 4
                sis2 = i+1
                # if index4:
                #     sis2 = sis2 + len(index4)
                # # if bre_index_pred:
                # #     sis2 = sis2 + 2*len(bre_index_pred)
                # if bre_array_not:
                #     sis2 = sis2 + 2*len(bre_array_not)
                # if bre_index:
                #     sis2 = sis2 + 2*len(bre_index)
                index1.append(sis1) # se poio kyklo ginetai h paroxetefsh
                index7.append(sis2) # se poio kyklo einai to AE'
                check_and_remove_difference_of_3(bre_index, index7)
            
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] in ["0000001", "0000010", "0000011"]:
            if p1["r1"] == p3["r3"] or p1["r2"] == p3["r3"]:
                sis1 = p11+2
                sis2 = i+3
                index_bypass_cycle1.append(sis2)
        if p3["opcode"] in ["0000001", "0000010", "0000011"] and p1["opcode"] == "1110000":
            if p1["r1"] == p1["r3"] or p1["r2"] == p3["r3"]:
                sis1 = p11+2
                sis2 = p11+5
                index_bypass_cycle1.append(sis2)
            
    # if do_p4 == 1:
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0010000"]:
    #         if p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0000001", "0000010", "0000011"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0010000"]:
    #         if p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["0100000"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["0100000"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0000001", "0000010", "0000011"] and p4.opcode in ["1110000"]:
    #         if p1.r3 == p4.r1 or p1.r3 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)
    #     if p1.opcode in ["0010000"] and p4.opcode in ["1110000"]:
    #         if p1.r1 == p4.r1 or p1.r1 == p4.r2:
    #             sis1 = p11+2
    #             sis2 = p11+4
    #             index_bypass_cycle2.append(sis2)

    check_and_remove_difference_of_2(bre_index, index4)
    check_and_remove_difference_of_2(bre_index_pred, index8)
    check_and_remove_difference_of_3(bre_index_pred, index7)
    check_and_remove_difference_of_0(bre_index_pred, index4)
    check_and_remove_difference_of_0(index4, index7)