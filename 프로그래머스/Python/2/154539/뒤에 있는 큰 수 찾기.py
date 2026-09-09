def solution(numbers):
    stack = []
    n = len(numbers)
    answer = [-1] * n
    
    for i in range(n):
        while stack and numbers[stack[-1]] <numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)
    return answer