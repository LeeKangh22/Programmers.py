n = 15
def solution(n):
    answer = 0
    sum = 0
    for i in range(1, int(n / 2) + 1):
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                sum = 0
                break
        sum = 0
    return answer + 1
#시간 초과 코드
print(solution(n))
