s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
'''
,로 튜플로 나눈 다음에 괄호 싹다 없애기?
아니면 가장 긴 길이의 퓨틀 본 다음에 그걸로 답 내기?
방법 생각좀

'''

def solution(s):
    answer = []
    temp = []
    for i in range(0, len(s)):
        temp.append(s[i])
    
    temp.split("{")
    temp.split("}")
    
    my_set = set(temp)
    temp = list(my_set)
    print(temp) 
    return answer

solution(s)