def solution(number, k):
    answer = -1
    stack = []
    for i in number:
        while stack and stack[-1]<i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k>0:
        stack = stack[:-k]
    answer = "".join(stack)
    return answer