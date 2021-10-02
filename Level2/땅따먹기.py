land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
def solution(land):
    answer = 0
    n = land[0].index(max(land[0]))
    answer += max(land[0])
    for i in range(1, len(land)):
        if land[i][land[i].index(max(land[i]))] == n:
            land[i][land[i].index(max(land[i]))] = 0
            answer += max(land[i])
            n = land[i].index(max(land[i])) 
        else:
            answer += max(land[i])
            n = land[i].index(max(land[i]))
    return answer
print(solution(land))
