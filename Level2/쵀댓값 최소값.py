s = "-1 -2 -3 -4"

def solution(s):
    answer = ''
    temp = [] 
    temp = list(map(int, s.split()))
    
    answer += str(min(temp))
    answer += ' '
    answer += str(max(temp))
    print(temp)
    return answer
print(solution(s))