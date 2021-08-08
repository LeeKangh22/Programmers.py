def solution(arr):
    answer = []
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] <= min:
            min = arr[i]
    arr.remove(min)
    if len(arr) == 0:
        arr.append(-1)
    answer = arr
    return answer