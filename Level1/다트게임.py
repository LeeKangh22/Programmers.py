dartResult = "1S2D*3T" #nedd resolving
answer = 0
def solution(dartResult):
    dartResult += ' ' # index error 방지를 위해 삽입, 애초에 접근 자체가 안된다. 
    answer = 0
    before = 0
    score = 0
    i = 0
    while i < len(dartResult): # 파이썬에서는 for문 index 변경이 불가능하다. 따라서 While문을 이용한 indexing을 진행
        if dartResult[i] >= '0' and dartResult[i] <= '9':
            before = score
            if dartResult[i + 1] == '0':
                score = 10
                i += 1
            else:
                score = int(dartResult[i])
        elif dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if dartResult[i] == 'D':
                score = pow(score, 2)
            elif dartResult[i] == 'T':
                score = pow(score, 3)

            if dartResult[i + 1] == '*':
                answer -= before
                before *= 2
                score *= 2
                i += 1
                answer += before;
            elif dartResult[i + 1] == '#':
                score *= -1
                i += 1
            answer += score
        i += 1
    return answer
answer = solution(dartResult)
print(answer)