n = 123
def solution(n):
    answer = 0
    string = str(n)
    for i in range(0, len(string)):
        answer += int(string[i])
    return answer
print(solution(n))