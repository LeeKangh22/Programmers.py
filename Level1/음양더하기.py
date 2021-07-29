def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i] is True:
            answer += absolutes[i]
        elif signs[i] is False:
            answer -= absolutes[i]

    return answer