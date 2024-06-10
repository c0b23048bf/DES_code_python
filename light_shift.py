def split(str2):
    long = len(str2) // 2
    result1 = str2[:long]
    result2 = str2[long:]
    return result1, result2


def ls(x, n):
    return x[n:] + x[:n]


if __name__ == '__main__':
    pc1 = "01110001010011101101100010110111000100100011111010010111"
    sp1 = split(pc1)
    print(sp1)
    
    ls1_1 = ls(sp1[0], 1)
    print(ls1_1)
    
    ls1_2 = ls(sp1[1], 1)  
    print(ls1_2)