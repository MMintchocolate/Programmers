from collections import deque

def solution(x, y, n):
    arr = deque([(x,y,0)])
    visited = {x}
    while arr:
        nx, ny, cnt = arr.popleft()
        
        if nx == ny:
            return cnt
        if nx+n <= y and nx+n not in visited:
            arr.append((nx+n, ny, cnt+1))
            visited.add(nx+n)
        if nx*2 <= y and nx*2 not in visited:
            arr.append((nx*2, ny, cnt+1))
            visited.add(nx*2)
        if nx*3 <= y and nx*3 not in visited:
            arr.append((nx*3, ny, cnt+1))
            visited.add(nx*3)
    return -1
