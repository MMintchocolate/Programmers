def solution(progresses, speeds):
    answer = []
    cnt = 0
    idx = 0
    day = 1
    while progresses:
        if idx == len(progresses):
            answer.append(cnt)
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            cnt = 0
            idx = 0
            day += 1
            continue

            break
        first = progresses[idx] + speeds[idx]*day
        
        if first >= 100:
            cnt+=1
            idx+=1
        else:
            if cnt > 0:
                answer.append(cnt)
                for i in range(cnt):
                    progresses.pop(0)
                    speeds.pop(0)
                cnt = 0
                idx = 0
            day+=1
            
    return answer