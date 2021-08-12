def solution(x, n):
    answer = []
    temp = x
    for i in range(0, n):
        answer.append(x)
        x += temp
    return answer