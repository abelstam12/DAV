import numpy as np

CENTRUM = [11, 12, 18, 17, 16, 15]
INDUSTRIE_CORPORATE = [14, 43, 42, 44, 41, 45, 46, 47, 99, 96, 101, 105]
OUD_ZUID = [75, 71, 77]
# nieuw west bos en lommere etc
NIEUWBOUW = [67, 69, 60, 64, 65, 63, 62, 56, 57, 56, 55]

def catagorized_postal(postal_array):
    cen = np.zeros(len(postal_array))
    indus = np.zeros(len(postal_array))
    oud = np.zeros(len(postal_array))
    nieuw = np.zeros(len(postal_array))
    nummerical = get_numeric_postal(postal_array) - 1000
    print(nummerical)
    c, j, o, n = 0,0,0,0
    for i in range(len(postal_array)):
        print(i)
        if int(nummerical[i]) in CENTRUM:
            cen[i] = 1
            c += 1
        if int(nummerical[i]) in INDUSTRIE_CORPORATE:
            indus[i] = 1
            j += 1
        if int(nummerical[i]) in OUD_ZUID:
            oud[i] = 1
            o += 1
        if int(nummerical[i]) in NIEUWBOUW:
            nieuw[i] = 1
            n += 1
    print(c, j, o, n) 
    result = np.array([cen, indus, oud, nieuw])
    print(result)
    return result





def get_numeric_postal(pd_postal_column):
    pc = np.array(pd_postal_column)
    for index in range(len(pc)):
        pc[index] = int(pc[index][0:4])
    return pc
    