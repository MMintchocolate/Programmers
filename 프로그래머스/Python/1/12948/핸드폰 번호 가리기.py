def solution(phone_number):
    masking = len(phone_number)-4
    answer = '*'*masking + phone_number[-4:]
    return answer