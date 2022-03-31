
def reflect(arr):
    reflect = []
    for i in range(3):
        lst = []
        for j in range(2,-1,-1):
            lst.append(arr[i][j])
        reflect.append(lst)
    return reflect

def rotate(arr):
    rotate = []
    for j in range(3):
        lst = []
        for i in range(2,-1,-1):
            lst.append(arr[i][j])
        rotate.append(lst)
    return rotate

def total_sum(s, arr):
    total = []
    for rows in range(3):
        total_rows = []
        for cols in range(3):
            sum_value = abs(s[rows][cols] - arr[rows][cols])
            total_rows.append(sum_value)
        #print(total_rows)
        total.append(sum(total_rows))
    return sum(total)

def formingMagicSquare(s):
    ms = [[4,3,8],
          [9,5,1],
          [2,7,6]]
    totals = []
    for total in range(4):
        totals.append(total_sum(s,ms))
        reflect_ms = reflect(ms)
        print("=====reflect====")
        print(reflect_ms)
        totals.append(total_sum(s, reflect_ms))
        ms = rotate(ms)
        print("======rotate=======")
        print(ms)
    return min(totals)


s = [[4,8,2],[4,5,7],[6,1,6]]
#print(formingMagicSquare(s))
#print("==========")
s = [[4,9,2],[3,5,7],[8,1,5]]
#print(formingMagicSquare(s))
print("============")
s = [[5,3,4],[1,5,8],[6,4,2]]
print(formingMagicSquare(s))
