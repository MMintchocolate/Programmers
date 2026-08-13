def solution(brown,yellow):
    total = brown + yellow
    for width in range(total, 2, -1):
        if total % width != 0:
            continue
        if width < total// width:
            continue
        height = total // width
        if (width - 2) * (height - 2) == yellow:
            return [width, height]
    return answer

