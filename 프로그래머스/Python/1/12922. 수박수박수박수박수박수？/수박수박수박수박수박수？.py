def solution(n):
    arr = ""
    a = "수"
    b = "박"
    cnt = 0
    while True:
        if cnt == n:
            break
        cnt+=1
        arr+=a
        if cnt == n:
            break
        cnt+=1
        arr+=b
    return arr