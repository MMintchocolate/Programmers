def solution(priorities, location):
    max_n = max(priorities)
    leng = len(priorities)
    idx = 0
    answer = 0
    while priorities[location] != 0:
        if priorities[idx] < max_n:
            idx=(idx+1)%leng
        elif priorities[idx]==max_n:
            priorities[idx] = 0
            answer+=1
            max_n = max(priorities)
            idx=(idx+1)%leng
    return answer