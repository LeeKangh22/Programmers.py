number = "1924"
#solving

'''
앞에서부터 k개씩 검사한다. 여기서 가장 작은걸 뺀다.
이걸 k번 하면 큰 수가 만들어진다. 만약 가장 작은수가 맨 앞에 있으면 맨앞에 것을 뺀다. 
--> 알고리즘 틀린 것 같음. 테스트케이스 3개에서만 돌아감 시간초과도 뜸
'''

def solution(number, k):
    answer = ''
    temp = []
    for j in range(0, len(number)):
        temp.append(int(number[j]))
    for j in range(0, k):
        temp.remove(min(temp[0:k])) 
    for i in range(0, len(temp)):
        answer += str(temp[i])

    return answer
print(solution(number,2))