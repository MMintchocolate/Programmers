def solution(n, computers):
    visited = [False] * n
    answer = 0
    def sol(start):
        visited[start] = True
        for i in range(n):
            if computers[start][i] == 1 and visited[i] == False:
                sol(i)
                
    for i in range(n):
        if visited[i] == False:
            sol(i)
            
            answer += 1
    
    return answer