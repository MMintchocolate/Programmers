def solution(s):
    numbers = list(map(int, s.split()))
    min_num = min(numbers)
    max_num = max(numbers)
    answer = ' '.join([str(min_num), str(max_num)])
    return answer