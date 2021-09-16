def solution(n,a,b):
    answer = 1  
    
    if b > a:
        while True:
            if b % 2 == 0 and b - a == 1:
                break
            else:
                if a % 2 == 1:
                    a = (a + 1) / 2
                else:
                    a = a / 2
                if b % 2 == 1:
                    b = (b + 1) / 2
                else:
                    b = b / 2
            answer += 1
            
    else: 
        while True:
            if a % 2 == 0 and a - b == 1:
                break
            else:
                if a % 2 == 1:
                    a = (a + 1) / 2
                else:
                    a = a / 2
                if b % 2 == 1:
                    b = (b + 1) / 2
                else:
                    b = b / 2
            answer += 1

    return answer
