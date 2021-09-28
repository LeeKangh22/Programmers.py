b = 2
w = 10
t = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    clear = []
    temp = []
    count = len(truck_weights)
    while len(clear) != count:
        va = 0
        if len(truck_weights) != 0:
            va = truck_weights[0]
        for i in range(bridge_length):
            while len(temp) <= bridge_length and sum(temp) + va <= weight:
                temp.append(truck_weights.pop(0))
                answer += 1
            clear.append(temp.pop(0))
            answer += 1
                    
    return answer
print(solution(b,w,t))