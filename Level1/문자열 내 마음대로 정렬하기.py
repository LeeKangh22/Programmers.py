def solution(strings, n):
    answer = []
    return sorted(sorted(strings), key=lambda x:x[n])

