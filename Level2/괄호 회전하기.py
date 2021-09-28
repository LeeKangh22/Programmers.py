s = "}]()[{"
def solution(s):
    answer = 0
    temp = []
    for j in range(0, len(s)):
        temp.append(s[j])
    for j in temp:
        if j == '(':
            for k in range(temp.index(j), len(s)):
                if temp[k] == ')':
                    temp.pop(temp.index(j))
                    temp.pop(k)
                    break
        elif j == '{':
            for k in range(temp.index(j), len(s)):
                if temp[k] == '}':
                    temp.pop(temp.index(j))
                    temp.pop(k)
                    break   
        elif j == '[':
            for k in range(temp.index(j), len(s)):
                if temp[k] == ']':
                    temp.pop(temp.index(j))
                    temp.pop(k)
                    break
    if len(temp) == 0:
        answer += 1
    for i in range(1, len(s)):
        temp = []
        s += s[0]
        s = s[1:]
        for j in range(0, len(s)):
            temp.append(s[j])
        for j in temp:
            if j == '(':
                for k in range(temp.index(j), len(s)):
                    if temp[k] == ')':
                        temp.pop(temp.index(j))
                        temp.pop(k)
                        break
            elif j == '{':
                for k in range(temp.index(j), len(s)):
                    if temp[k] == '}':
                        temp.pop(temp.index(j))
                        temp.pop(k)
                        break   
            elif j == '[':
                for k in range(temp.index(j), len(s)):
                    if temp[k] == ']':
                        temp.pop(temp.index(j))
                        temp.pop(k)
                        break
        if len(temp) == 0:
            answer += 1
    return answer
print(solution(s))