def solution(price, money, count):
    total = 0
    for i in range(0, count):
        total += (i + 1) * price
    answer = money - total
    if answer < 0:
        answer = -answer
    else:
        answer = 0
    return answer