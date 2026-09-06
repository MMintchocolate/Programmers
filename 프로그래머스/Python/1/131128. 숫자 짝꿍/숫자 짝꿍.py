def solution(X, Y):
    countX = [0]*10
    countY = [0]*10
    
    for ch in X:
        countX[int(ch)] += 1
    for ch in Y:
        countY[int(ch)] += 1

    common = [min(countX[d], countY[d]) for d in range(10)]

    if sum(common) == 0:
        return "-1"

    result = ''.join(str(d) * common[d] for d in range(9, -1, -1))

    if result[0] == '0':
        return "0"
    
    return result