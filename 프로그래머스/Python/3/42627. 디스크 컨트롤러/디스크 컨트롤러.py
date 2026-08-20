import heapq

def solution(jobs):
    jobs = sorted(jobs)  
    n = len(jobs)
    i = 0
    heap = []
    time = 0
    total = 0

    while i < n or heap:
        while i < n and jobs[i][0] <= time:
            s, l = jobs[i]
            heapq.heappush(heap, (l, s))
            i += 1

        if not heap:
            time = jobs[i][0]
            continue

        l, s = heapq.heappop(heap)
        time += l
        total += (time - s)

    return total // n