table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
def solution(table, languages, preference):
    answer = ''
    temp = [] #각 직업군 별 언어를 공백 기준으로 스플릿 하여 넣어놓을 값
    pref = [] #직업군 별 직업군 언어 점수 * 언어 선호도 곱하여 넣을 값 
    score = 0
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
print(solution(table,languages,preference))