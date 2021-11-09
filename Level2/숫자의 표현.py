n = 15
'''
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
'''

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            answer += 1
    return answer 
# 약수 중 홀수인 수의 개수와 같다..왜..?
print(solution(n))
