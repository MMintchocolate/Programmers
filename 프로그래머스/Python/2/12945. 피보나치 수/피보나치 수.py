pibo = [0,1]

def solution(n):
    for i in range(2,n+1):
        new = pibo[i-1] + pibo[i-2]
        pibo.append(new)
    answer = pibo[n]%1234567
    return answer