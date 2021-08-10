# 에라토스테네스의 체를 활용
# 소수 찾을 때에는 효율성을 위해 이를 공부해야 할 것 같다.
def solution(n):
    answer = 0
    a = [False,False] + [True]*(n-1)
    for i in range(2, n + 1):
        if a[i]:
            answer += 1
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return answer