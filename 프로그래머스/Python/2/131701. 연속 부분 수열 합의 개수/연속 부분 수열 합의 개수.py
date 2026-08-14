ans = set()

def sol(total, start, elements, n):
    new_elements=elements + elements 
    for i in range(start, start + n):
        total+=new_elements[i]
        ans.add(total)
    

def solution(elements):
    n = len(elements)
    for i in range(n):
        sol(0,i, elements, n)
    answer = len(ans)
    return answer