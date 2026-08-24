def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def sol(total, depth):
        nonlocal answer
        if depth == n:
            if total == target:
                answer += 1
            return
        sol(total + numbers[depth], depth + 1)
        sol(total - numbers[depth], depth + 1)

    sol(0, 0)
    return answer