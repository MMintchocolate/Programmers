def solution(a, b):
    answer = 0
    if a > b:
        big = a
        small = b
    elif b > a:
        big = b
        small = a
    else:
        return a
    for i in range(small, big+1):
        answer+=i
    return answer