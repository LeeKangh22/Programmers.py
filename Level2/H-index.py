citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    citations.sort()
    h_temp = []
    if len(citations) == 1:
        return 1
    for i in range(0, len(citations)):
        if citations[i] == 0:
            h_temp.append(0)
        else:
            for j in range(0, citations[i]):
                if j + 1 <= len(citations) - i:
                    h_temp.append(j + 1) 
    answer = max(h_temp)
    return answer
print(solution(citations))


    
    
