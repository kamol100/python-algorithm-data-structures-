def zigzag_conversion(str,row):
    if row == 1 : return str
    result = ""
    for r in range(row):
        step = 2 * (row-1)
        for i in range(r, len(str), step):
            result += str[i]
            if r > 0 and r < row -1 and i + step - 2 * r < len(str):
                result += str[i + step - 2 * r]
    return result




"PAYPALISHIRING"
4

print(zigzag_conversion("PAYPALISHIRING", 4))#PAHN APLSIIG # YIR
#PIN ALSIG YAHR PI