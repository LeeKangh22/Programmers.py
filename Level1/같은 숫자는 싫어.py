def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    for i in range(1, len(arr)):
        if arr[i] != temp:
            temp = arr[i]
            answer.append(temp)

    return answer