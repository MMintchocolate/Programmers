def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if not stack:
                answer = False
                break
            stack.pop()
    if stack:
        answer = False
    return answer