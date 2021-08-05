n=7

def solution(n):
    answer = 0
    three = int(str(n),3)
    temp = ''
    for i in range(0, 2):
        three[i] = three[len(three) - 1 - i]
    answer = int(three, 10)    

    return answer
print(solution(n))