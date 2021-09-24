def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

'''
일단 string들을 먼저 사전순으로 정렬하고 그다음에 n번째 요소로 정렬한다.
'''