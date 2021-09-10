citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    temp = []
    citations.sort()
    count = 0
    h_temp = []
    for i in range(0, len(citations)):
        print(citations)
        h = citations[i]
        count = len(citations)
        if count >= h:
            h_temp.append(h)
            citations.pop(0)
        else:
            break
    answer = max(h_temp)
    
    return answer
print(solution(citations))