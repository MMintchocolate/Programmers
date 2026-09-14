from collections import deque

def solution(order):
    answer = 0
    stack = []
    queue = deque(order)
    for i in range(1,len(order)+1):
        stack.append(i)
        while stack and stack[-1] == queue[0]:
            answer+=1
            stack.pop()
            queue.popleft()
    return answer