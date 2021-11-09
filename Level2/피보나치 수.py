n=10000
def solution(n):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(2, n):
        fibo.append(fibo[i - 2] + fibo[i - 1])
    return (fibo[n - 2] + fibo[n - 1]) % 1234567
print(solution(n))