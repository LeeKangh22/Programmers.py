def solution(s):
    answer = 0
    if s[0] == '+':
        s.replace('+','')
        answer = int(s)
    else:
        answer = int(s)
    return answer