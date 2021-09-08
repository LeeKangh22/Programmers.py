from itertools import *
word = "AAAAE"
def solution(word):
    answer = 0
    n = []
    for i in range(1, 6):
        n += list(product("AEIOU", repeat = i))
    n.sort()
    str = []
    for i in range(0, len(n)):
        str.append("".join(n[i]))
    answer = str.index(word) + 1
    
    return answer
print(solution(word))