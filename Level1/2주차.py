scores = [[100,50,50],[50,100,50],[50,50,100]]

def solution(scores):
    point = [[0 for col in range(len(scores))] for row in range(len(scores))] # 2차원 배열 생성 잘 알아두기. 여기서 문제가 발생했었음.
    for i in range(0, len(scores)):
        for j in range(0, len(scores[i])):
            point[j][i] = scores[i][j]
    answer = ''
    max = 0
    min = 0     
    for i in range(0, len(scores)):
        max = point[i][0]
        min = point[i][0]
        max_count = 0
        min_count = 0
        sum = 0
        avg = 0
        switch_max = 0
        switch_min = 0
        for j in range(1, len(point[i])):
            if max < point[i][j]:
                max = point[i][j]
                max_count = 0
            elif max == point[i][j]:
                max_count = 1
            if min > point[i][j]:
                min = point[i][j]
                min_count = 0
            elif min == point[i][j]:
                min_count = 1
        for l in range(0, len(point[i])):
            sum += point[i][l]
        for k in range(0, len(point[i])):
            if i == k and point[i][k] == max and max_count == 0:
                avg = (sum - max) / (len(scores[i]) - 1)
                switch_max = 1
                break
            elif i == k and point[i][k] == min and min_count == 0:
                avg = (sum - min) / (len(scores[i]) - 1)
                switch_min = 1
                break
            else:
                pass
        if switch_max == 0 and switch_min == 0:
            avg = sum / len(point[i])
        if avg >= 90:
            answer += 'A'
        elif 90 > avg and avg >= 80:
            answer += 'B'
        elif 80 > avg and avg >= 70:
            answer += 'C'
        elif 70 > avg and avg >= 50:
            answer += 'D'
        elif 50 > avg:
            answer += 'F'
    return answer
print(solution(scores))