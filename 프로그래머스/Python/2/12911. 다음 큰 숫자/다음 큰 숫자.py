def solution(n):
    next_n = n + 1
    binar = bin(n)[2:]
    cnt_n = sum(map(int, binar))
    
    while next_n > n:
        next_bin = bin(next_n)[2:]
        cnt_next_bin = sum(map(int, next_bin))
        if cnt_next_bin == cnt_n:
            return next_n
        next_n+=1
