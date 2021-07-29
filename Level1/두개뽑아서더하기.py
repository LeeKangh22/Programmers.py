def solution(numbers):
    answer = []
    temp = []
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp.append(numbers[i] + numbers[j])
        
    new_array = []
    for i in range(0, len(temp)):
        if temp[i] not in new_array:
            new_array.append(temp[i])
    new_array.sort()
    answer = new_array
    return answer