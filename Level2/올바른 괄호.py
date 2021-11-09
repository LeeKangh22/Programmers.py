def solution(s):
    
    temp = []
    if len(s) == 1 or len(s) == 0:
        return False
    else:
        for i in range(0, len(s)):
            temp.append(s[i])
            if len(temp) >= 2 and temp[-1] == ')' and temp[-2] == '(':
                temp.pop()
                temp.pop()
    if len(temp) == 0:
        return True
    else:
        return False
