s='There  is so many tears'
def solution(s):
    answer = ''
    count = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
        else:
            if count % 2 == 0:
                if s[i].isupper() == True:
                    answer += s[i]
                    count += 1
                else:
                    answer += s[i].upper()
                    count += 1
            else:
                if s[i].islower() == True:
                    answer += s[i]
                    count += 1
                else:
                    answer += s[i].lower()
                    count += 1
    return answer
print(solution(s))