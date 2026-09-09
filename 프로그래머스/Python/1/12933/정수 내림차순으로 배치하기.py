def solution(n):
    numbers = sorted(str(n), reverse = True)
    answer = "".join(numbers)
    return int(answer)