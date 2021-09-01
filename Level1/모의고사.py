answers = [1,2,3,4,5]

def solution(answers):
    answer = []
    temp = []
    student1 = 0
    student2 = 0
    student3 = 0

    # 수포자 1 
    correct = 1
    for i in range(0, len(answers)):
        if correct > 5:
            correct = 1
        if correct == answers[i]:
            student1 += 1
        correct += 1
    temp.append(student1)
    
    # 수포자 2
    correct1 = 2
    correct2 = 1
    for i in range(0, len(answers)):
        if correct2 == 2:
            correct2 = 3
        if correct2 > 5:
            correct2 = 1
        if i % 2 == 0:
            if answers[i] == correct1:
                student2 += 1
        else:
            if answers[i] ==  correct2:
                student2 += 1
            correct2 += 1
    temp.append(student2)

    # 수포자 3
    switch = 0 # 같은 숫자가 두 번 나왔는 지 검사하는 스위치
    correct = 3
    for i in range(0, len(answers)):
        if answers[i] == correct:
            student3 += 1
        if correct == 3 and switch == 1:
            correct = 1
        elif correct == 5 and switch == 1:
            correct = 3
        elif correct == 2 and switch == 1:
            correct = 4
        elif (correct == 1 or correct == 4) and switch == 1:
            correct += 1
        if switch == 0:
            switch = 1
        elif switch == 1:
            switch = 0
    temp.append(student3)
    
    max = student1
    for i in range(1,3):
        if temp[i] >= max:
            max = temp[i]
    
    if max == student1:
        answer.append(1)
    if max == student2:
        answer.append(2)
    if max == student3:
        answer.append(3)

    return answer
answer = solution(answers)
print(answer)