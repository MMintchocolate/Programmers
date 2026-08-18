import heapq

def solution(operations):
    heap = []
    heapq.heapify(heap)
    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
            continue
        if not heap:
                continue
        if int(i[2:]) < 0:
            heapq.heappop(heap)
        else:
            heap.sort()
            heap.pop()
    if not heap:
        answer = [0,0]
    else:
        answer = [max(heap), heapq.heappop(heap)] 
    return answer