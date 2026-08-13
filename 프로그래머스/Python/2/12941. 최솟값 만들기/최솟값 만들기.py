def solution(A,B):
    B.sort()
    A.sort()
    answer = 0
    for i in range(len(A)):
        A_min = A.pop(0)
        B_max = B.pop()
        answer+=A_min*B_max

    return answer