def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper() and (ord(i) + n) > 90:
            answer += chr(ord(i) + n - 26)
        elif i.islower() and (ord(i) + n) > 122:
            answer += chr(ord(i) + n - 26)
        elif i == ' ':
            answer += i
        else:
            answer += chr(ord(i) + n)
    return answer


