def solution(people, limit):
    people.sort()
    answer = 0
    low, high = 0, len(people) - 1
            
    while low <= high:
        if people[low] + people[high] <= limit:
            low += 1
        high -= 1
        answer += 1
    return answer