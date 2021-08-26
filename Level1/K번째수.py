def solution(array, commands):
    answer = []
    temp = []
    for j in range(0, len(commands)):
        for i in range(commands[j][0] - 1, commands[j][1]):
            temp.append(array[i])
        temp.sort()
        answer.append(temp[commands[j][2] - 1])
        temp = []

    return answer
