excel = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
         "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lenExcel = len(excel) # 26

def convert_to_title(col_number: int) -> str:
    n_lettere = col_number // lenExcel
    ret = ""
    nLettereI = n_lettere
    for i in range(n_lettere+1):
        temp = nLettereI % lenExcel
        ret += excel[temp]
        nLettereI -= lenExcel
    return ret

def convert_to_title(col_number: int) -> str:
    ret = ""
    while(col_number > 0):
        resto = (col_number -1) % 26
        ret = excel[resto] + ret
        col_number = (col_number -1) // 26
    return ret

print(convert_to_title(26))

print(convert_to_title(27))

print(convert_to_title(28))

print(convert_to_title(701))