def solution(arr):
    li = []
    answer = max(arr)
    can = True
    while can:
        for i in arr:
            if answer%i == 0:
                can = False
            else:
                can = True
                break
        answer+=1
    return answer-1