s = "}}}"
def solution(s):
    answer = 0
    switch1 = 0
    switch2 = 0
    if '(' in s:
        switch1 += 1
    if '{' in s:
        switch1 += 1
    if '[' in s:
        switch1 += 1
    for j in range(0, len(s)):
        if s[j] == '(':
            if ')' in s[j:]:
                switch2 += 1
        if s[j] == '{':
            if '}' in s[j:]:
                switch2 += 1
        if s[j] == '[':
            if ']' in s[j:]:
                switch2 += 1
    if switch1 == switch2:
        answer += 1       
    for i in range(1, len(s)):
        s += s[0]
        s = s[1:]
        switch2 = 0
        for j in range(0, len(s)):
            if s[j] == '(':
                if ')' in s[j:]:
                    switch2 += 1
            if s[j] == '{':
                if '}' in s[j:]:
                    switch2 += 1
            if s[j] == '[':
                if ']' in s[j:]:
                    switch2 += 1
        if switch1 == switch2:
            answer += 1       
    return answer
print(solution(s))