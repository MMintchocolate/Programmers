from collections import deque

def solution(maps):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    n = len(maps)
    m = len(maps[0])
    answer = -1
    visited = [[False]*m for i in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    while queue:
        y, x, cnt = queue.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx, cnt+1])

    
    return answer