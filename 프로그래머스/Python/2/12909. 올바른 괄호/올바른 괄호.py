from collections import deque

def solution(s):
    li = []
    
    for i in s:
        if  i =="(":
            li.append(i)
        elif i == ")":
            if not li:
                return False
            li.pop()
    return not li