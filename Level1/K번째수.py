array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

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

answer = solution(array,commands)
print(answer)