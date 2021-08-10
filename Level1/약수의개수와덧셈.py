left = 13
right = 17

def hi(n):
    temp = 0
    for i in range(1, n + 1):
        if n % i == 0:
            temp += 1
    return temp


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if hi(i) % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer

print(solution(left,right))