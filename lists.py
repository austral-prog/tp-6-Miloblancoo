# Replace the "ANSWER HERE" with your answer

def remove_elements(list):
    if len(list) > 5: 
        del list[5]
    if len(list) > 4: 
        del list[4]
    if len(list) > 0: 
        del list[0]
    return list


def add_elements(list):
    return ['Pink'] + list + ['Yellow']


def is_empty(list):
    return list == [] 


def check_lists(list1, list2):
    if len(list1) > 2 and len(list2) > 2:
        return list1[2] == list2[2]
    else:
        return False


def list_of_lists(list):
    primero = list[0][:2]
    segundo = list[1][1:4]
    tercero = list[2][-2:]
    return [primero, segundo, tercero]
ejemplo = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
