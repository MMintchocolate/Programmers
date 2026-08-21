def solution(k, dungeons):
    answer = -1
    check = [False] * len(dungeons)
    def sol(now_k, n):
        nonlocal answer
        answer=max(answer, n)
        if n == len(dungeons):
            return
        
        for i in range(len(dungeons)):
            if check[i] == True: continue
            if dungeons[i][0] <= now_k:
                check[i] = True
                sol(now_k-dungeons[i][1], n+1)
                check[i] = False
    sol(k, 0)
    return answer