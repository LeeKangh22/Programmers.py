def solution(table, languages, preference):
    answer = ''
    temp = [] #각 직업군 별 언어를 공백 기준으로 스플릿 하여 넣어놓을 값
    pref = [] #직업군 별 직업군 언어 점수 * 언어 선호도 곱하여 넣을 값 
    score = 0
    #테이블에서 한 직업 당 스플릿한다.
    #이후 언어에서 그 직업의 언어 점수를 수식으로 곱하여 직업당 점수를 계산한다.
    #이를 모두 저장하고 가장 큰 값을 찾아낸다.
    for i in range(0, len(table)):
        temp = table[i].split()
        for j in range(0, len(temp)):
            for k in range(0, len(languages)):
                if temp[j] == languages[k]:
                    score += ((6 - j) * preference[k])
                else:
                    score += 0
        pref.append(score)
        score = 0
    max = pref[0]
    lan_temp = []
    for i in range(1, len(pref)):
        if max <= pref[i]:
            max = pref[i]
    # 점수가 가장 큰 직업을 다 넣어놓고 사전순으로 정렬하여 가장 처음에 위치한 직업을 출력한다.
    if pref[0] == max:
        lan_temp.append('SI')
    if pref[1] == max:
        lan_temp.append('CONTENTS')
    if pref[2] == max:
        lan_temp.append('HARDWARE')
    if pref[3] == max:
        lan_temp.append('PORTAL')
    if pref[4] == max:
        lan_temp.append('GAME')
    lan_temp.sort()
    answer = lan_temp[0]
            
    return answer
