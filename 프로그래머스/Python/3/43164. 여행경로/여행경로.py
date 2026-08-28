'''
인천 -> 
인천에서 시작하는 리스트 함수 시작하고
visited 체크 하고
전체 돌린 다음 경로를 answer에 append 하고
다음 인천에서 시작하는 함수 또 시작
'''
    
def solution(tickets):
    tickets.sort()
    target = len(tickets)
    visited = [False] * target
    answer = []
    
    def sol(start, road):
        if len(road) == target+1:
            answer.append(road[:])
            return
        
        for i in range(target):
            if visited[i] == False and tickets[i][0] == start:
                visited[i] = True
                road.append(tickets[i][1])
                sol(tickets[i][1], road)
                visited[i] = False
                road.pop()
                
    sol("ICN", ["ICN"])
    
    return answer[0]