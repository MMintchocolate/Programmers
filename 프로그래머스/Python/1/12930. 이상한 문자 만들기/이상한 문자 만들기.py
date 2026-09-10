def solution(s):
    n = len(s)
    answer = ''
    idx = 0
    for i in s:
        if i==" ":
            answer+=i
            idx =0
        elif idx%2==1:
            answer+=i.lower()
            idx+=1
        else:
            answer+=i.upper()
            idx+=1
            
    return answer