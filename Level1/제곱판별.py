import math
def solution(n):
    answer = 0
    temp = math.sqrt(n)
    if temp - int(temp) == 0:
        answer = pow(temp + 1, 2)
    else:
        answer = -1
    return answer