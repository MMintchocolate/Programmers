def solution(x):
    answer = True
    x_sum = 0
    xx = x
    while x>0:
        x_sum+=(x%10)
        x//=10
    if xx%x_sum == 0:
        answer = True
    else:
        answer = False
    return answer