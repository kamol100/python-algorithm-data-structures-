def int_to_roman(num):
    romanList = [
        ["I", 1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],
        ["C",100],["CD",400],["D",500],["CM",900],["M",1000]
    ]

    res = ""
    for sym, val in reversed(romanList):
        #print(sym,val)
        if num //val:
            count = num//val
            res += (sym * count)
            num = num % val
    return res








print(int_to_roman(1994))
print(int_to_roman(3))
