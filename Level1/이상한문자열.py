s='There  is so many tears'
def solution(s):
    answer = ''
    '''
    너무 어렵게 생각하고 너무 어렵게 풀었다. 간단하게 풀어야겠다.
    temp = []
    space = ''
    for i in range(0, len(s)): #공백의 갯수를 세어 space에 저장 후 각각의 위치에 도달하기 위해 temp에 저장
        if s[i] == ' ':
            space += ' '
        else:
            temp.append(space)
            space = ''
    while '' in temp: #공백 말고 아무것도 없는 경우를 제외하기 위한 while문
        temp.remove('')
    s = s.split() #s를 공백 기준으로 나눈다.
    print(temp)
    count = 0
    for i in range(0, len(s)): #각 단어별로
        for j in range(0, len(s[i])): #각 단어의 인덱스 위치에 따라 대소문자 변환
            s2 = ''
            if j % 2 == 0:
                if s[i][j].isupper() == True:
                    s2 += s[i][j]
                else:
                    s2 += s[i][j].upper()
            else:
                if s[i][j].islower() == True:
                    s2 += s[i][j]
                else:
                    s2 += s[i][j].lower()
        
        s2 += temp[count]
        if count < len(temp):
            count += 1
        answer += s2
    '''
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