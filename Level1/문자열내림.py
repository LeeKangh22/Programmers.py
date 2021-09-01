def solution(s):
    answer = ''
    temp = []
    for i in range(0, len(s)):
        temp.append(s[i])
    temp.sort(reverse = True)
    
    for i in range(0, len(temp)):
        answer += temp[i]
    return answer
