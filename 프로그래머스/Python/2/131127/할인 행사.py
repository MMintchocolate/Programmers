def solution(want, number, discount):
    day = len(discount)
    item = {}
    for i,j in zip(want, number):
        item[i] = j
    answer = 0
    for i in range(day-9):
        total = sum(number)
        target = item.copy()
        for j in discount[i:10+i]:
            if j not in item or target[j] == 0: break
            total-=1
            target[j]-=1
            
        if total == 0:
            answer+=1
    return answer