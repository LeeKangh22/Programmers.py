from itertools import *
word = "AAAAE"

def solution(word):
    answer = 0
    n = []
    for i in range(1, 6):
        n += list(product("AEIOU", repeat = i)) #해당 문자를 i개, 중복 허용하여 만들 수 있는 모든 경우의 수
    n.sort() #정렬이 되어있지 않으므로 정렬
    str = []
    for i in range(0, len(n)):
        str.append("".join(n[i])) #해당 리스트로 존재하는 문자들을 모두 문자열로 조합
    answer = str.index(word) + 1 #인덱스 + 1 반환
    
    
    return answer
print(solution(word))