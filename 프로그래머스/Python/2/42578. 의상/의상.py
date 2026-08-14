def solution(clothes):
    clothes_hash = {}
    for i in clothes:
        if i[1] not in clothes_hash:
            clothes_hash[i[1]] = [i[0]]
        else: 
            clothes_hash[i[1]].append(i[0])
    answer = 1
    cnt = 1
    for v in clothes_hash.values():
        cnt*=(len(v)+1)
    answer = cnt - 1
    return answer