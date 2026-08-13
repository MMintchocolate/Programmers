def solution(s):
    s_list = s.split(' ')
    for i in range(len(s_list)):
        if s_list[i] == '':
            continue 
        elif 48<=ord(s_list[i][0])<=57:
            s_list[i] = s_list[i].lower()
        else:
            s_list[i] = s_list[i][0].upper() + s_list[i][1:].lower()
    answer = ' '.join(s_list)
    return answer