
def solution(n, arr1, arr2): #다시 풀어보기
    answer = []
    
    for i in range(0, len(arr1)):
        string = ''
        arr1[i] = bin(arr1[i])
        for j in range(0, n - (len(arr1[i]) - 2)):
            string = string + '0'
        arr1[i] = string + arr1[i][2:]
    for i in range(0, len(arr2)):
        string = ''
        arr2[i] = bin(arr2[i])
        for j in range(0, n - (len(arr2[i]) - 2)):
            string = string + '0'
        arr2[i] = string + arr2[i][2:]
    for i in range(0, n):
        string = ''
        for j in range(0, n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                string += ' '
            else:
                string += '#'
        answer.append(string)
    return answer