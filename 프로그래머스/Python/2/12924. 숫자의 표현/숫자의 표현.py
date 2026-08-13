cnt = 1

def sol(now_s, s):
    global cnt
    
    for i in range(now_s+1, s+1):
        if now_s+i == s:
            cnt+=1
        if now_s+i > s:
            return
        now_s+=i

        

def solution(n):
    for i in range(1,n+1):
        sol(i,n)
    answer = cnt
    return answer

