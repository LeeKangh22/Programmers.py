import random

number = "1924"


def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def solution(number, k):
    answer = ''
    temp = []
    for i in range(0, len(number)):
        temp.append(int(number[i]))
    count = 0
    while len(temp) > len(temp) - k:
        temp = bigger(temp.remove(random.choice(temp)),temp.remove(random.choice(temp)))
    print(temp)

            

    return answer
solution(number,2)