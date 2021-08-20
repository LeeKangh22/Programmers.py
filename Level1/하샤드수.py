def solution(x):
    answer = True
    temp = str(x)
    sum = 0
    for i in range(0, len(temp)):
        sum += int(temp[i])
    if x % sum == 0:
        return answer
    else:
        answer = False
    return answer