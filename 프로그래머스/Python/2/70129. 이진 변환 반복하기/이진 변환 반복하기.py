cnt = 0
zero_cnt = 0
    
def solution(s):
    global cnt
    global zero_cnt
    
    
    while s != '1':
        cnt+=1
        zero = s.count('0')
        
        zero_cnt+=zero
        s = s.replace('0', "")
        
        s = bin(len(s))[2:]
        
    answer = [cnt, zero_cnt]
    
    return answer