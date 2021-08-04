
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(0, len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer += 1
        else:
            break
    return answer