s = 'baabaa'

def solution(s):
    temp = []
    if len(s) == 1:
        return 0
    elif len(s) == 0:
        return 1
    else:
        temp.append(s[0])
        temp.append(s[1])
        if len(temp) >=2 and temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
        for i in range(2, len(s)):
            temp.append(s[i])
            if len(temp) >=2 and temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
            elif len(temp) < 2:
                continue
    if not temp:
        return 1
    else:
        return 0
    
print(solution(s))