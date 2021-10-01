s = "}}}"
def solution(s):
    answer = 0
    temp = []
    for i in s:
        s += s[0]
        s = s[1:]
        for j in range(0, len(s)):
            temp.append(s[j])
            if len(temp) >= 2 and temp[-2] == '[':
                if temp[-1] == ']':
                    temp.pop()
                    temp.pop()
            if len(temp) >= 2 and temp[-2] == '{':
                if temp[-1] == '}':
                    temp.pop()
                    temp.pop()
            if len(temp) >= 2 and temp[-2] == '(':
                if temp[-1] == ')':
                    temp.pop()
                    temp.pop()
        if len(temp) == 0:
            answer += 1
            temp = []
        else:
            temp = []
            
    
    return answer
print(solution(s))