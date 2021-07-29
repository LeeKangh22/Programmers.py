def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    temp = 0
    rank = 0
    for i in range(0, len(lottos)):
        if lottos[i] == 0:
            temp += 1
        elif lottos[i] in win_nums:
            rank += 1
    best = 0
    if temp + rank == 6:
        best = 1
    elif temp + rank == 5:
        best = 2
    elif temp + rank == 4:
        best = 3
    elif temp + rank == 3:
        best = 4
    elif temp + rank == 2:
        best = 5
    else:
        best = 6
    
    worst = 0
    if rank == 6:
        worst = 1
    elif rank == 5:
        worst = 2
    elif rank == 4:
        worst = 3
    elif rank == 3:
        worst = 4
    elif rank == 2:
        worst = 5
    else:
        worst = 6

    answer.append(best)
    answer.append(worst)
    return answer