for t in range(0, (int)(input())):
    strA = input()
    strB = input()
    length = len(strA) + len(strB)
    result = []
    strA = strA + '~'
    strB = strB + '~'
    for j in range(0, length):
        if(strA <= strB):
            result.append(strA[0])
            strA = strA[1:]
        else:
            result.append(strB[0])
            strB = strB[1:]
    print("".join(result))