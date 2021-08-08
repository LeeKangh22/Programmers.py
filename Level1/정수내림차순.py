def solution(n):
    answer = 0
    string = str(n)
    temp = []
    for i in range(0, len(string)):
        temp.append(int(string[i]))
    temp.sort(reverse = True)
    string2 = ''
    for i in range(0, len(string)):
        temp[i] = str(temp[i])
        string2 += temp[i]
    answer = int(string2)
    return answer