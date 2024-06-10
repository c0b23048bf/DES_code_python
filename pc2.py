def tennti(table, num):
    return_lst = []
    for i in table:
        return_lst.append(num[i-1])
    return "".join(return_lst)


def merge(str2_1, str2_2):
    return str2_1 + str2_2


if __name__ == '__main__':
    ls1_1 = "1110001010011101101100010110"
    ls1_2 = "1110001001000111110100101110"
    merge1 = merge(ls1_1, ls1_2)
    print(merge1)
    
    pc2 = tennti([
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
        ], merge1)
    print("結果:" + pc2 + ", 長さ" + str(len(pc2)))