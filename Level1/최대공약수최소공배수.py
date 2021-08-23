def solution(n, m):
    answer = []
    big = 0
    if n > m:
        big = n
    else:
        big = m
    temp = 0
    div = []
    for i in range(1, big):
        if n % i == 0 and m % i ==0:
            div.append(i)
    temp = max(div)
    answer.append(temp)        
    answer.append((m * n) / temp)
    return answer