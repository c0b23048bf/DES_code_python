def tennti(table, num):
    return_lst = []
    for i in table:
        return_lst.append(num[i-1])
    return "".join(return_lst)


def split(str2):
    long = len(str2) // 2
    result1 = str2[:long]
    result2 = str2[long:]
    return result1, result2


if __name__ == '__main__':
    hirabunn = "0000101101000001000101101000001000101101000001000101101000001000"
    
    start_t = tennti([
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
        ], hirabunn)
    print(start_t)
    
    sp2 = split(start_t)
    print(sp2)
    
    print("初期転置前半:" + sp2[0] + ", 長さ:" + str(len(sp2[0])) + \
        "\n初期転置後半:" + sp2[1] + ", 長さ:" + str(len(sp2[1])))