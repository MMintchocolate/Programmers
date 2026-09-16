def solution(arr1, arr2):
    n = len(arr1)        # arr1의 행 개수
    m = len(arr2[0])     # arr2의 열 개수
    k = len(arr2)         # arr1의 열 개수 = arr2의 행 개수

    answer = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for x in range(k):
                answer[i][j] += arr1[i][x] * arr2[x][j]

    return answer