def solution(s):
    answer = True
    cnt = 0
    for i in s:
        cnt+=1
        if not i.isdigit():
            answer = False
    if cnt != 4 and cnt!=6:
        answer = False
    return answer