def sol2(num):
    num = int(num)
    if  num< 2:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return 0
    return 1

def solution(numbers):
    n = len(numbers)
    used = [False]*n
    result = set()
    def sol(now):
        if now:
            result.add(int(now))

        for i in range(n):
            if not used[i]:
                used[i] = True
                sol(now+numbers[i])
                used[i] = False
    sol("")
    return sum(sol2(i) for i in result)