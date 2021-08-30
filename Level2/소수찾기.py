from itertools import permutations
import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            return False
    return True
            

def solution(numbers):
    answer = 0
    num = ''
    nums = []
    tem = []

    for i in range(0, len(numbers)):
        tem.append(int(numbers[i]))
    tem.sort()
    for i in range(0, len(tem)):
        num += str(tem[i])

    while True:
        temp = ''
        for i in range(0, len(temp)):
            temp += num[i]
            nums.append(int(temp))
        if permutations(num): continue
        break

    nums.sort()
    my_set = set(nums)
    nums = list(my_set)

    for i in range(0, len(nums)):
        if prime(nums[i]):
            answer += 1

    return answer