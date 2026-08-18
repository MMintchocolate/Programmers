import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_sco = heapq.heappop(scoville)
        if min_sco >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        min_sco+=(heapq.heappop(scoville)*2)
        answer+=1
        heapq.heappush(scoville, min_sco)
    return answer







