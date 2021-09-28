arr = [2,6,8,14]

def solution(arr):
    answer = 0
    lcm = 1
    for i in range(0, len(arr)):
        for j in range(max(arr[i], lcm), (arr[i] * lcm + 1)):
            if j % lcm == 0 and j % arr[i] == 0:
                lcm = j
                break
        answer = lcm
    return answer
    
print(solution(arr))