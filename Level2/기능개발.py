def solution(progresses, speeds):
    answer = []
    count_stack = []
    count = 0
    for i in range(0, len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        count_stack.append(count)
    print(count_stack)
    progress = count_stack[0]
    count = 1
    for i in range(1, len(count_stack)):
        if count_stack[i] <= progress:
            count += 1
        else:
            answer.append(count)
            progress = count_stack[i]
            count = 1 
    answer.append(count)        
            
    return answer
