s = 'gbacabbbaagtggtc'
#답은 잘 나옴. 시간초과로 실패가 뜸
def remove_(s):
    a = s
    for i in range(0, len(s) - 1):
            temp = s[i]
            if s[i + 1] is temp:
                a = s.replace(temp + temp,'')
    return a

def solution(s):
    if len(s) % 2 == 1:
        return 0
    else:
        a = s
        count = 0
        while count == 0:
            a = remove_(a)
            if len(a) == len(remove_(a)):
                count += 1
            if len(a) == 0:
                return 1
            elif count == 1:
                return 0
    return 0
print(solution(s))