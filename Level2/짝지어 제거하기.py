s = 'gbacabbbaagtggtc'

def remove_(s):
    for i in range(0, len(s) - 1):
            temp = s[i]
            if s[i + 1] is temp:
                a = s.replace(temp + temp,'')
                return a
    return s

def solution(s):
    temp = ''
    if len(s) % 2 == 1:
        return 0
    else:
        a = s
        for i in range(0, int(len(s) / 2)):
            a = remove_(a)
            if len(a) == 0:
                return 1
    return 0
print(solution(s))