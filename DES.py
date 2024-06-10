def tennti(table, num):
    return_lst = []
    for i in table:
        return_lst.append(num[i-1])
    return "".join(return_lst)


# def ls(x):
#     long = len(x)
#     light_shift = int(x, 2) << 1
#     return f"{light_shift:b}".zfill(long)


def ls(x, n):
    return x[n:] + x[:n]


def f_split(x, k):
    r_l = []
    long = len(x) // k
    for i in range(k):
        r_l.append(x[i*long:(i+1)*long])
    print(r_l)
    return r_l


def xor(x, y):
    long = len(x) + len(y)
    xor = int(x, 2) ^ int(y, 2)
    return f"{xor:b}".zfill(long)


def f(key, input):
    SBOX = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    k_input = tennti([
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ], input) 
    print("拡大転置後:" + k_input)
    
    f_xor_l = []
    for i, n in zip(f_split(key, 8), f_split(k_input, 8)):
        a = int(i, 2) ^ int(n, 2)
        f_xor_l.append(f"{a:b}".zfill(6))
    print("aa")
    print(f_xor_l)
    print("aa")
        
    sbox_lst = []
    for i, (n, m) in enumerate(zip(SBOX, f_xor_l)):
        a = m[0] + m[5]
        b = m[1:5]
        print(a,b)
        num = SBOX[i][int(a, 2)][int(b, 2)]
        print(i, int(a, 2), int(b, 2), SBOX[i][int(a, 2)][int(b, 2)])
        sbox_lst.append(f"{num:b}".zfill(4))
    print(sbox_lst)
    sbox =  "".join(sbox_lst)
    print("sbox:" + str(len(sbox)) + sbox)
    result = tennti([
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26, 
        5, 18, 31, 10, 
        2, 8, 24, 14, 
        32, 27, 3, 9, 
        19, 13, 30, 6, 
        22, 11, 4, 25
        ], sbox)
    
    return result

def change_key(gakuseki, long):
    k2 = f"{gakuseki:b}"*4
    return k2.zfill(long)
    
    
def split(str2):
    long = len(str2) // 2
    result1 = str2[:long]
    result2 = str2[long:]
    return result1, result2


def merge(str2_1, str2_2):
    return str2_1 + str2_2


if __name__ == '__main__':
    key = "1001111101010101010100000110100010110010100111101110101000111001"
    
    pc1 = tennti([57, 49, 41, 33, 25, 17, 9,
                  1, 58, 50, 42, 34, 26, 18,
                  10, 2, 59, 51, 43, 35, 27,
                  19, 11, 3, 60, 52, 44, 36,
                  63, 55, 47, 39, 31, 23, 15,
                  7, 62, 54, 46, 38, 30, 22,
                  14, 6, 61, 53, 45, 37, 29,
                  21, 13, 5, 28, 20,12, 4
                  ], key)
    print(pc1)
    
    sp1 = split(pc1)
    print(sp1)
    
    ls1_1 = ls(sp1[0], 1)
    print(ls1_1)
    
    ls1_2 = ls(sp1[1], 1)  
    print(ls1_2)  
    
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
    print(str(len(pc2)) + ":" + pc2)
    
    #   初期転置
    #gaku_bann = input("学籍番号下5桁を入力せよ")
    gaku_bann = 23048
    hirabunn = change_key(gaku_bann, 64) # 普段は
    print("a :" + hirabunn + str(len(hirabunn)))
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
    
    f1 = f(pc2, sp2[1])
    print(f1)
    
    xor1 = int(sp2[0], 2) ^ int(f1, 2)
    xor1 = f"{xor1:b}".zfill(32)
    print("s" + xor1)