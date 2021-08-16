def solution(brown, yellow):
    answer = []
    yellow_width = 0
    yellow_height = 0
    area = brown + yellow
    for i in range(1, yellow + 1):
        if 2 * i + 2 * (yellow / i) + 4 == brown:
            yellow_width = i
            yellow_height = yellow / i
    answer.append(yellow_width + 2)
    answer.append(yellow_height + 2)
    return answer